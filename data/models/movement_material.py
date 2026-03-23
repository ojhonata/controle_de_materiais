from typing import Any

import sqlalchemy as sa
from sqlalchemy import orm

from data.models.material import Material
from data.models.model_base import ModelBase
from data.models.movement import Movement


class MovementMaterial(ModelBase):
    __tablename__: str = "movements_materials"

    id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, primary_key=True, server_default=sa.func.gen_random_uuid()
    )
    quantity: orm.Mapped[int] = orm.mapped_column(sa.Integer, nullable=False)

    movement_id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, sa.ForeignKey("movements.id"), nullable=False
    )
    movement: orm.Mapped[Movement] = orm.relationship("Movement", lazy="joined")

    material_id: orm.Mapped[sa.UUID[Any]] = orm.mapped_column(
        sa.UUID, sa.ForeignKey("materials.id"), nullable=False
    )
    material: orm.Mapped[Material] = orm.relationship("Material", lazy="joined")
