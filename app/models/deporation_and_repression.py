from datetime import date

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from .base import BaseDTO

class DeportationAndRepressionDTO(BaseDTO):
    __tablename__: str = "deportations_and_repressions"

    id: Column[int] = Column(Integer, primary_key=True)
    person_id: Column[int] = Column(
        Integer, ForeignKey("persons.id"), nullable=False)

    # Other information about deportation or repression
    other_information: Column[str] = Column(Text)

    places:Mapped[list["PlacesDTO"]]  = relationship(
        "PlacesDTO",
        back_populates="deportations_and_repressions",
        uselist=True
        )
    person: Mapped["PersonDTO"] = relationship(
        "PersonDTO",
        back_populates="deportations_and_repressions",
        uselist=False
        )


class PlacesDTO(BaseDTO):
    __tablename__: str = "places"

    id: Column[int] = Column(Integer, primary_key=True)
    deportation_id: Column[int] = Column(Integer, ForeignKey("deportations_and_repressions.id"), nullable=False)

    # When deportation or repression took place
    from_when_date: Column[date] = Column(Date, nullable=True)
    # When deportation or repression ended (if applicable)
    to_when_date: Column[date] = Column(Date, nullable=True)
    from_yyyy: Column[str] = Column(String, nullable=True)
    mm_first: Column[str] = Column(String, nullable=True)
    dd_first: Column[str] = Column(String, nullable=True)
    to_yyyy: Column[str] = Column(String, nullable=True)
    mm_last: Column[str] = Column(String, nullable=True)
    dd_last: Column[str] = Column(String, nullable=True)
    # Authority or institution that ordered or carried out the deportation or repression
    deporting_authority: Column[str] = Column(String, nullable=True)
    # Location of deportation or repression
    oblast: Column[str] = Column(String, nullable=True)
    # City or town of deportation or repression
    city: Column[str] = Column(String, nullable=True)
    
    deportations_and_repressions: Mapped["DeportationAndRepressionDTO"] = relationship(
        "DeportationAndRepressionDTO",
        back_populates="places",
        uselist=False
    )
