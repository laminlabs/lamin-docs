# Security

```{important}

<img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/jo0O8ip85njL4wYj0000.png" width=100 style="background: transparent; margin-right: 5em;" align="right">

Please see our [Trust Center](https://trust.lamin.ai) for the [SOC 2 report](https://trust.lamin.ai/compliance), [security policies](https://trust.lamin.ai/resources), controls & subprocessors.

We're SOC2 certified and monitor compliance with HIPAA and ISO 27001.

See our [status page](https://status.lamin.ai) for service health and availability.

```

## Data exposure

### Free plan

The open-source LaminDB is fully contained in your infrastructure. No data reaches Lamin's services.

### Pro plan

All your data is hosted by Lamin services.

### Team plan

As on the Pro plan, you can use Lamin's hosted databases and storage locations. On the Team plan, you can also use a self-hosted LaminDB instance so that both your Postgres databases and storage locations remain in your infrastructure. The LaminHub web application remains hosted by Lamin.

To connect your on-prem Postgres database, you configure network access and allowlist the LaminHub backend's IP address at your network or VPN firewall ({doc}`service-endpoints`). LaminHub then sends queries to Postgres and processes the returned metadata on its servers to display it in the LaminHub UI. Providing LaminHub access to your on-prem storage locations is optional and controlled separately from the Postgres connection. You can grant access to AWS S3 through `AssumeRole` or to Google Cloud Storage through service account impersonation.

```{mermaid}
flowchart TB
    browser["Browser"]

    hub["LaminHub"]:::focal

    subgraph customer["Customer infrastructure"]
        db[("Postgres<br/>Metadata")]
        s3[("AWS S3<br/>Data")]
        gcs[("Google Cloud Storage<br/>Data")]
        gcs[("Local Storage<br/>Data")]
    end

    browser <-->|"HTTPS"| hub
    hub -->|"SQL queries<br/>Allowlisted connection"| db
    db -->|"Metadata results<br/>Allowlisted connection"| hub
    hub <-.->|"Optional storage access<br/>AssumeRole"| s3
    hub <-.->|"Optional storage access<br/>Service account impersonation"| gcs
```

Solid arrows show the connection used to browse metadata. Dashed arrows show optional file-storage access. Without storage access, you can still browse, search and query metadata, inspect annotations and explore lineage. Storage previews are unavailable for storage locations LaminHub cannot access. See {doc}`permissions` for access management.

### Enterprise plan

You're running a full on-prem deployment of LaminHub, meaning all your data stays in your infrastructure even during transit.

## Security at Lamin

### Application security

AppSec is the practice of building software that is secure by design, secured during development, secured with testing and review, and deployed securely.

We build our software on distributed infrastructure in which client data is decoupled across databases, storage locations, data centers and networks. LaminHub's data backends are deployed in a fully automated way in the distributed networks & data centers that host databases.

We have automated monitoring test applications that continuously check for networks & errors using observability providers: Sentry, AWS Inspector, Sprinto, Supabase & Cloudflare.

We use HTTPS for secure connections. We force HTTPS for all services using TLS (SSL), including our public website and the Dashboard to ensure secure connections.

All data in Lamin-managed deployments is encrypted in transit and at rest.

Internal code reviews are performed using a modern, PR-based development workflow on Github. Production deployments are gated on successful reviews and isolated test suites running in local environments for unit tests and staging environments for integration tests.

### Corporate security

CorpSec is the practice of making sure Lamin employees have secure access to Lamin company infrastructure, and also that exposed channels to Lamin are secured. CorpSec controls are the primary concern of standards such as SOC2.

Access to our services and applications that connect to customer data is gated on a SSO Identity Provider (IdP) with the exception of GitHub, where our employees are allowed to maintain accounts linked to their IdP of choice.

We mandate phishing-resistant multi-factor authentication (MFA) in all enrolled services.

We regularly audit access to internal systems.

### Bug bounty program

Keeping user data secure is a top priority at Lamin. We welcome contributions from the security community to identify vulnerabilities in LaminHub and disclose them to us in a responsible manner. We offer rewards ranging from $100 to $1000+ depending on the severity of the issue discovered. To participate, please send a report of the vulnerability to `security@lamin.ai`.

Please note that reports for the open-source packages, in particular, LaminDB, almost never qualify for a bounty; you're welcome to make a pull request on the public repository.

Also, some Lamin resources are intentionally public. Reports that rely only on the following expected behavior are out of scope for bounty review:

- public LaminDB instances allowing anonymous or unauthenticated read-only access
- public instance metadata, public profile metadata, and public read-only database connection details for public instances
- public S3 buckets or object listings that back public instances, public assets, examples, or documentation
- public keys like anonymous API keys
- client-side configuration files that expose publishable values, including Supabase anonymous API keys
- enumeration of data that is already available through public Lamin pages, public APIs, public instances, public buckets, or public repositories

### Data privacy

Lamin does not use your source code or data for its own purposes. Access for customer-requested support is limited to designated platform administrators. Lamin staff do not use customer data with consumer AI applications or unapproved browser extensions.

## Frequently asked questions

### Is SSO included, and can we use Microsoft Entra ID?

SSO is included in Team and Enterprise plans and configured during onboarding. Microsoft Entra ID (Azure) sign-in is also supported through OAuth, separately from organization SSO. Users do not need a separate Lamin password; password and MFA policies are managed by the identity provider.

### Which logs can we review and export?

Database writes, permission changes, REST requests, MCP tool calls, and configured S3 activity are covered. Views beyond database writes are currently in **Preview**. See {doc}`audit-logs` for coverage, access, and exports.

### Can we control access for AI agents?

Bot accounts let you limit an agent's access to specific databases and spaces. You control which AI tools your users and agents use. See {doc}`permissions`.

### How are backups and recovery handled?

Lamin-managed AWS PostgreSQL deployments use automated backups. Retention and recovery arrangements depend on the deployment. For infrastructure you operate, your team manages backups and recovery. Our [security policies](https://trust.lamin.ai/resources) cover business continuity and disaster recovery.

### Do you provide an uptime SLA?

Uptime and support commitments are defined in your customer agreement. See our [status page](https://status.lamin.ai) for service health and availability.

For security questionnaires or deployment reviews, contact [security@lamin.ai](mailto:security@lamin.ai).
