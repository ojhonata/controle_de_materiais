from sqlalchemy.orm import Session

from data.models.sector import Sector
from data.repository import sector_repository
from schemas.sector_schema import SectorCreate


def get_all(session: Session) -> list[Sector]:
    return sector_repository.get_all_sector(session)


def get_sector_by_id(session: Session, name: str) -> Sector:
    sector = sector_repository.get_by_id(session, name)

    if not sector:
        raise ValueError("Usuário não encontrado")

    return sector


def post_sector(session: Session, data: SectorCreate) -> Sector:
    existing_sector = sector_repository.get_by_id(session, data.name)

    if existing_sector:
        raise ValueError("Setor já cadastrado!")
    return sector_repository.create_sector(session, data)
