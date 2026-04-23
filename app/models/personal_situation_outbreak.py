from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from .base import BaseDTO

if TYPE_CHECKING:
    from .person import PersonDTO

class PersonalSituationOutbreakOfWWIIDTO(BaseDTO):
    __tablename__: str = "personal_situation_outbreak"

    id: Column[int] = Column(Integer, primary_key=True)
    person_id: Column[int] = Column(
        Integer, ForeignKey("persons.id"), nullable=False)

    # Residence at the outbreak of WWII
    residence: Column[str] = Column(String, nullable=True)
    # Kresy Inhabitant Status:
    kresy_inhabitant_status: Column[str] = Column(String, nullable=True)
    # Ethnicity
    ethnicity: Column[str] = Column(String, nullable=True)
    # Religion
    religion: Column[str] = Column(String, nullable=True)
    # Education Level
    education_level: Column[str] = Column(String, nullable=True)
    # Occupation at the outbreak of WWII
    occupation: Column[str] = Column(String, nullable=True)
    # Military status at the outbreak of WWII
    military_status: Column[str] = Column(String, nullable=True)
    # Military Rank at the outbreak of WWII
    military_rank: Column[str] = Column(String, nullable=True)

    person: Mapped["PersonDTO"] = relationship(
        "PersonDTO",
        back_populates="personal_situation_outbreak",
        uselist=False
        )
