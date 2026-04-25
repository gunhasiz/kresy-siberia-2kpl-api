# app/crud/record.py

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.person import PersonDTO
from app.models.personal_situation_outbreak import PersonalSituationOutbreakOfWWIIDTO
from app.models.deporation_and_repression import DeportationAndRepressionDTO
from app.models.repatriation import RepatriationDTO
from app.models.occupation_period import OccupationPeriodDTO
from app.models.military_experience import MilitaryExperienceDTO
from app.models.other_military_experience import OtherMilitaryExperienceDTO
from app.models.sources import SourcesDTO
from app.models.related_galleries import RelatedGalleriesDTO
from app.schemas.record import RecordCreate

async def create_full_record(db: AsyncSession, obj_in: RecordCreate) -> PersonDTO:
    db_person = PersonDTO(**obj_in.person.model_dump())

    if obj_in.personal_situation_outbreak:
        db_person.personal_situation_outbreak = PersonalSituationOutbreakOfWWIIDTO(
            **obj_in.personal_situation_outbreak.model_dump()
        )

    if obj_in.deportation_and_repression:
        db_person.deportations_and_repressions = DeportationAndRepressionDTO(
            **obj_in.deportation_and_repression.model_dump()
        )

    if obj_in.repatration:
        db_person.repatriations = RepatriationDTO(
        **obj_in.repatration.model_dump()
    )

    if obj_in.occupation_period:
        db_person.occupation_periods = OccupationPeriodDTO(
            **obj_in.occupation_period.model_dump()
        )
    
    if obj_in.military_experience:
        db_person.military_experiences = MilitaryExperienceDTO(
            **obj_in.military_experience.model_dump()
        )

    if obj_in.other_military_experience:
        db_person.other_military_experiences = OtherMilitaryExperienceDTO(
            **obj_in.other_military_experience.model_dump()
        )

    if obj_in.sources:
        db_person.sources = [
            SourcesDTO(**source.model_dump()) 
            for source in obj_in.sources
        ]

    if obj_in.related_galleries:
        db_person.related_galleries = [
            RelatedGalleriesDTO(**gallery.model_dump()) 
            for gallery in obj_in.related_galleries
        ]

    db.add(db_person)
    await db.commit()
    await db.refresh(db_person)
    
    return db_person