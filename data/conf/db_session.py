import os
from pathlib import Path

import sqlalchemy as sa
from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from data.models.model_base import ModelBase

load_dotenv()
__engine: Engine | None = None


# config banco de dados
def create_engine(sqlite: bool = False) -> Engine:
    global __engine

    if __engine:
        return __engine
    if sqlite:
        arquivo_db = "db/controle_materiais.sqlite"
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f"sqlite:///{arquivo_db}"
        __engine = sa.create_engine(
            url=conn_str, echo=False, connect_args={"check_same_thread": False}
        )
    else:
        conn_str = os.getenv("DATABASE_URL")
        print(f"url postgresql: {conn_str}")
        if conn_str is None:
            raise ValueError("DATABASE_URL")
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


# sessão para a conexão ao banco de dados
def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine()  # para sqlite create_engine(sqlite=True)

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_table() -> None:
    global __engine

    if not __engine:
        create_engine()

    import data.models.__all_models # pyright: ignore
    ModelBase.metadata.create_all(__engine)
