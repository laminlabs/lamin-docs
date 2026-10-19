[LaminHub](https://lamin.ai) is a collaboration hub built on LaminDB similar to how GitHub is built on git:

- **permissions** → role-based, fine-grained access management for humans, bots & teams
- **audit logs** → full traceability for compliance
- **single sign-on** → social logins, Okta, Ping, and other providers
- **secure** → SOC2 certified, monitoring ISO27001 & HIPAA compliance
- **infra-as-code** → manage many databases and storage locations

Architecture:

- **zero lock-in** → LaminDB ensures data remains yours & accessible even if you cancel Lamin
- **permissions on the Postgres & storage layer** → no need for an intermediate web service
- **TRE (Trusted Research Environment)** → manage sensitive data from e.g. the UK Biobank
- **auto-generated REST API** → optional REST interface for JavaScript-based web applications

UI:

- **lineage** → interactive graphs for records, datasets, notebooks & pipelines
- **catalog** → browse, search & query records and datasets
- **notebooks, workflows, runs** → visualize & launch executions
- **versioning** → manage data & code revisions
- **LIMS & ELN** → records & notes integrated with ontologies
- **schemas, features, labels** → manage data models

Give it a try by exploring public databases at [lamin.ai/explore](https://lamin.ai/explore). It's free and no account is required.

For private data & commercial usage, see: [lamin.ai/pricing](https://lamin.ai/pricing).
