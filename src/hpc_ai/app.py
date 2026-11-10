"""Application factory; no model or external service is required at startup."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    service: Literal["hpc-ai"] = "hpc-ai"


def create_app() -> FastAPI:
    app = FastAPI(title="HPC AI", version="0.1.0")

    @app.get("/health", response_model=HealthResponse, tags=["health"])
    async def health() -> HealthResponse:
        """Report process liveness, not model readiness."""
        return HealthResponse()

    return app
