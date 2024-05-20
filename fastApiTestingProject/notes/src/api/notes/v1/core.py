from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=..., dependencies=[Depends()])
async def get_all_notes():
    pass
