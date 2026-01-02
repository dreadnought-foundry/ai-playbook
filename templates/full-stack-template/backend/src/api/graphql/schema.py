"""GraphQL schema with queries and mutations.

Demonstrates:
- Async resolvers
- Database session from context
- Type conversion (SQLAlchemy model → GraphQL type)
- Input validation
"""
import strawberry
from uuid import UUID
from sqlalchemy import select

from .types import Asset, CreateAssetInput, Tenant, User
from ...db import models


@strawberry.type
class Query:
    """GraphQL queries."""

    @strawberry.field
    async def tenants(self, info: strawberry.Info) -> list[Tenant]:
        """Get all tenants."""
        session = info.context["session"]
        result = await session.execute(select(models.Tenant))
        db_tenants = result.scalars().all()
        return [
            Tenant(
                uuid=t.uuid,
                name=t.name,
                slug=t.slug,
                is_active=t.is_active,
                created_at=t.created_at,
                updated_at=t.updated_at,
            )
            for t in db_tenants
        ]

    @strawberry.field
    async def tenant(self, info: strawberry.Info, uuid: UUID) -> Tenant | None:
        """Get a tenant by UUID."""
        session = info.context["session"]
        result = await session.execute(
            select(models.Tenant).where(models.Tenant.uuid == uuid)
        )
        db_tenant = result.scalar_one_or_none()
        if not db_tenant:
            return None

        return Tenant(
            uuid=db_tenant.uuid,
            name=db_tenant.name,
            slug=db_tenant.slug,
            is_active=db_tenant.is_active,
            created_at=db_tenant.created_at,
            updated_at=db_tenant.updated_at,
        )

    @strawberry.field
    async def assets(
        self,
        info: strawberry.Info,
        tenant_uuid: UUID | None = None
    ) -> list[Asset]:
        """Get assets, optionally filtered by tenant."""
        session = info.context["session"]
        stmt = select(models.Asset)

        if tenant_uuid:
            stmt = stmt.where(models.Asset.tenant_uuid == tenant_uuid)

        result = await session.execute(stmt)
        db_assets = result.scalars().all()

        return [
            Asset(
                uuid=a.uuid,
                tenant_uuid=a.tenant_uuid,
                name=a.name,
                type=a.type,
                description=a.description,
                created_at=a.created_at,
                updated_at=a.updated_at,
            )
            for a in db_assets
        ]


@strawberry.type
class Mutation:
    """GraphQL mutations."""

    @strawberry.mutation
    async def create_asset(
        self,
        info: strawberry.Info,
        input: CreateAssetInput
    ) -> Asset:
        """Create a new asset."""
        session = info.context["session"]

        # Create SQLAlchemy model instance
        db_asset = models.Asset(
            tenant_uuid=input.tenant_uuid,
            name=input.name,
            type=input.type,
            description=input.description,
        )

        session.add(db_asset)
        await session.flush()
        await session.refresh(db_asset)

        # Convert to GraphQL type
        return Asset(
            uuid=db_asset.uuid,
            tenant_uuid=db_asset.tenant_uuid,
            name=db_asset.name,
            type=db_asset.type,
            description=db_asset.description,
            created_at=db_asset.created_at,
            updated_at=db_asset.updated_at,
        )


# Create schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
