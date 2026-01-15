from __future__ import annotations

import os
import sys
from logging.config import fileConfig
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context

# Ajuste correto do PYTHONPATH (obrigatório no Windows + pytest + alembic)


BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

#  Carrega variáveis de ambiente

# Prioridade para testes
if os.getenv("PYTEST_CURRENT_TEST"):
    load_dotenv(".env.test", override=True)
else:
    load_dotenv()

# Imports do projeto (agora funcionam)

from infrastructure.database import Base  # noqa: E402

# Configuração Alembic

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL não configurada")
    return database_url


# Modo OFFLINE


def run_migrations_offline() -> None:
    config.get_main_option("sqlalchemy.url")
    context.configure()
