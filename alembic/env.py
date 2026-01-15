from __future__ import annotations

import os
import sys
from logging.config import fileConfig
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context

# ─────────────────────────────────────────────
# AJUSTE DO PYTHONPATH (OBRIGATÓRIO)
# ─────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

# ─────────────────────────────────────────────
# VARIÁVEIS DE AMBIENTE
# ─────────────────────────────────────────────

if os.getenv("PYTEST_CURRENT_TEST"):
    load_dotenv(".env.test", override=True)
else:
    load_dotenv()

# ─────────────────────────────────────────────
# IMPORTS DO PROJETO (SÓ AGORA)
# ─────────────────────────────────────────────

from infrastructure.db.base import Base  # noqa: E402
from infrastructure.db.models import recibo_models  # noqa: E402  (FORÇA REGISTRO)

target_metadata = Base.metadata

# ─────────────────────────────────────────────
# CONFIG ALEMBIC
# ─────────────────────────────────────────────

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL não configurada")
    return url


# ─────────────────────────────────────────────
# OFFLINE
# ─────────────────────────────────────────────


def run_migrations_offline() -> None:
    context.configure(
        url=get_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ─────────────────────────────────────────────
# ONLINE
# ─────────────────────────────────────────────


def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_database_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# ─────────────────────────────────────────────

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
