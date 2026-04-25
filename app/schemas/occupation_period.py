# app/schemas/occupation_period.py

from pydantic import BaseModel
from typing import Optional

class OccupationPeriodCreate(BaseModel):
    province: Optional[str] = None
    county: Optional[str] = None
    city_place: Optional[str] = None
    nearest_large_city: Optional[str] = None