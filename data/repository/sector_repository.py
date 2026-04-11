from sqlalchemy import select
from sqlalchemy.orm import Session

from data.models.sector import Sector
from schemas.sector_schema import SectorCreate


def get_all_sector(session: Session) -> list[Sector]:
    return session.execute(select(Sector)).scalars().all() #pyright: ignore

def get_by_id(session: Session, name: str) -> Sector | None:
    return session.execute(select(Sector).where(Sector.name == name)).scalars().first()

def create_sector(session: Session, data: SectorCreate) -> Sector:
    sector = Sector(name = data.name)
    session.add(sector)
    session.commit()
    session.refresh(sector)

    return sector

