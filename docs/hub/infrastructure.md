# Infrastructure

These endpoints register S3 buckets and database servers.

## Buckets

| Method | Endpoint                                     | Description                                     |
| ------ | -------------------------------------------- | ----------------------------------------------- |
| `PUT`  | `/api/storages/s3/{bucket_name}/permissions` | [Register an S3 bucket](#register-an-s3-bucket) |

### Register an S3 bucket

Registers an S3 bucket in LaminHub and updates the bucket policy so Lamin can
access it.

JSON body:

- `aws_access_key_id`: required AWS access key id.
- `aws_secret_access_key`: required AWS secret access key.
- `region`: required bucket region.
- `aws_session_token`: optional AWS session token.
- `extra_parameters`: optional extra bucket parameters.

## Database servers

| Method | Endpoint                      | Description                                                   |
| ------ | ----------------------------- | ------------------------------------------------------------- |
| `POST` | `/api/db/server/register`     | [Register a database server](#register-a-database-server)     |
| `POST` | `/api/db/server/check-access` | [Check database server access](#check-database-server-access) |

### Register a database server

JSON body:

- `name`: required database server name.
- `url`: required database URL.
- `api_server_name`: required API server name.
- `organization_id`: required owning organization id.

### Check database server access

Query parameter:

- `name`: required database server name.
