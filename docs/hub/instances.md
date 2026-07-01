# Instances

These endpoints create and manage LaminDB instances and expose instance-level
connection information.

For registry queries inside an instance, see
[Registry querying](registry-querying.md).

## Endpoints

| Method   | Endpoint                                                         | Description                                                   |
| -------- | ---------------------------------------------------------------- | ------------------------------------------------------------- |
| `PUT`    | `/api/instances`                                                 | [Create an instance](#create-an-instance)                     |
| `GET`    | `/api/instances/{owner}/{name}/settings`                         | [Get instance settings](#get-instance-settings)               |
| `DELETE` | `/api/instances/{instance_id}`                                   | [Delete an instance](#delete-an-instance)                     |
| `PATCH`  | `/api/instances/{instance_id}/owner/{handle}`                    | Transfer instance ownership                                   |
| `POST`   | `/api/instances/{instance_id}/migrate`                           | Run instance migrations                                       |
| `GET`    | `/api/instances/{instance_id}/db_token`                          | [Get an instance database JWT](#get-an-instance-database-jwt) |
| `GET`    | `/api/instances/{instance_id}/schema`                            | Get the instance schema                                       |
| `GET`    | `/api/instances/{instance_id}/schema/{module_name}/{model_name}` | Get model relations                                           |
| `GET`    | `/api/instances/{instance_id}/statistics`                        | [Get instance statistics](#get-instance-statistics)           |
| `GET`    | `/api/instances/{instance_id}/non_empty_tables`                  | List non-empty tables                                         |

## Create an instance

Query parameters:

- `name`: required instance name.
- `storage`: optional storage path. Defaults to `create-s3`.
- `schema_str`: optional schema string.
- `db_server_name`: optional database server name.
- `storage_uid`: optional existing storage uid.
- `bucket_extra_parameters`: optional extra bucket parameters.
- `account_id`: optional owner account id.
- `public`: optional boolean.

```bash
curl -X PUT "https://aws.us-east-1.lamin.ai/api/instances?name=<instance-name>" \
  -H "Authorization: Bearer <lamin-jwt>"
```

## Get instance settings

```bash
curl "https://aws.us-east-1.lamin.ai/api/instances/<owner>/<name>/settings" \
  -H "Authorization: Bearer <lamin-jwt>"
```

## Delete an instance

Query parameter:

- `instance_name`: required instance name confirmation.

## Get an instance database JWT

```bash
curl "https://aws.us-east-1.lamin.ai/api/instances/<instance-id>/db_token" \
  -H "Authorization: Bearer <lamin-jwt>"
```

## Get instance statistics

Optional query parameter:

- `q`: model name in `module.ClassName` format. Repeat to request multiple
  models.
