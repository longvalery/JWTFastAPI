from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    login: str
    email: EmailStr
    password: str
    full_name: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True

class UserOut(BaseModel):
    id: int
    login: str
    email: EmailStr
    full_name: Optional[str] = None

    class Config:
        from_attributes = True  # Для Pydantic v2