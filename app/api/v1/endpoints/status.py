from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.status import StatusCreate, StatusResponse
from app.crud import status as crud_status

router = APIRouter()

@router.post("/", response_model=StatusResponse)
async def post_status(
    *,
    db: AsyncSession = Depends(get_db),
    status_in: StatusCreate
) -> crud_status.StatusDTO:
    return await crud_status.create_status(db=db, obj_in=status_in)