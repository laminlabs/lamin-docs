# REST

```{toctree}
:maxdepth: 1
:caption: Hub
:hidden:

hub/authentication
hub/account
hub/instances
hub/permissions
hub/registry-querying
hub/infrastructure
hub/service-endpoints
```

Use the LaminHub REST API to automate Hub workflows from scripts, services, or
tools that do not use the LaminDB Python client.

## Start here

1. Use the API URL for your Lamin region from
   [Service endpoints and client connectivity](service-endpoints.md).
2. Get a token in [Authentication](authentication.md).
3. Pick the page that matches your task below.

## Common flows

- **Query registry entries**: inspect the schema, query generic registries, and
  use dedicated endpoints for Artifacts, Transforms, ULabels, and Records in
  [Registry querying](registry-querying.md).
- **Manage access**: manage organizations, teams, spaces, and instance
  collaborators in [Permissions](permissions.md).
- **Set up backend resources**: register S3 buckets and database servers in
  [Infrastructure](infrastructure.md).
- **Configure networks**: find regional endpoints, allow-listed IPs, and direct
  PostgreSQL connectivity notes in
  [Service endpoints and client connectivity](service-endpoints.md).

## Reference pages

- [Authentication](authentication.md): Lamin JWTs, instance database JWTs, S3
  credentials, and LaminDB access tokens.
- [Account](account.md): authenticated account details, API keys, service
  accounts, and service-account API keys.
- [Instances](instances.md): instance creation, settings, migrations, schemas,
  database JWTs, and statistics.
- [Registry querying](registry-querying.md): generic registry queries and
  dedicated endpoints for common registries.
- [Permissions](permissions.md): organizations, teams, spaces, and instance
  collaborators.
- [Infrastructure](infrastructure.md): S3 bucket registration and database
  servers.
- [Service endpoints and client connectivity](service-endpoints.md): regional
  API endpoints, allow-listed IPs, and direct PostgreSQL connectivity.
