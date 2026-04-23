from sqlalchemy.ext.asyncio import AsyncSession

from app.models.status import StatusDTO
from app.schemas.status import StatusCreate

async def create_status(db: AsyncSession, obj_in: StatusCreate) -> StatusDTO:
    db_obj = StatusDTO(
        entry_id=obj_in.entry_id,
        url=obj_in.url,
        status=obj_in.status
    )
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj