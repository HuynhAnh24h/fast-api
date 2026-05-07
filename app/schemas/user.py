from pydantic import BaseModel, EmailStr, Field
from app.schemas.profile import ProfileResponse

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class UserUpdate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=73)
    role: str
    is_active: bool

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    profile: ProfileResponse | None = None

    class Config:
        from_attributes: True
