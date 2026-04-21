import asyncio
import sys
import os
import logging
from sqlalchemy.ext.asyncio import create_async_engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def wait_for_db():
    """Ждем пока БД будет доступна перед запуском приложения"""
    db_url = os.getenv("ASYNC_DATABASE_URL")
    max_retries = 30
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            engine = create_async_engine(db_url)
            async with engine.begin() as conn:
                await conn.exec_driver_sql("SELECT 1")
            logger.info(f"Database is ready (backend)")
            await engine.dispose()
            return True
        except Exception as e:
            retry_count += 1
            logger.warning(f"Database not ready ({retry_count}/{max_retries}): {e}")
            if retry_count < max_retries:
                await asyncio.sleep(1)
    
    logger.error("Could not connect to database")
    sys.exit(1)


if __name__ == "__main__":
    asyncio.run(wait_for_db())
