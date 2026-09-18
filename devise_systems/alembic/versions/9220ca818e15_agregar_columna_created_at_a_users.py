"""Agregar columna created_at a users

Revision ID: 9220ca818e15
Revises: f09018e4711b
Create Date: 2026-09-17 08:46:41.191774

"""
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "9220ca818e15"
down_revision: Union[str, Sequence[str], None] = "f09018e4711b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Mantiene la revision historica sin cambios de esquema."""
    pass


def downgrade() -> None:
    """Mantiene la revision historica sin cambios de esquema."""
    pass
