# Frontend - Next.js + shadcn/ui

Next.js 14 frontend with TypeScript, Tailwind CSS, and shadcn/ui components.

## Quick Start

```bash
# Install dependencies
npm install

# Copy environment file
cp .env.example .env.local

# Start development server
npm run dev
```

The app will be available at http://localhost:3000

## Project Structure

```
frontend/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── layout.tsx         # Root layout
│   │   ├── page.tsx           # Home page
│   │   └── tenants/           # Tenants page
│   ├── components/
│   │   └── ui/                # shadcn/ui components
│   ├── lib/
│   │   ├── apollo-wrapper.tsx # Apollo Client setup
│   │   └── utils.ts           # Utility functions
│   └── types/
│       └── graphql.ts         # Generated GraphQL types
├── package.json
├── tailwind.config.ts         # Tailwind configuration
├── components.json            # shadcn/ui configuration
└── codegen.yml               # GraphQL codegen config
```

## Key Features

### GraphQL Type Safety

This template uses GraphQL Code Generator to create TypeScript types from your GraphQL schema:

```bash
# Generate types from backend schema
npm run codegen
```

This creates `src/types/graphql.ts` with fully typed queries and mutations.

### shadcn/ui Components

Add new components using the CLI:

```bash
npx shadcn-ui@latest add [component-name]
```

Examples:
```bash
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add table
```

See all components: https://ui.shadcn.com/docs/components

### Apollo Client

GraphQL queries use Apollo Client:

```tsx
"use client";

import { useQuery, gql } from "@apollo/client";

const GET_ITEMS = gql`
  query GetItems {
    items {
      id
      name
    }
  }
`;

export default function MyPage() {
  const { loading, error, data } = useQuery(GET_ITEMS);
  // ...
}
```

## Common Tasks

### Add a New Page

1. Create `src/app/my-page/page.tsx`
2. Export default component
3. Link from navigation: `<Link href="/my-page">My Page</Link>`

### Add a GraphQL Query

1. Create query in component or `.graphql` file
2. Run `npm run codegen` to generate types
3. Use typed hooks: `useMyQueryQuery()`

### Add shadcn/ui Component

```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
```

Components are added to `src/components/ui/`.

### Style with Tailwind

Use Tailwind utility classes:

```tsx
<div className="flex items-center gap-4 p-6 bg-card rounded-lg">
  <h1 className="text-2xl font-bold">Title</h1>
</div>
```

Customize colors in `tailwind.config.ts`.

## Environment Variables

- `NEXT_PUBLIC_GRAPHQL_URL` - Backend GraphQL endpoint (default: http://localhost:8000/graphql)

## Building for Production

```bash
# Build
npm run build

# Start production server
npm start
```

## Tech Stack

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS
- **shadcn/ui** - Beautiful, accessible components
- **Apollo Client** - GraphQL client
- **GraphQL Code Generator** - Type generation
