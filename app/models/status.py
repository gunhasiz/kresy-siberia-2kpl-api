from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseDTO

class StatusDTO(BaseDTO):
    __tablename__: str = "statuses"
    
    id: Column[int] = Column(Integer, primary_key=True)

    # Id of an entry in the main table
    entry_id: Mapped[str] = mapped_column(String, nullable=True)
    # URL or reference to the source
    url: Mapped[str] = mapped_column(String, nullable=True)
    # Scrape status (e.g., "pending", "in_progress", "completed", "failed")
    status: Mapped[str] = mapped_column(String, nullable=True)