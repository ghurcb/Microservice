from __future__ import annotations
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.session import AsyncSessionLocal

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db = AsyncSessionLocal()
    try:
        yield db # Передаем сессию в handler
    finally:
        await db.close() # Закрываем после использования
