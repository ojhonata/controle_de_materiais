from sqlalchemy import select
from sqlalchemy.orm import Session

from data.models.user import User
from schemas.user_schema import UserCreate


def get_all_user(session: Session) -> list[User]:
    return session.execute(select(User)).scalars().all()  # pyright: ignore


def get_by_cs(session: Session, cs: int) -> User | None:
    return session.execute(select(User).where(User.cs == cs)).scalars().first()


def creat_user(session: Session, data: UserCreate) -> User:
    user = User(name=data.name, cs=data.cs, sector_id=data.sector_id)
    session.add(user)
    session.commit()
    session.refresh(user)

    return user
