from pydantic import BaseModel
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogOut(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True
