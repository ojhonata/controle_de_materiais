import sqlalchemy as sa

from data.models.model_base import ModelBase


class Sector(ModelBase):
    __tablename__: str = "sectors"

    id: sa.Column[int] = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: sa.Column[str] = sa.Column(sa.String(100), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Sector: {self.nome}"
