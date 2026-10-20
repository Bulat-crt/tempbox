from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    text: str
    ttl_seconds: int = Field(gt=0)

class NoteResponse(BaseModel):
    key: str
    ttl_seconds: int

class NoteDetail(BaseModel):
    key: str
    text: str
    ttl_seconds: int