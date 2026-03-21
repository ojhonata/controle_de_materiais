import sqlalchemy as sa
from sqlalchemy import orm

from data.models.model_base import ModelBase


class Shelf(ModelBase):
    __tablename__: str = "shelves"

    id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    name: orm.Mapped[str] = orm.mapped_column(sa.String(5), nullable=False)
