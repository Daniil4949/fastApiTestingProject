"""Package with common v1 routes for current service."""

from fastapi import APIRouter

from notes.src.api.v1.healthcheck import router as healthcheck

router = APIRouter()

router.include_router(healthcheck, tags=["HealthCheck"], prefix="/health-check")
