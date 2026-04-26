# app/crud/record.py

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.person import PersonDTO
from app.models.personal_situation_outbreak import PersonalSituationOutbreakOfWWIIDTO
from app.models.deporation_and_repression import DeportationAndRepressionDTO, PlacesDTO
from app.models.repatriation import RepatriationDTO
from app.models.occupation_period import OccupationPeriodDTO
from app.models.military_experience import MilitaryExperienceDTO, MilitaryServiceDTO
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

    if obj_in.deportation_and_repression and obj_in.deportation_and_repression.places:
        db_person.deportations_and_repressions = DeportationAndRepressionDTO(
            other_information=obj_in.deportation_and_repression.other_information,
            places=[
                PlacesDTO(**place.model_dump()) 
                for place in obj_in.deportation_and_repression.places
            ]
        )

    if obj_in.repatration:
        db_person.repatriations = RepatriationDTO(
        **obj_in.repatration.model_dump()
    )

    if obj_in.occupation_period:
        db_person.occupation_periods = OccupationPeriodDTO(
            **obj_in.occupation_period.model_dump()
        )
    
    if obj_in.military_experience and obj_in.military_experience.military_services:
        db_person.military_experiences = MilitaryExperienceDTO(
            other_military_service=obj_in.military_experience.other_military_service,
            participation_in_wwii_battles=obj_in.military_experience.participation_in_wwii_battles,
            medals_received=obj_in.military_experience.medals_received,
            other_battles=obj_in.military_experience.other_battles,
            military_services=[
                MilitaryServiceDTO(**service.model_dump()) 
                for service in obj_in.military_experience.military_services
            ]
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