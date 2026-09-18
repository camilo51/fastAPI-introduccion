"""agregar_fecha_de_creacion_a_usuarios

Revision ID: 4c07a69ca0d1
Revises: 1d048545d1b2
Create Date: 2026-09-17 20:17:51.071210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c07a69ca0d1'
down_revision: Union[str, Sequence[str], None] = '1d048545d1b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # SQLite requiere recrear la tabla para agregar una columna obligatoria
    # con el valor predeterminado CURRENT_TIMESTAMP.
    with op.batch_alter_table("users", recreate="always") as batch_op:
        batch_op.add_column(
            sa.Column(
                "created_at",
                sa.DateTime(timezone=True),
                server_default=sa.text("CURRENT_TIMESTAMP"),
                nullable=False,
            )
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("users", recreate="always") as batch_op:
        batch_op.drop_column("created_at")
