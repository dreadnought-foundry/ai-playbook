"use client";

import { useQuery, gql } from "@apollo/client";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

const GET_TENANTS = gql`
  query GetTenants {
    tenants {
      uuid
      name
      slug
      isActive
      createdAt
    }
  }
`;

interface Tenant {
  uuid: string;
  name: string;
  slug: string;
  isActive: boolean;
  createdAt: string;
}

export default function TenantsPage() {
  const { loading, error, data } = useQuery<{ tenants: Tenant[] }>(GET_TENANTS);

  if (loading) {
    return (
      <main className="flex min-h-screen flex-col items-center p-24">
        <div className="text-center">Loading tenants...</div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="flex min-h-screen flex-col items-center p-24">
        <Card className="max-w-2xl">
          <CardHeader>
            <CardTitle>Error</CardTitle>
            <CardDescription>Failed to load tenants</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{error.message}</p>
            <p className="text-sm text-muted-foreground mt-4">
              Make sure the backend is running at http://localhost:8000
            </p>
          </CardContent>
        </Card>
      </main>
    );
  }

  return (
    <main className="flex min-h-screen flex-col p-24">
      <div className="max-w-5xl mx-auto w-full space-y-6">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-bold">Tenants</h1>
            <p className="text-muted-foreground">
              Manage your organizations
            </p>
          </div>
          <Button asChild variant="outline">
            <Link href="/">← Back</Link>
          </Button>
        </div>

        {data?.tenants.length === 0 ? (
          <Card>
            <CardContent className="pt-6">
              <p className="text-center text-muted-foreground">
                No tenants found. Create your first tenant using the GraphQL API.
              </p>
            </CardContent>
          </Card>
        ) : (
          <div className="grid gap-4">
            {data?.tenants.map((tenant) => (
              <Card key={tenant.uuid}>
                <CardHeader>
                  <CardTitle>{tenant.name}</CardTitle>
                  <CardDescription>
                    {tenant.slug} • Created{" "}
                    {new Date(tenant.createdAt).toLocaleDateString()}
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="flex items-center gap-2">
                    <span
                      className={`inline-block w-2 h-2 rounded-full ${
                        tenant.isActive ? "bg-green-500" : "bg-gray-400"
                      }`}
                    />
                    <span className="text-sm">
                      {tenant.isActive ? "Active" : "Inactive"}
                    </span>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
