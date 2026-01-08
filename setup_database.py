"""
Database setup script for Loja App.

This script creates the database tables for the Loja App.
Run this script before starting the application if using PostgreSQL.

For SQLite (default), tables are created automatically on app startup.
"""

import os
import sys

from infrastructure.database import create_tables


def setup_database():
    """Create all database tables."""
    database_url = os.getenv("DATABASE_URL", "sqlite:///./receipts/recibos.db")

    print(f"Setting up database at: {database_url}")
    print("Creating tables...")

    try:
        create_tables()
        print("✓ Tables created successfully!")
        print("\nTables:")
        print(
            "  - recibos (id, total, metodo, parcelas, "
            "informacoes_adicionais, created_at)"
        )

        return 0
    except Exception as e:
        print(f"✗ Error creating tables: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(setup_database())
