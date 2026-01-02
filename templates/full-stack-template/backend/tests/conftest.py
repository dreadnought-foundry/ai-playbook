"""Pytest configuration and fixtures."""
import pytest
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.db.base import Base


@pytest.fixture(scope="session")
async def engine():
    """Create test database engine."""
    test_engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost:5432/app_test",
        echo=False,
    )

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield test_engine

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await test_engine.dispose()


@pytest.fixture
async def session(engine) -> AsyncGenerator[AsyncSession, None]:
    """Create test database session."""
    async_session = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session
        await session.rollback()
