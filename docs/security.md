# Security

```{important}

Please see our Trust Center at [trust.lamin.ai](https://trust.lamin.ai) for controls, subprocessors, and certifications. We're currently undergoing our first audits.

```

## Data exposure

### LaminDB

LaminDB is open-source software that operates inside your infrastructure and is subject to your security measures.

Lamin obtains no access to your data when you use LaminDB.

### LaminHub Basic

- Signing up on LaminHub uses an auth flow from an identity provider, storing user handle & email address.
- If you register a LaminDB instance on LaminHub, storage locations (AWS S3 or GCP bucket names) are stored.
- Lamin isn't able to access your data and you won't be able to see your data on LaminHub.

### LaminHub Team & Enterprise

Both on the Team & Enterprise plan, LaminHub provides a layer for AWS that makes access management more secure & intuitive ({doc}`access`):

- Based on an identity provider (Google, GitHub, SSO, OIDC) and a role-based permission system, LaminDB users automatically receive federated access tokens for data on AWS or GCP. These tokens are short-lived and thereby minimize attack surface.
- LaminHub's permission system makes it easy to minimize attack surfaces by implementing the principle of least privilege.

All cloud data in LaminDB instances is hosted in AWS S3 and GCP storage, which are decoupled from VPCs. Metadata is hosted in dedicated Postgres servers with automated access management.

- On the **Team plan**, distributed Postgres server endpoints, by default, are accessible from any IP on the public internet while being protected through vulnerability scans. Access from suspicious IP addresses is immediately black-listed. You can opt to only allow access from specific whitelisted IP addresses.
- On the **Enterprise plan**, Postgres servers can be deployed in your VPC in your AWS account.

## Security at Lamin

### Application security

AppSec is the practice of building software that is secure by design, secured during development, secured with testing and review, and deployed securely.

We build our software on distributed infrastructure in which client data is decoupled across databases, storage locations, data centers and networks. LaminHub's data backends are deployed in a fully automated way in the distributed networks & data centers that host databases. With this, the attack surface of any single customer on the Team & Enterprise plans is equivalent to self-hosted infrastructure on AWS or GCP.

We have automated monitoring test applications that continuously check for networks & errors using observability providers: Sentry, AWS Inspector, Vanta, Supabase & Cloudflare.

We use HTTPS for secure connections. We force HTTPS for all services using TLS (SSL), including our public website and the Dashboard to ensure secure connections.

All user data is encrypted in transit and at rest.

Internal code reviews are performed using a modern, PR-based development workflow on Github. Production deployments are gated successful reviews and isolated test suites running in local environments for unit tests and staging environments for integration tests.

### Corporate security

CorpSec is the practice of making sure Lamin employees have secure access to Lamin company infrastructure, and also that exposed channels to Lamin are secured. CorpSec controls are the primary concern of standards such as SOC2.

Access to our services and applications that connect to customer data is gated on a SSO Identity Provider (IdP) with the exception of GitHub, where our employees are allowed to maintain accounts linked to their IdP of choice.

We mandate phishing-resistant multi-factor authentication (MFA) in all enrolled services.

We regularly audit access to internal systems.

### Bug bounty program

Keeping user data secure is a top priority at Lamin. We welcome contributions from the security community to identify vulnerabilities in our product and disclose them to us in a responsible manner. We offer rewards ranging from $100 to $1000+ depending on the severity of the issue discovered. To participate, please send a report of the vulnerability to security@lamin.ai

### Data privacy

Lamin will never access or use your source code or data.
