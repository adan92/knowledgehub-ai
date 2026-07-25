from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    filename: str
    size: int
    modified: datetime


class MessageResponse(BaseModel):
    message: str
