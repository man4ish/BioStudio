# docker-ollama-llm-models

Minimal Docker setup to run Ollama LLM models inside a container.

## Description

This Docker image installs the Ollama runtime on Ubuntu 22.04, exposes the default Ollama server port (`11434`),  
and uses an entrypoint script to start the Ollama server.

## Usage

1. Build the Docker image:

```bash
   docker build -t ollama-llm-models .
```
Run the container and expose port 11434:

```
docker run -p 11434:11434 ollama-llm-models
```

The Ollama server will start inside the container, ready to serve LLM models.

## Files
- Dockerfile: Builds the image with Ollama runtime installed.

- entrypoint.sh: Entrypoint script to launch the Ollama server.
