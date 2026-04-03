from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    name: str
    cs: int
    sector_id: int

    class Config:
        orm_mode = True

class UserCreate(UserSchema):
    role: str = "user"

    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    name: str | None = None
    cs: int | None = None
    sector: int | None = None

class UserResponse(UserSchema):
    id: UUID
    active: bool

    model_config = ConfigDict(from_attributes=True) # mapeamento
