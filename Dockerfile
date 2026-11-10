FROM ghcr.io/astral-sh/uv:0.11.26 AS uv
FROM python:3.12-slim-bookworm

COPY --from=uv /uv /usr/local/bin/uv
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HPC_AI_HOST=0.0.0.0 \
    HPC_AI_PORT=8000 \
    PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN uv sync --locked --no-dev --no-editable \
    && groupadd --gid 10001 app \
    && useradd --uid 10001 --gid app --no-create-home app

USER app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.environ.get('HPC_AI_PORT', '8000') + '/health', timeout=2)"
CMD ["hpc-ai"]
