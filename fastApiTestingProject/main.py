import os

import uvicorn
from fastapi import FastAPI
from loguru import logger

from notes.src.api import api_router


def init_app() -> FastAPI:
    """Create FastAPI app."""
    app = FastAPI()
    app.include_router(api_router)

    @app.on_event("startup")
    async def startup() -> None:
        logger.info("Startup: Message")

    @app.on_event("shutdown")
    async def shutdown() -> None:
        logger.info("Shutdown: Message")

    return app


if __name__ == "__main__":
    uvicorn.run(
        "main:init_app",
        host=os.getenv("NOTES_APP_HOST", "0.0.0.0"),
        port=int(os.getenv("NOTES_APP_PORT", 8000)),
        reload=True,
        factory=True,
    )
