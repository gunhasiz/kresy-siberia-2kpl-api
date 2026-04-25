# app/schemas/related_galleries.py

from pydantic import BaseModel
from typing import Optional

class RelatedGalleryCreate(BaseModel):
    summary: Optional[str] = None
    url_text: Optional[str] = None
    url: Optional[str] = None