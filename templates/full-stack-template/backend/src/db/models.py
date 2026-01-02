"""Sample database models.

This file demonstrates the opinionated patterns:
- UUID primary keys
- Timestamp tracking (created_at, updated_at)
- SQLAlchemy 2.0 style (Mapped, mapped_column)
- Type hints on all columns
"""
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, TimestampMixin, UUIDMixin


class Tenant(Base, UUIDMixin, TimestampMixin):
    """Multi-tenant organization model.

    Each tenant represents a separate customer/organization with isolated data.
    """
    __tablename__ = "tenants"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    # Relationships
    users: Mapped[list["User"]] = relationship(back_populates="tenant", lazy="selectin")
    assets: Mapped[list["Asset"]] = relationship(back_populates="tenant", lazy="selectin")


class User(Base, UUIDMixin, TimestampMixin):
    """User model with tenant relationship.

    Users belong to a single tenant. For multi-tenant access, use a join table.
    """
    __tablename__ = "users"

    tenant_uuid: Mapped[UUID] = mapped_column(ForeignKey("tenants.uuid"), nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    # Relationships
    tenant: Mapped["Tenant"] = relationship(back_populates="users", lazy="selectin")


class Asset(Base, UUIDMixin, TimestampMixin):
    """Generic asset model.

    Demonstrates:
    - Tenant isolation (all assets belong to a tenant)
    - Flexible type field (customize for your domain)
    - Optional fields (description, location can be None)
    """
    __tablename__ = "assets"

    tenant_uuid: Mapped[UUID] = mapped_column(ForeignKey("tenants.uuid"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Optional: Add PostGIS geometry column
    # location: Mapped[str | None] = mapped_column(Geometry("POINT", srid=4326), nullable=True)

    # Relationships
    tenant: Mapped["Tenant"] = relationship(back_populates="assets", lazy="selectin")
