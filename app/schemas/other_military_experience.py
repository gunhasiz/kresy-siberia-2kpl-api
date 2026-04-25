# app/schemas/other_military_experience.py

from pydantic import BaseModel
from typing import Optional

class OtherMilitaryExperienceCreate(BaseModel):
    information: Optional[str] = None
    orphanages: Optional[str] = None
    civilian_camp_middle_east: Optional[str] = None
    civilian_camp_india: Optional[str] = None
    civilian_camp_africa: Optional[str] = None
    other_information: Optional[str] = None