from datetime import datetime
from typing import Any

import sqlalchemy as sa
from sqlalchemy import orm

from data.models.model_base import ModelBase
from data.models.user import User


class InventoryCount(ModelBase):
    __tablename__: str = "inventory_count"

    id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, primary_key=True, server_default=sa.func.gen_random_uuid()
    )
    date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, server_default=sa.func.now(), index=True
    )

    user_id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, sa.ForeignKey("users.id")
    )

    user: orm.Mapped[User] = orm.relationship("User", lazy="joined")
