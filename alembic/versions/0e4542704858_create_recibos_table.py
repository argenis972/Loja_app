"""create recibos table

Revision ID: 0e4542704858
Revises: None
Create Date: 2026-01-10 19:03:18.335800
"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0e4542704858"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "recibos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("total", sa.Float(), nullable=False),
        sa.Column("metodo", sa.String(length=50), nullable=False),
        sa.Column("parcelas", sa.Integer(), nullable=False),
        sa.Column("informacoes_adicionais", sa.String(), nullable=True),
        sa.Column("valor_parcela", sa.Float(), nullable=False),
        #  O BANCO CUIDA DA DATA
        sa.Column(
            "data_hora", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
    )


def downgrade() -> None:
    op.drop_index("ix_recibos_id", table_name="recibos")
    op.drop_table("recibos")
