"""Smoke tests for imports and basic functionality.

These tests run quickly and catch import errors before running full test suite.
"""


def test_imports():
    """Test that all main modules can be imported."""
    # Database
    from src.db import Base, User, Asset
    from src.db.session import get_session, engine

    # API
    from src.api.app import app
    from src.api.graphql.schema import schema
    from src.api.graphql.types import User as UserType, Asset as AssetType

    # Config
    from src.config.settings import settings

    assert Base is not None
    assert app is not None
    assert schema is not None
    assert settings is not None


def test_database_models_have_tablename():
    """Ensure all models have __tablename__ defined."""
    from src.db.models import User, Asset

    assert hasattr(User, "__tablename__")
    assert hasattr(Asset, "__tablename__")


def test_graphql_schema_has_query():
    """Ensure GraphQL schema is properly configured."""
    from src.api.graphql.schema import schema

    assert schema.query_type is not None
    assert schema.mutation_type is not None
