# Access management, secrets & security

## Open-source

LaminDB is open-source software that operates inside your infrastructure like any other open-source package.

The sign up & log in for LaminDB only store email address, user name, and identifiers like s3 bucket names or public database URIs that you register on LaminHub. Unless you explicitly grant Lamin access to your infrastructure (e.g., through AWS secrets), LaminHub has no access to your data.

This means: You can use LaminDB for your private data for free, but you can't use LaminHub for your private data.

## Closed-source

If you'd like to manage access to private data, you can do so on an enterprise plan.

There are two options:

1. You manage secrets & authorization through Lamin Vault (standard enterprise plan, see below).
2. We license LaminHub to host on-prem behind your VPC/firewall (higher effort, and hence, higher cost).

## Lamin Vault

Lamin Vault is an enterprise feature that allows you to flexibly manage access to databases & storage locations through simple collaborator management in LaminHub.

Additionally, you will be able to create fine-grained roles using SQL & cloud (AWS, GCP) policies.

Lamin Vault is based on [HashiCorp](https://en.wikipedia.org/wiki/HashiCorp) Vault, the industry leader in this space.

### How does it work?

1. **Initialization**: You initialize the Vault for any LaminDB instance by providing an admin connection string to your Postgres database. The information is securely stored in HashiCorp Vault.
2. **Access generation**: If a collaborator wants to access the Postgres database, the Vault dynamically generates unique short-lived tokens for each session (e.g., for username & password). The permissions of these credentials are subject to pre-defined policies and typically defined through LaminHub's collaborator management (e.g., "read" vs. "write" access).

This process ensures that access to the database is secure, managed efficiently, and follows the principle of least privilege & short-lived tokens.

### How to use vault with `lamindb`?

For any given Postgres-based instance, you can enable access management through the vault.

#### Initializing Vault

There are two ways to initialize Vault in Lamin.

1. **When initializing an instance, with —vault flag**

   This command initializes an instance with a Postgres database. The connection string for the database is stored securely in Vault.

   ```bash
   lamindb init --db postgresql://USER:PWD@HOSTANME:PORT/DBNAME --vault
   ```

   In Python:

   ```python
   from lamindb_setup import init_vault

   init_vault(db="postgresql://USER:PWD@HOSTANME:PORT/DBNAME")
   ```

2. **Using the init_vault command**

   This command is used to initialize Vault for the current LaminDB instance. It is used internally by the init command.

   ```bash
   lamindb init_vault --db postgresql://USER:PWD@HOSTANME:PORT/DBNAME --vault
   ```

   In Python:

   ```python
   from lamin_vault.client._init_instance_vault import init_instance_vault

   init_instance_vault(
       vault_admin_client=VAULT_ADMIN_CLIENT,
       instance_id=INSTANCE_ID,
       admin_account_id=ADMIN_ACCOUNT_ID,
       db_host=DB_HOST,
       db_port=DB_PORT,
       db_name=DB_NAME,
       vault_db_username=VAULT_DB_USERNAME,
       vault_db_password=VAULT_DB_PASSWORD,
   )
   ```

#### Using Vault when Loading an Instance

When you load an instance using —vault flag, it fetches the database connection details from Vault and to generate credentials and establishes a secure connection to the database.

```bash
lamindb load INSTANCE_IDENTIFIER --vault
```

In Python:

```python
from lamindb_setup import load_instance

load_instance(instance_name="INSTANCE_IDENTIFIER")
```

#### Important Note

Vault is used by default when loading an instance. However, for SQLite instances, Vault is not used. This is because SQLite databases are file-based and do not require a connection string.

### How do we ensure credentials can only be retrieved by authorized users?

1. **JWT exchange**

   When a request is made to retrieve credentials, a JSON Web Token (JWT) is used to authenticate the requester. This JWT is signed by a trusted entity (Supabase) and contains claims about the identity of the requester.

   This process is done through the following steps:

   - The JWT is sent to a trusted identity provider (`laminhud-rest`).
   - The trusted identity provider verifies the JWT is valid.
   - It then use requester identity to retrieve the associated vault policy and database role configuration (a SQL query).
   - It finally returns a vault token that is restricted to only read generated credentials, by vault policy, for a specific db role

   This process is handled by the identity provider and is transparent to Lamin clients (`lamindb-setup` or `laminapp-rest`)

2. **Request**

   The Vault token, is used to make an authenticated request to Vault and retrieve the database credentials.

3. **Credential Generation**

   Vault dynamically generates a new set of credentials (username and password) for the database. These credentials are unique for each request to the vault and have a limited lifespan. The role name passed to this function determines the permissions of the generated credentials and vault policy enabling to retrieve them.

4. **Credential Delivery**

   Vault delivers the credentials back to the Lamin instance. These credentials are then used to establish a secure connection to the database.

### How do we ensure vault can only be configured by an instance admin?

1. **JWT exchange**

   The process is a bit different to the one to generate credentials:

   - The JWT is sent to a trusted identity provider (`laminhud-rest`).
   - The trusted identity provider verifies the JWT is valid.
   - It then use requester identity to verify the user is an instance admin
   - It used predefined admin vault policy and admin database role configuration.
   - It finally returns a vault token that can manage vault configuration because it used an admin vault policy

2. **Vault configuration**

   The Vault token, is used to make an authenticated request to Vault and modify policies and db roles.

### How do we manage authorization?

When a collaborator is added to an instance, we create a new role in the vault for this collaborator with authorizations depending on the provided lamin role (read, write, admin). Delete or update of a collaborator are also propagate in the vault.
