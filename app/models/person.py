from datetime import date

from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship, Mapped

from .base import BaseDTO
from .personal_situation_outbreak import PersonalSituationOutbreakOfWWIIDTO
from .deporation_and_repression import DeportationAndRepressionDTO
from .repatriation import RepatriationDTO
from .occupation_period import OccupationPeriodDTO
from .military_experience import MilitaryExperienceDTO
from .other_military_experience import OtherMilitaryExperienceDTO
from .sources import SourcesDTO
from .related_galleries import RelatedGalleriesDTO

class PersonDTO(BaseDTO):
    __tablename__ = "persons"

    id: Column[int] = Column(Integer, primary_key=True)

    # Entry ID
    external_entry_id: Column[int] = Column(Integer, unique=True, index=True)
    # Name
    full_name: Column[str] = Column(String, index=True)
    # Maiden Name
    maiden_name: Column[str] = Column(String, nullable=True)
    # Nickname/Pseudonym
    nickname: Column[str] = Column(String, nullable=True)
    # Gender
    gender: Column[str] = Column(String, nullable=True)
    # Date of birth
    birth_date: Column[date] = Column(Date, nullable=True)
    # Place of birth
    birth_place: Column[str] = Column(String, nullable=True)
    # Did this person die during World War ll?
    died_in_ww2: Column[bool] = Column(Boolean, default=False)
    # Date of death
    death_date: Column[date] = Column(Date, nullable=True)
    # Place of death
    death_place: Column[str] = Column(String, nullable=True)
    # Cause of death
    death_cause: Column[str] = Column(String, nullable=True)
    # Fathers given name
    father_name: Column[str] = Column(String, nullable=True)
    # Mothers given name
    mother_name: Column[str] = Column(String, nullable=True)
    # Mothers maiden name
    mother_maiden_name: Column[str] = Column(String, nullable=True)
    # Given name of spuse:
    spouse_name: Column[str] = Column(String, nullable=True)
    # Maiden name of spouse:
    spouse_maiden_name: Column[str] = Column(String, nullable=True)
    # Given name(s) of childern:
    children_names: Column[str] = Column(String, nullable=True)
    # Description
    description: Column[str] = Column(String, nullable=True)

    personal_situation_outbreak: Mapped["PersonalSituationOutbreakOfWWIIDTO"] = relationship(
        "PersonalSituationOutbreakOfWWIIDTO",
        back_populates="person",
        uselist=False)
    deportations_and_repressions: Mapped["DeportationAndRepressionDTO"] = relationship(
        "DeportationAndRepressionDTO",
        back_populates="person",
        uselist=False)
    repatriations: Mapped["RepatriationDTO"] = relationship(
        "RepatriationDTO",
        back_populates="person",
        uselist=False)
    occupation_periods: Mapped["OccupationPeriodDTO"] = relationship(
        "OccupationPeriodDTO",
        back_populates="person",
        uselist=False)
    military_experiences: Mapped["MilitaryExperienceDTO"] = relationship(
        "MilitaryExperienceDTO",
        back_populates="person",
        uselist=False)
    other_military_experiences: Mapped["OtherMilitaryExperienceDTO"] = relationship(
        "OtherMilitaryExperienceDTO",
        back_populates="person",
        uselist=False)
    sources: Mapped[list["SourcesDTO"]] = relationship(
        "SourcesDTO",
        back_populates="person",
        uselist=False)
    related_galleries: Mapped[list["RelatedGalleriesDTO"]] = relationship(
        "RelatedGalleriesDTO",
        back_populates="person",
        uselist=False)