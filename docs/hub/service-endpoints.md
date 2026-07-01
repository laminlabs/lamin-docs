# Service Endpoints and Client Connectivity

This document covers two different connectivity scenarios:

1. Allowing Lamin-managed services to reach a customer-managed PostgreSQL server.
2. Allowing end-user devices to reach a Lamin-hosted instance.

## Browser and API access

The Lamin web application, authentication flows, and control-plane API traffic use HTTPS on port `443`.

The primary control-plane endpoint used by the LaminDB client is `https://hub.lamin.ai`.

Our services are available in the following regions with the respective API URLs:

### US East (N. Virginia) - `us-east-1`

- **API URL:** `https://us-east-1.api.lamin.ai`
- **IPs:**
  - `100.28.137.170`
  - `54.159.231.46`
  - `100.28.144.231`

### US West (N. California) - `us-west-2`

- **API URL:** `https://us-west-2.api.lamin.ai`
- **IPs:**
  - `44.229.134.201`
  - `52.34.14.66`
  - `54.191.49.248`

### EU Central (Frankfurt) - `eu-central-1`

- **API URL:** `https://eu-central-1.api.lamin.ai`
- **IPs:**
  - `3.73.231.249`
  - `35.156.185.72`
  - `52.29.229.104`

These IPs are relevant when a customer wants to allow Lamin-managed backend services to reach a customer-managed PostgreSQL server.

## Direct PostgreSQL access for LaminDB clients

When a user runs `lamin connect account/name` from Python, R, or the CLI against a hosted PostgreSQL-backed instance, the client does two things:

1. It authenticates with Lamin Hub over HTTPS.
2. It then opens a direct PostgreSQL connection to the instance database.

This direct database connection is required because LaminDB reads and writes metadata directly against the instance database instead of routing all metadata operations through a REST API.

For Supabase-backed instances, the database endpoint can be a host like `aws-0-eu-central-1.pooler.supabase.com` on port `6543`.

### Why port `6543` can be required

Port `6543` is the standard Supabase Supavisor transaction-pooler port. It allows many client sessions to share a smaller number of backend PostgreSQL connections, which is useful for workshops and hackathons where multiple users connect to the same hosted instance.

### Can HTTPS on port `443` be used instead?

Not for the full LaminDB Python or R client workflow on a hosted PostgreSQL-backed instance.

HTTPS on port `443` is still required for:

- authentication
- the web application
- retrieving instance settings and other control-plane operations

However, once a user connects to a hosted PostgreSQL-backed LaminDB instance, the client still needs PostgreSQL connectivity to the instance database endpoint.

### Artifact storage access

If participants download or upload artifacts through the LaminDB client, they can also need access to the cloud object storage endpoint backing the instance, for example an S3 bucket endpoint. This depends on the storage configuration of the instance.

### Which networks and devices should be allowed?

From Lamin's perspective, the required traffic is outbound, client-initiated, and TLS-protected from the participant device to Lamin-managed services. No inbound opening to participant devices is required.

Allow access from whichever networks and devices the event organizer approves for participation, for example:

- internal network
- VPN
- guest Wi-Fi
- institution-managed laptops
- participant-owned laptops

Technically, both managed and personal devices can work. The important requirement is that approved participant devices can reach:

- HTTPS endpoints on port `443`
- the PostgreSQL endpoint for the hosted instance, if participants are using the LaminDB client
