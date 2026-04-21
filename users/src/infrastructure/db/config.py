from __future__ import annotations
import os


def get_database_url() -> str:
    url = os.getenv("ASYNC_DATABASE_URL")
    if not url:
        raise RuntimeError(
            "ASYNC_DATABASE_URL must be set. "
            "Format: postgresql+asyncpg://user:password@host:port/dbname"
        )
    return url
