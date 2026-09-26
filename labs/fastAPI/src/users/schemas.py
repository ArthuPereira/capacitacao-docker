from datetime import datetime

from pydantic import EmailStr, Field

from ..core.basemodel import CustomModel


class UserCreate(CustomModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr


class UserUpdate(CustomModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: EmailStr | None = None


class UserResponse(CustomModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime