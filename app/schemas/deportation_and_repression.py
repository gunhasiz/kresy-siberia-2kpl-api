# app/schema/deportation_and_repression.py

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class DeportationAndRepressionCreate(BaseModel):
    other_information: Optional[str] = None
    places: List[Place] = []
    
class Place(BaseModel):
    from_when_date: Optional[date] = None
    to_when_date: Optional[date] = None
    from_yyyy: Optional[str] = None
    mm_first: Optional[str] = None
    dd_first: Optional[str] = None
    to_yyyy: Optional[str] = None
    mm_last: Optional[str] = None
    dd_last: Optional[str] = None
    deporting_authority: Optional[str] = None
    oblast: Optional[str] = None
    city: Optional[str] = None