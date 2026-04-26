from typing import Tuple

from sqlalchemy import Result, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.status import StatusDTO
from app.schemas.status import StatusCreate

async def create_status(db: AsyncSession, obj_in: StatusCreate) -> StatusDTO:
    query: Select[Tuple[StatusDTO]] = select(StatusDTO).where(StatusDTO.entry_id == obj_in.entry_id)
    result: Result[Tuple[StatusDTO]] = await db.execute(query)
    db_obj: StatusDTO | None = result.scalars().first()
    
    if db_obj:
        if db_obj.status != obj_in.status:
            db_obj.status = obj_in.status
    else:
        db_obj = StatusDTO(
            entry_id=obj_in.entry_id,
            url=obj_in.url,
            status=obj_in.status
        )
        db.add(db_obj)

    await db.commit()
    await db.refresh(db_obj)
    return db_obj