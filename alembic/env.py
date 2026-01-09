import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import os

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context
from infrastructure.database import Base  # ajusta el import si cambia

load_dotenv()

config = context.config

config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

target_metadata = Base.metadata
