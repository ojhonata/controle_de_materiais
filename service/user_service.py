from sqlalchemy.orm import Session

from data.models.user import User
from data.repository import user_repository
from schemas.user_schema import UserCreate


def get_all(session: Session) -> list[User]:
    return user_repository.get_all_user(session)


def get_user_by_cs(session: Session, cs: int) -> User:
    if len(str(cs)) != 6:
        raise ValueError("cs inválida")

    user = user_repository.get_by_cs(session, cs)

    if not user:
        raise ValueError(f"Usuário com a cs {cs} não encontradao")

    if not user.active:
        raise ValueError("Usuário desativado")

    return user


def post_user(session: Session, data: UserCreate) -> User:
    existing_user = user_repository.get_by_cs(session, data.cs)

    if len(str(data.cs)) != 6:
        raise ValueError("cs inválida")

    if existing_user:
        raise ValueError("Usuário ja cadastrado")
    return user_repository.creat_user(session, data)
