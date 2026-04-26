from datetime import date

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from .base import BaseDTO

class RepatriationDTO(BaseDTO):
    __tablename__: str = "repatriations"

    id: Column[int] = Column(Integer, primary_key=True)
    person_id: Column[int] = Column(Integer, ForeignKey("persons.id"), nullable=False)

    # Date of return to Poland
    return_date: Column[str] = Column(String, nullable=True)
    # Place of return to Poland
    province: Column[str] = Column(String, nullable=True)
    # District of return to Poland
    county: Column[str] = Column(String, nullable=True)
    # Locality of return to Poland
    locality: Column[str] = Column(String, nullable=True)
    # Nearest large city to place of return to Poland
    nearest_large_city: Column[str] = Column(String, nullable=True)

    person: Mapped["PersonDTO"] = relationship(
        "PersonDTO",
        back_populates="repatriations",
        uselist=False
        )