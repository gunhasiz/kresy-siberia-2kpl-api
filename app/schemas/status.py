from pydantic import BaseModel, ConfigDict

class StatusCreate(BaseModel):
    entry_id: str
    url: str
    status: str = "pending"

class StatusResponse(StatusCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)