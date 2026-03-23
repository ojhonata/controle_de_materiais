from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    name: str
    cs: int
    sector_id: int

class UserCreate(UserSchema):
    pass

class UserUpdate(BaseModel):
    name: str | None = None
    cs: int | None = None
    sector: int | None = None

class UserResponse(UserSchema):
    id: UUID
    active: bool

    model_config = ConfigDict(from_attributes=True) # mapeamento
