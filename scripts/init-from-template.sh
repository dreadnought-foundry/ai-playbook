#!/bin/bash
# Initialize a new project from the full-stack template
# Usage: ./scripts/init-from-template.sh project-name "Project Display Name"

set -e

# Colors for output
GREEN='\033[0.32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLAYBOOK_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$PLAYBOOK_DIR/templates/full-stack-template"

# Check arguments
if [ -z "$1" ]; then
    echo "Usage: ./scripts/init-from-template.sh <project-name> [\"Project Display Name\"]"
    echo "Example: ./scripts/init-from-template.sh my-app \"My Awesome App\""
    exit 1
fi

PROJECT_SLUG="$1"
PROJECT_NAME="${2:-$1}"
TARGET_DIR="$(pwd)/$PROJECT_SLUG"

# Validate project slug
if [[ ! "$PROJECT_SLUG" =~ ^[a-z0-9-]+$ ]]; then
    echo "Error: Project name must be lowercase alphanumeric with hyphens only"
    echo "Example: my-project"
    exit 1
fi

# Check if template exists
if [ ! -d "$TEMPLATE_DIR" ]; then
    echo "Error: Template not found at $TEMPLATE_DIR"
    exit 1
fi

# Check if target directory already exists
if [ -d "$TARGET_DIR" ]; then
    echo "Error: Directory $TARGET_DIR already exists"
    exit 1
fi

echo -e "${BLUE}📦 Initializing new project: $PROJECT_NAME${NC}"
echo -e "${BLUE}📍 Location: $TARGET_DIR${NC}"
echo ""

# Copy template
echo -e "${GREEN}1. Copying template...${NC}"
cp -r "$TEMPLATE_DIR" "$TARGET_DIR"
cd "$TARGET_DIR"

# Remove git history from template
if [ -d ".git" ]; then
    rm -rf .git
fi

# Customize project files
echo -e "${GREEN}2. Customizing project files...${NC}"

# Update backend/pyproject.toml
sed -i '' "s/name = \"app-backend\"/name = \"$PROJECT_SLUG-backend\"/" backend/pyproject.toml
sed -i '' "s/description = \".*\"/description = \"$PROJECT_NAME backend\"/" backend/pyproject.toml

# Update frontend/package.json
sed -i '' "s/\"name\": \"app-frontend\"/\"name\": \"$PROJECT_SLUG-frontend\"/" frontend/package.json
sed -i '' "s/\"description\": \".*\"/\"description\": \"$PROJECT_NAME frontend\"/" frontend/package.json

# Update docker-compose.yml container names
sed -i '' "s/container_name: app-/container_name: $PROJECT_SLUG-/" docker-compose.yml
sed -i '' "s/POSTGRES_DB: app/POSTGRES_DB: $PROJECT_SLUG/" docker-compose.yml

# Update README.md
sed -i '' "s/# Full Stack Template/# $PROJECT_NAME/" README.md
sed -i '' "1a\\
\\
$PROJECT_NAME - Brief description here.\\
" README.md

# Update CLAUDE.md
sed -i '' "s/Full Stack App/$PROJECT_NAME/" CLAUDE.md

# Create .env files from examples
echo -e "${GREEN}3. Creating environment files...${NC}"
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local

# Update database URLs in .env
sed -i '' "s/app/$PROJECT_SLUG/g" backend/.env

# Initialize git
echo -e "${GREEN}4. Initializing git repository...${NC}"
git init
git add .
git commit -m "Initial commit - project scaffolding

Created from ai-playbook full-stack template

🤖 Generated with Claude Code
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

# Create initial directory structure for sprints
echo -e "${GREEN}5. Setting up sprint workflow...${NC}"
mkdir -p docs/sprints/{0-backlog,1-todo,2-in-progress,3-done,4-blocked,5-abandoned,6-archived}
mkdir -p docs/epics

# Copy sprint template
cp "$PLAYBOOK_DIR/templates/sprint-template.md" docs/sprints/

# Create registry.json
cat > docs/sprints/registry.json <<EOF
{
  "version": "1.0",
  "nextSprintNumber": 1,
  "nextEpicNumber": 1,
  "sprints": {},
  "epics": {}
}
EOF

# Create initial epic (Epic 0: Foundation)
cat > docs/epics/epic-00_foundation.md <<EOF
---
epic: 0
title: "Foundation"
status: in-progress
created: $(date +%Y-%m-%d)
---

# Epic 0: Foundation

## Overview

Bootstrap project with working backend, frontend, and development environment.

## Goal

Establish foundational patterns and get a working full-stack application running locally.

## Sprints

| Sprint | Title | Status |
|--------|-------|--------|
| - | Bootstrap complete (via template) | done |

## Success Criteria

- [ ] Backend running and accessible
- [ ] Frontend running and displaying data
- [ ] Database migrations working
- [ ] GraphQL queries functional
- [ ] Tests passing
- [ ] Docker Compose configured

## Notes

Created from ai-playbook template. Follow [project-bootstrap-guide.md](../../ai-playbook/playbooks/project-bootstrap-guide.md) for next steps.
EOF

# Install pre-commit hooks (if pre-commit is available)
if command -v pre-commit &> /dev/null; then
    echo -e "${GREEN}6. Installing pre-commit hooks...${NC}"
    pre-commit install
    pre-commit install --hook-type commit-msg
else
    echo -e "${YELLOW}⚠️  pre-commit not found. Install with: pip install pre-commit${NC}"
    echo -e "${YELLOW}   Then run: cd $TARGET_DIR && pre-commit install${NC}"
fi

# Print success message
echo ""
echo -e "${GREEN}✅ Project initialized successfully!${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo ""
echo -e "  1. ${GREEN}cd $PROJECT_SLUG${NC}"
echo -e "  2. ${GREEN}make init${NC}        # Install dependencies"
echo -e "  3. ${GREEN}make db${NC}          # Start database"
echo -e "  4. ${GREEN}make migrate${NC}     # Run migrations"
echo -e "  5. ${GREEN}make dev${NC}         # Start everything"
echo ""
echo -e "  Then visit:"
echo -e "  - Frontend: ${BLUE}http://localhost:3000${NC}"
echo -e "  - Backend:  ${BLUE}http://localhost:8000${NC}"
echo -e "  - GraphQL:  ${BLUE}http://localhost:8000/graphql${NC}"
echo ""
echo -e "${YELLOW}📚 Documentation:${NC}"
echo -e "  - Quick start:  README.md"
echo -e "  - Tech stack:   STACK.md"
echo -e "  - AI dev:       CLAUDE.md"
echo -e "  - Bootstrap:    ai-playbook/playbooks/project-bootstrap-guide.md"
echo ""
echo -e "${GREEN}Happy building! 🚀${NC}"
