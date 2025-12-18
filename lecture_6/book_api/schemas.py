from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    
    @field_validator("title", "author")
    @classmethod
    def validate_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Field cannot be empty or contain only whitespace")
        return v.strip()


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
