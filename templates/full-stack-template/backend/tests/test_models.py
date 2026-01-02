"""Test database models."""
import pytest
from sqlalchemy import select

from src.db.models import Asset, Tenant, User


@pytest.mark.asyncio
async def test_create_tenant(session):
    """Test creating a tenant."""
    tenant = Tenant(name="Test Org", slug="test-org")
    session.add(tenant)
    await session.commit()

    result = await session.execute(select(Tenant).where(Tenant.slug == "test-org"))
    db_tenant = result.scalar_one()

    assert db_tenant.name == "Test Org"
    assert db_tenant.slug == "test-org"
    assert db_tenant.is_active is True
    assert db_tenant.uuid is not None


@pytest.mark.asyncio
async def test_create_user(session):
    """Test creating a user with tenant relationship."""
    # Create tenant first
    tenant = Tenant(name="Test Org", slug="test-org")
    session.add(tenant)
    await session.flush()

    # Create user
    user = User(
        tenant_uuid=tenant.uuid,
        email="test@example.com",
        full_name="Test User",
    )
    session.add(user)
    await session.commit()

    # Verify
    result = await session.execute(select(User).where(User.email == "test@example.com"))
    db_user = result.scalar_one()

    assert db_user.full_name == "Test User"
    assert db_user.tenant_uuid == tenant.uuid
    assert db_user.is_active is True


@pytest.mark.asyncio
async def test_create_asset(session):
    """Test creating an asset."""
    # Create tenant
    tenant = Tenant(name="Test Org", slug="test-org")
    session.add(tenant)
    await session.flush()

    # Create asset
    asset = Asset(
        tenant_uuid=tenant.uuid,
        name="Test Asset",
        type="equipment",
        description="A test asset",
    )
    session.add(asset)
    await session.commit()

    # Verify
    result = await session.execute(select(Asset).where(Asset.name == "Test Asset"))
    db_asset = result.scalar_one()

    assert db_asset.name == "Test Asset"
    assert db_asset.type == "equipment"
    assert db_asset.description == "A test asset"
