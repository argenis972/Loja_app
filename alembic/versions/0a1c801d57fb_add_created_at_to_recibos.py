import sqlalchemy as sa

from alembic import op

revision = "XXXXXXXX"
down_revision = "YYYYYYYY"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "recibos",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )


def downgrade():
    op.drop_column("recibos", "created_at")
