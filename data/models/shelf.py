import sqlalchemy as sa

from data.models.model_base import ModelBase


class Shef(ModelBase):
    __tablename__: str = "shelves"

    id: sa.Column[int] = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: sa.Column[str] = sa.Column(sa.String(5), nullable=False)
