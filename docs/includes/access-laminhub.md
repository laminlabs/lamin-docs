Rather than configuring storage & database permissions directly on AWS or GCP, LaminHub allows you to manage collaborators for databases & storage locations in the same way you manage access to repositories on GitHub. However, in contrast to a typical SaaS product like GitHub, LaminHub leaves you in full control of your data with direct API access to databases & storage locations on AWS or GCP.

How does it work?

- Based on an identity provider (Google, GitHub, SSO, OIDC) and a role-based permission system, LaminDB users automatically receive federated access tokens for data on AWS or GCP. These tokens are short-lived and thereby minimize attack surface.
- LaminHub's permission system makes it easy to minimize attack surfaces by implementing the principle of least privilege.
