# app/schema/record.py

from pydantic import BaseModel, ConfigDict
from typing import List, Optional

from .person import PersonCreate
from .personal_situation_outbreak import PersonalSituationOutbreakCreate
from .deportation_and_repression import DeportationAndRepressionCreate
from .repatriation import RepatriationCreate
from .occupation_period import OccupationPeriodCreate
from .military_experience import MilitaryExperienceCreate
from .other_military_experience import OtherMilitaryExperienceCreate
from .sources import SourceCreate
from .related_galleries import RelatedGalleryCreate

class RecordCreate(BaseModel):
    person: PersonCreate
    personal_situation_outbreak: Optional[PersonalSituationOutbreakCreate] = None
    deportation_and_repression: Optional[DeportationAndRepressionCreate] = None
    repatration: Optional[RepatriationCreate] = None
    occupation_period: Optional[OccupationPeriodCreate] = None
    military_experience: Optional[MilitaryExperienceCreate] = None
    other_military_experience: Optional[OtherMilitaryExperienceCreate] = None
    sources: List[SourceCreate] = []
    related_galleries: List[RelatedGalleryCreate] = []
    
    model_config = ConfigDict(from_attributes=True)

class RecordResponse(BaseModel):
    status: str
    message: str
    person_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)