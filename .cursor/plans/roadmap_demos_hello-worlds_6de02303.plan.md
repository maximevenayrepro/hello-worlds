---
name: roadmap demos hello-worlds
overview: "Roadmap of hello-world demos to add to the project, ordered by increasing difficulty. Each demo reproduces the same concept as the existing Python demo: minimal HTTP server returning JSON on `/`, 404 otherwise, with tests and Dockerfile."
todos:
  - id: demo-javascript-node
    content: "javascript-node: Node.js stdlib HTTP server"
    status: pending
  - id: demo-go
    content: "go: Go stdlib HTTP server"
    status: pending
  - id: demo-java
    content: "java: JDK HttpServer HTTP server"
    status: pending
  - id: demo-csharp
    content: "csharp: C# .NET minimal API HTTP server"
    status: pending
  - id: demo-rust
    content: "rust: Rust stdlib TcpListener HTTP server"
    status: pending
  - id: demo-cpp
    content: "cpp: C++ POSIX sockets HTTP server"
    status: pending
  - id: demo-c
    content: "c: C POSIX sockets HTTP server"
    status: pending
isProject: false
---

# Hello-world demo roadmap

## Common concept

Every demo reproduces the exact same pattern as `[python/](python/)`:

- A `hello()` function returning `"Hello, World!"`
- An HTTP server on port **8000** serving `{"message": "Hello, World!"}` as JSON on `GET /`
- A **404** response for any other path
- **3 tests**: unit test on `hello()`, integration on `/`, integration on an unknown path
- A working **Dockerfile**
- A **README** with run/test/docker instructions

---

## Order by increasing difficulty

### 1. `javascript-node` — Node.js (stdlib)

- **Difficulty**: trivial
- **Why**: the `http` module is built-in, JSON is native to the language
- **Entrypoint**: `index.js`
- **Tests**: `node:test` + `node:assert` (built-in since Node 18)
- **Deps**: none
- **Docker image**: `node:22-slim`

### 2. `go` — Go (stdlib)

- **Difficulty**: easy
- **Why**: `net/http` + `encoding/json` in stdlib, built-in tooling (`go test`)
- **Entrypoint**: `main.go`
- **Tests**: `testing` + `net/http/httptest` (stdlib)
- **Deps**: `go.mod` (no external dependency)
- **Docker image**: multi-stage with `golang:1.23` then `gcr.io/distroless/static-debian12`

### 3. `java` — Java (JDK)

- **Difficulty**: moderate
- **Why**: `com.sun.net.httpserver.HttpServer` is in the JDK but the API is verbose; no built-in test framework, JUnit needed
- **Entrypoint**: `Main.java`
- **Tests**: JUnit 5 (dependency managed manually or via a script)
- **Deps**: JUnit 5 jars (downloaded in Dockerfile, no Maven/Gradle to stay minimal)
- **Docker image**: `eclipse-temurin:21-jdk-jammy`

### 4. `csharp` — C# (.NET)

- **Difficulty**: moderate
- **Why**: .NET minimal API is very concise, but the .NET ecosystem (csproj, restore, build) adds structural complexity
- **Entrypoint**: `Program.cs`
- **Tests**: xUnit in a separate project or inline
- **Deps**: `.csproj` (.NET framework, no external NuGet for the server)
- **Docker image**: multi-stage `mcr.microsoft.com/dotnet/sdk:9.0` then `mcr.microsoft.com/dotnet/aspnet:9.0`

### 5. `rust` — Rust (stdlib)

- **Difficulty**: high
- **Why**: no HTTP server in stdlib; requires `std::net::TcpListener` and manual HTTP parsing/writing
- **Entrypoint**: `main.rs` (in `src/`)
- **Tests**: built-in `#[cfg(test)]` module
- **Deps**: `Cargo.toml` (no external dependency, HTTP done by hand)
- **Docker image**: multi-stage `rust:1.84-slim` then `debian:bookworm-slim`

### 6. `cpp` — C++ (sockets)

- **Difficulty**: high
- **Why**: no HTTP or JSON in stdlib; POSIX sockets + manual HTTP parsing + manual JSON construction
- **Entrypoint**: `main.cpp`
- **Tests**: functional test script (curl/wget in container) or header-only mini framework
- **Deps**: none (POSIX sockets)
- **Docker image**: multi-stage `gcc:14` then `debian:bookworm-slim`

### 7. `c` — C (sockets)

- **Difficulty**: maximum
- **Why**: same constraints as C++ but without classes, strings, or RAII — everything is manual memory and buffer management
- **Entrypoint**: `main.c`
- **Tests**: functional test script (most pragmatic in pure C)
- **Deps**: none (POSIX sockets + libc)
- **Docker image**: multi-stage `gcc:14` then `debian:bookworm-slim`

---

## Summary


| #   | Folder            | Language | Approach             | Difficulty |
| --- | ----------------- | -------- | -------------------- | ---------- |
| 1   | `javascript-node` | Node.js  | stdlib `http`        | trivial    |
| 2   | `go`              | Go       | stdlib `net/http`    | easy       |
| 3   | `java`            | Java     | JDK `HttpServer`     | moderate   |
| 4   | `csharp`          | C# .NET  | minimal API          | moderate   |
| 5   | `rust`            | Rust     | stdlib `TcpListener` | high       |
| 6   | `cpp`             | C++      | POSIX sockets        | high       |
| 7   | `c`               | C        | POSIX sockets        | maximum    |


---

## Notes

- **No frameworks**: every demo uses the bare minimum (stdlib or JDK), except C# where .NET minimal API is the idiomatic standard.
- **Natural progression**: from languages where an HTTP server fits in 15 lines, to those where everything must be coded by hand.
- The root README will be updated incrementally as each new demo is added.

