"""Run the optional HTTP service with `uv run hpc-ai`."""

import uvicorn

from hpc_ai.settings import Settings


def main() -> None:
    settings = Settings()
    uvicorn.run(
        "hpc_ai.app:create_app",
        factory=True,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
    )


if __name__ == "__main__":
    main()
