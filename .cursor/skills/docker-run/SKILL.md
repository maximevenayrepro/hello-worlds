---
name: docker-run
description: Build and run a demo's Docker container. Use when the user wants to run, test, or deploy a demo with Docker, or says "run the demo" or "docker".
---

# Docker Run

## Workflow

1. **Identify the demo folder** (ask if ambiguous)
2. **Verify `Dockerfile` exists** in the demo folder
3. **Build the image**:
   ```bash
   docker build -t hello-worlds/{demo-name} {demo-folder}/
   ```
4. **Run the container**:
   ```bash
   docker run --rm hello-worlds/{demo-name}
   ```
   For web demos that expose a port, add port mapping:
   ```bash
   docker run --rm -p {host-port}:{container-port} hello-worlds/{demo-name}
   ```
5. **Report the result** — show output, confirm it works

## Conventions

- Image name: `hello-worlds/{demo-name}` (e.g. `hello-worlds/python-fastapi`)
- Always use `--rm` to clean up the container after exit
- For web demos, use the port defined in the Dockerfile's `EXPOSE` directive
