# Build stage
FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*
COPY helloworld.py /app/helloworld.py

# Runtime stage
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3-minimal && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/helloworld.py /app/helloworld.py
WORKDIR /app
CMD ["tail", "-f", "/dev/null"]
