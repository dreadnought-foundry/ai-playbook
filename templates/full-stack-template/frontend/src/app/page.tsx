import Link from "next/link";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-center font-mono text-sm">
        <Card className="max-w-2xl mx-auto">
          <CardHeader>
            <CardTitle className="text-3xl">Full Stack Template</CardTitle>
            <CardDescription>
              FastAPI + GraphQL + Next.js + shadcn/ui
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <p className="text-muted-foreground">
              This template includes:
            </p>
            <ul className="list-disc list-inside space-y-2 text-sm text-muted-foreground">
              <li>Python backend with FastAPI and Strawberry GraphQL</li>
              <li>PostgreSQL with SQLAlchemy 2.0 async ORM</li>
              <li>Next.js 14 with App Router</li>
              <li>Tailwind CSS and shadcn/ui components</li>
              <li>GraphQL Code Generator for type safety</li>
              <li>Docker Compose for local development</li>
            </ul>
            <div className="flex gap-4 pt-4">
              <Button asChild>
                <Link href="/tenants">View Tenants</Link>
              </Button>
              <Button variant="outline" asChild>
                <a
                  href="http://localhost:8000/graphql"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  GraphQL Playground
                </a>
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
