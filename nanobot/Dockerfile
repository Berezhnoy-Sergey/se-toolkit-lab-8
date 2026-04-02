FROM harbor.pg.innopolis.university/docker-hub-cache/python:3.14-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy all local dependencies
COPY mcp /app/mcp
COPY nanobot-websocket-channel /app/nanobot-websocket-channel

# Copy nanobot project files
COPY nanobot/pyproject.toml nanobot/uv.lock ./

# Install dependencies (with local mcp-lms and mcp-webchat)
RUN uv sync --frozen --no-dev

# Copy the rest of nanobot
COPY nanobot/ .

# Create workspace directory
RUN mkdir -p /app/nanobot/workspace

# Ensure nanobot is in PATH
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "/app/nanobot/entrypoint.py"]
