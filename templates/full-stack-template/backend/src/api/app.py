"""FastAPI application with GraphQL endpoint.

This is the main entry point for the backend API.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from ..config.settings import settings
from ..db.session import get_session
from .graphql.schema import schema


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown events."""
    # Startup
    print(f"🚀 Starting API server on {settings.api_host}:{settings.api_port}")
    print(f"📊 GraphQL endpoint: http://{settings.api_host}:{settings.api_port}/graphql")

    yield

    # Shutdown
    print("👋 Shutting down API server")


# Create FastAPI app
app = FastAPI(
    title="App Backend",
    description="FastAPI + GraphQL backend template",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# GraphQL route with session injection
async def get_context():
    """Provide context for GraphQL resolvers."""
    async for session in get_session():
        return {"session": session}


graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "status": "ok",
        "message": "API is running",
        "graphql": "/graphql",
    }


@app.get("/health")
async def health():
    """Health check for load balancers."""
    return {"status": "healthy"}
