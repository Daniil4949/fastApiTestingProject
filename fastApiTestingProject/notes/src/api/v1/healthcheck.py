# """Microservice healthcheck endpoints."""
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/")
async def get_health_check_status() -> JSONResponse:
    """Get health check status."""
    return JSONResponse(content={"message": "Success."}, status_code=200)