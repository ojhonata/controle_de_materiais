from pydantic import BaseModel


class SectorResponse(BaseModel):
    id: int
    name: str


class SectorCreate(BaseModel):
    name: str


class SectroUpdate(BaseModel):
    name: str | None
