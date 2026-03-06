import threading
import unittest
import json
from urllib.error import HTTPError
from urllib.request import urlopen

from main import hello, HelloHandler
from http.server import HTTPServer


class TestHello(unittest.TestCase):
    def test_hello_returns_string(self):
        assert hello() == "Hello, World!"


class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), HelloHandler)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test_root_returns_json(self):
        with urlopen(f"http://127.0.0.1:{self.port}/") as res:
            assert res.status == 200
            body = json.loads(res.read())
            assert body == {"message": "Hello, World!"}

    def test_unknown_path_returns_404(self):
        with self.assertRaises(HTTPError) as ctx:
            urlopen(f"http://127.0.0.1:{self.port}/nope")
        assert ctx.exception.code == 404


if __name__ == "__main__":
    unittest.main()
