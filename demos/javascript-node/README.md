# JavaScript (Node.js)

A minimal HTTP server using only the Node.js standard library. Returns `{"message": "Hello, World!"}` on `/`.

## Prerequisites

- Node.js 22+

## Run

```bash
node index.js
```

The server starts on <http://localhost:8000>.

## Test

### Unit tests

```bash
node --test index.test.js
```

Runs 3 tests:

| Test | What it checks |
|------|----------------|
| `returns the greeting string` | `hello()` returns `"Hello, World!"` |
| `GET / returns JSON greeting` | `GET /` responds `200` with `{"message": "Hello, World!"}` |
| `GET /unknown returns 404` | `GET /unknown` responds `404` |

### Docker

```bash
docker build -t hello-worlds/javascript-node .
docker run --rm -d -p 8000:8000 hello-worlds/javascript-node
```

Verify the logs show the server started:

```bash
docker logs <container-id>
# Hello, World!
# Serving on http://localhost:8000
```

Then open <http://localhost:8000> in a browser to confirm the JSON response.

Stop the container when done:

```bash
docker stop <container-id>
```
