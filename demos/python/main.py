import json
from http.server import HTTPServer, BaseHTTPRequestHandler


def hello():
    return "Hello, World!"


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = json.dumps({"message": hello()})
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body.encode())
        else:
            self.send_error(404)

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    print(hello())
    server = HTTPServer(("0.0.0.0", 8000), HelloHandler)
    print("Serving on http://localhost:8000")
    server.serve_forever()
