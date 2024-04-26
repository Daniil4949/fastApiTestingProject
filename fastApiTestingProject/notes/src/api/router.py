"""Module which maps routers to use."""
from fastapi import APIRouter


from notes.src.api.v1 import router as api_v1

api_router = APIRouter(prefix="/api")
api_router.include_router(api_v1, prefix="/v1")