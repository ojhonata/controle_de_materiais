from datetime import datetime
from typing import Any

import sqlalchemy as sa
from sqlalchemy import ForeignKey, orm

from data.models.model_base import ModelBase
from data.models.sector import Sector
from data.models.type import Type
from data.models.user import User


class Movement(ModelBase):
    __tablename__: str = "movements"

    id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, primary_key=True, server_default=sa.func.gen_random_uuid()
    )

    ordem_number: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)
    date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, server_default=sa.func.now(), index=True
    )

    sector_id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer, ForeignKey("sectors.id")
    )
    sector: orm.Mapped[Sector] = orm.relationship("Sector", lazy="joined")

    type_id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer, ForeignKey("types.id")
    )
    type: orm.Mapped[Type] = orm.relationship("Type", lazy="joined")

    user_id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, ForeignKey("users.id")
    )
    user: orm.Mapped[User] = orm.relationship("User", lazy="joined")
