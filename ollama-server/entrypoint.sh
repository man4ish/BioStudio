#!/bin/bash
set -e

echo "[INFO] Starting entrypoint script..."

# Wait a few seconds to ensure Ollama is initialized (optional)
sleep 2

# Pull required models (if not already pulled)
if ! ollama list | grep -q 'llama3'; then
    echo "[INFO] Pulling llama3..."
    ollama pull llama3
fi

if ! ollama list | grep -q 'deepseek-v1'; then
    echo "[INFO] Pulling deepseek-v1..."
    ollama pull deepseek-v1
fi

echo "[INFO] Models ready. Starting Ollama server..."
exec "$@"

