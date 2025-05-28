FROM ubuntu:22.04

RUN apt-get update && apt-get install -y curl wget gnupg ca-certificates && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://ollama.com/install.sh | bash

EXPOSE 11434

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["ollama", "serve"]

