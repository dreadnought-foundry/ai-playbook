"""GraphQL types using Strawberry.

Types are separated from SQLAlchemy models to:
1. Control what's exposed to the frontend
2. Add computed fields
3. Handle GraphQL-specific logic
"""
import strawberry
from uuid import UUID
from datetime import datetime


@strawberry.type
class Tenant:
    """GraphQL type for Tenant."""
    uuid: UUID
    name: str
    slug: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


@strawberry.type
class User:
    """GraphQL type for User."""
    uuid: UUID
    tenant_uuid: UUID
    email: str
    full_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


@strawberry.type
class Asset:
    """GraphQL type for Asset."""
    uuid: UUID
    tenant_uuid: UUID
    name: str
    type: str
    description: str | None
    created_at: datetime
    updated_at: datetime


@strawberry.input
class CreateAssetInput:
    """Input for creating an asset."""
    tenant_uuid: UUID
    name: str
    type: str
    description: str | None = None
