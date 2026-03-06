# Python

A minimal HTTP server using only the standard library. Returns `{"message": "Hello, World!"}` on `/`.

## Prerequisites

- Python 3.12+

## Run

```bash
python main.py
```

The server starts on <http://localhost:8000>.

## Test

### Unit tests

```bash
python -m unittest test_main -v
```

Runs 3 tests:

| Test | What it checks |
|------|----------------|
| `test_hello_returns_string` | `hello()` returns `"Hello, World!"` |
| `test_root_returns_json` | `GET /` responds `200` with `{"message": "Hello, World!"}` |
| `test_unknown_path_returns_404` | `GET /nope` responds `404` |

### Docker

```bash
docker build -t hello-worlds/python .
docker run --rm -d -p 8000:8000 hello-worlds/python
```

Verify the logs show the server started:

```bash
docker logs <container-id>
# Hello, World!
# Serving on http://localhost:8000
```

Then open <http://localhost:8000> in a browser to confirm the JSON response.

> **Note:** `curl` / `Invoke-WebRequest` from the host shell may hang or time out when targeting a Docker container on `localhost` (observed on Windows with Docker Desktop). The Cursor IDE embedded browser (`browser_navigate` MCP tool) or a regular browser work reliably. If you need a CLI check, `docker exec` into the container instead:
>
> ```bash
> docker exec <container-id> python -c "from urllib.request import urlopen; print(urlopen('http://localhost:8000/').read())"
> ```

Stop the container when done:

```bash
docker stop <container-id>
```
