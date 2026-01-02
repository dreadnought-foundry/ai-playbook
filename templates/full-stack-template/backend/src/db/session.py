"""Database session management using SQLAlchemy 2.0 async pattern."""
from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from ..config.settings import settings

# Create async engine
engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    future=True,
)

# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database sessions.

    Usage in FastAPI:
        async def my_endpoint(session: AsyncSession = Depends(get_session)):
            ...

    Usage in GraphQL:
        @strawberry.field
        async def users(self, info: Info) -> list[User]:
            session = info.context["session"]
            ...
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
