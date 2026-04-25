# app/api/v1/endpoints/records.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.record import RecordCreate
from app.crud import record as crud_record

router = APIRouter()

@router.post("/")
async def upload_record(
    *,
    db: AsyncSession = Depends(get_db),
    record_in: RecordCreate
):
    try:
        new_record: crud_record.PersonDTO = await crud_record.create_full_record(db=db, obj_in=record_in)
        return {
            "status": "success",
            "message": "Record added successfully",
            "person_id": new_record.id}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))