# Managing Credentials and Authorization with Vault in Lamin

Vault is used in Lamin to securely manage and provide database credentials, as well as handle authorization. Here's a simple explanation of how it works:

1. **Initialization**
    
    When you initialize Vault with a database connection string, Vault establishes a connection with the database. This connection string contains the necessary details like the database host, port, username, and password.
    
2. **Credential Generation**
    
    Once Vault is connected to the database, it can dynamically generate credentials (username and password) for the database. These credentials have a limited lifespan and are unique for each session. This means that every time you load an instance in Lamin, Vault provides a new set of credentials to connect to the database.
    
3. **Authorization**
    
    Vault also manages authorization. When it generates credentials, it also assigns specific permissions to these credentials based on predefined policies. This ensures that the credentials have the necessary permissions to perform their intended tasks, and no more. This principle of least privilege reduces the risk of unauthorized access or actions.
    
4. **Credential Revocation**
    
    When the lifespan of the credentials ends, Vault automatically revokes them.
    

This process ensures that access to the database is secure, managed efficiently, and follows the principle of least privilege, reducing the risk of credentials being leaked, misused, or performing unauthorized actions.

## How to use vault with `lamindb`?

### Initializing Vault

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
    

### Using Vault when Loading an Instance

When you load an instance using —vault flag, it fetches the database connection details from Vault and to generate credentials and establishes a secure connection to the database.

```bash
lamindb load INSTANCE_IDENTIFIER --vault
```

In Python:

```python
from lamindb_setup import load_instance

load_instance(instance_name="INSTANCE_IDENTIFIER")
```

### Important Note

Vault is used by default when loading an instance. However, for SQLite instances, Vault is not used. This is because SQLite databases are file-based and do not require a connection string.

## How do we ensure credentials can only be retrieved by authorized users?

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
    

## How do we ensure vault can only be configured by an instance admin?

1. **JWT exchange**
    
    The process is a bit different to the one to generate credentials:
    
    - The JWT is sent to a trusted identity provider (`laminhud-rest`).
    - The trusted identity provider verifies the JWT is valid.
    - It then use requester identity to verify the user is an instance admin
    - It used predefined admin vault policy and admin database role configuration.
    - It finally returns a vault token that can manage vault configuration because it used an admin vault policy
2. **Vault configuration**
    
    The Vault token, is used to make an authenticated request to Vault and modify policies and db roles.
    

## How do we manage authorization?

When a collaborator is added to an instance, we create a new role in the vault for this collaborator with authorizations depending on the provided lamin role (read, write, admin). Delete or update of a collaborator are also propagate in the vault.
