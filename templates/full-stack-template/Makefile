.PHONY: help init dev backend frontend db migrate test clean

help:
	@echo "Full Stack Template - Available Commands"
	@echo ""
	@echo "  make init      - Initialize project (copy env files, install deps)"
	@echo "  make dev       - Start all services (postgres, backend, frontend)"
	@echo "  make backend   - Start backend only"
	@echo "  make frontend  - Start frontend only"
	@echo "  make db        - Start database only"
	@echo "  make migrate   - Run database migrations"
	@echo "  make test      - Run all tests"
	@echo "  make clean     - Stop all services and clean volumes"
	@echo ""

init:
	@echo "📦 Initializing project..."
	@if [ ! -f backend/.env ]; then cp backend/.env.example backend/.env; fi
	@if [ ! -f frontend/.env.local ]; then cp frontend/.env.example frontend/.env.local; fi
	@echo "✅ Environment files created"
	@cd backend && pip install -e .[dev]
	@cd frontend && npm install
	@echo "✅ Dependencies installed"

dev:
	@echo "🚀 Starting all services..."
	docker-compose up

backend:
	@echo "🐍 Starting backend..."
	@lsof -ti:8000 | xargs kill -9 2>/dev/null || true
	cd backend && uvicorn src.api.app:app --reload

frontend:
	@echo "⚛️  Starting frontend..."
	@lsof -ti:3000 | xargs kill -9 2>/dev/null || true
	cd frontend && npm run dev

db:
	@echo "🐘 Starting database..."
	docker-compose up -d postgres

migrate:
	@echo "🔄 Running migrations..."
	cd backend && alembic upgrade head

test:
	@echo "🧪 Running tests..."
	cd backend && pytest
	cd frontend && npm test

clean:
	@echo "🧹 Cleaning up..."
	docker-compose down -v
	@echo "✅ All services stopped and volumes removed"
