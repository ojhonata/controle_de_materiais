from sqlalchemy import select
from sqlalchemy.orm import Session

from data.models.user import User


def get_all_user(session: Session) -> list[User]:
    return session.execute(select(User)).scalars().all()  # pyright: ignore
