const { describe, it, before, after } = require("node:test");
const assert = require("node:assert/strict");
const http = require("node:http");
const { hello, server } = require("./index");

describe("hello", () => {
  it("returns the greeting string", () => {
    assert.equal(hello(), "Hello, World!");
  });
});

describe("HTTP server", () => {
  let baseUrl;

  before((_, done) => {
    server.listen(0, "127.0.0.1", () => {
      const { port } = server.address();
      baseUrl = `http://127.0.0.1:${port}`;
      done();
    });
  });

  after((_, done) => {
    server.close(done);
  });

  it("GET / returns JSON greeting", (_, done) => {
    http.get(`${baseUrl}/`, (res) => {
      assert.equal(res.statusCode, 200);
      assert.equal(res.headers["content-type"], "application/json");
      let body = "";
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () => {
        assert.deepEqual(JSON.parse(body), { message: "Hello, World!" });
        done();
      });
    });
  });

  it("GET /unknown returns 404", (_, done) => {
    http.get(`${baseUrl}/unknown`, (res) => {
      assert.equal(res.statusCode, 404);
      res.resume();
      res.on("end", done);
    });
  });
});
