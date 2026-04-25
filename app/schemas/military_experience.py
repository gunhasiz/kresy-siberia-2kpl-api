# app/schemas/military_experience.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class MilitaryExperienceCreate(BaseModel):
    other_military_service: Optional[str] = None
    participation_in_wwii_battles: Optional[str] = None
    medals_received: Optional[str] = None
    other_battles: Optional[str] = None
    military_services: List[MilitaryService] = []

class MilitaryService(BaseModel):
    served_in: Optional[str] = None
    unit_name: Optional[str] = None
    rank: Optional[str] = None
    from_when_date: Optional[date] = None
    to_when_date: Optional[date] = None
    from_yyyy: Optional[str] = None
    mm_first: Optional[str] = None
    dd_first: Optional[str] = None
    to_yyyy: Optional[str] = None
    mm_last: Optional[str] = None
    dd_last: Optional[str] = None