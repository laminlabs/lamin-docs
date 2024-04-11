# Security

## Data exposure

### LaminDB

LaminDB is open-source software that operates inside your infrastructure and is subject to your security measures.

Lamin obtains no access to your data when you use LaminDB.

### LaminHub

#### Basic

- Signing up on LaminHub only stores & uses an auth flow from an identity provider, storing user name & email address.
- If you register a LaminDB instance on LaminHub, storage locations (AWS S3 or GCP bucket names) are stored.
- Lamin isn't able to access your data and you won't be able to see your data in LaminHub.

#### Enterprise

LaminHub provides a layer for AWS & GCP that makes access management more secure & intuitive.

- Based on an identity provider (Google, GitHub, SSO, OIDC) and a role-based permission system, LaminDB users automatically receive federated access tokens for data on AWS or GCP. These tokens are short-lived and thereby minimize attack surface.
- LaminHub's permission system makes it easy to minimize attack surfaces by implementing the principle of least privilege.

Beyond access through short-lived tokens, data is secured by AWS & GCP.

## Security at Lamin

### Application security (AppSec)

AppSec is the practice of building software that is secure by design, secured during development, secured with testing and review, and deployed securely.

We build our software on distributed infrastructure in which client data is decoupled across databases, storage locations, data centers and networks. LaminHub's backend is deployed in a fully automated way in the networks & data centers that host databases.

With this, the attack surface of any single customer on the Enterprise plan is equivalent to self-hosted infrastructure on AWS or GCP. However, we consult on access management and other attack vectors.

We have automated monitoring test applications that continuously check for networks & errors using observability providers.

We use HTTPS for secure connections. We force HTTPS for all services using TLS (SSL), including our public website and the Dashboard to ensure secure connections.

All user data is encrypted in transit and at rest.

Internal code reviews are performed using a modern, PR-based development workflow (Github).

### Corporate security (CorpSec)

CorpSec is the practice of making sure Lamin employees have secure access to Lamin company infrastructure, and also that exposed channels to Lamin are secured. CorpSec controls are the primary concern of standards such as SOC2.

Access to our services and applications that connect to customer data is gated on a SSO Identity Provider (IdP). The exception is GitHub, where our employees are allowed to maintain accounts linked to their IdP of choice.

We mandate phishing-resistant multi-factor authentication (MFA) in all enrolled IdP accounts.

We regularly audit access to internal systems.

### Bug bounty program

Keeping user data secure is a top priority at Lamin. We welcome contributions from the security community to identify vulnerabilities in our product and disclose them to us in a responsible manner. We offer rewards ranging from $100 to $1000+ depending on the severity of the issue discovered. To participate, please send a report of the vulnerability to security@lamin.ai

### Data privacy

Lamin will never access or use your source code or data.
