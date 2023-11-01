# Access management & security

## Open-source

LaminDB is open-source software that operates inside your infrastructure and is subject to your security measures.

By using LaminDB, Lamin obtains no access to your data.

- The sign up & log in to LaminHub only stores & uses email address & user name to create a unique user identity.
- If you register a LaminDB instance on LaminHub, storage locations (AWS S3 or GCP bucket names, directory names) are stored.

## Closed-source

If you'd like to conveniently manage access to private data, you can do so on an enterprise plan. We are happy to

1. host data & databases for you on AWS or GCP
2. help you host data & databases in your AWS or GCP organization
3. help you connect your existing data & databases to LaminDB & LaminHub

If you are on AWS or GCP, we can deploy a LaminHub backend behind your VPC/firewall.

For fine-grained access management, there are two options. You manage secrets & authorization

1. manually with AWS/GCP policies and SQL roles and provide us with what is needed to connect LaminHub
2. through Lamin Vault, a standard Vault service (currently in beta), which integrates storage policies and SQL roles in a simple interface
