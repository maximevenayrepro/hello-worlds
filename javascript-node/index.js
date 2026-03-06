const http = require("node:http");

function hello() {
  return "Hello, World!";
}

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/") {
    const body = JSON.stringify({ message: hello() });
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(body);
  } else {
    res.writeHead(404);
    res.end();
  }
});

if (require.main === module) {
  console.log(hello());
  server.listen(8000, "0.0.0.0", () => {
    console.log("Serving on http://localhost:8000");
  });
}

module.exports = { hello, server };
