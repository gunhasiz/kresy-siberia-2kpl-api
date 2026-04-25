# app/schemas/sources.py

from pydantic import BaseModel
from typing import Optional

class SourceCreate(BaseModel):
    summary: Optional[str] = None
    url_text: Optional[str] = None
    url: Optional[str] = None