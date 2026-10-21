from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    text: str = Field(min_length=1, max_length=1000)
    ttl_seconds: int = Field(gt=0, le=86400)

class NoteResponse(BaseModel):
    key: str
    ttl_seconds: int

class NoteDetail(BaseModel):
    key: str
    text: str
    ttl_seconds: int