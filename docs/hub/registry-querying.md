# Registry querying

Use these endpoints to query LaminDB registry entries through the Hub REST API.

See [Authentication](authentication.md) for getting a Lamin JWT.

## Generic registry querying

First, inspect the instance schema to find module and model names:

```bash
curl "https://aws.us-east-1.lamin.ai/api/instances/<instance-id>/schema" \
  -H "Authorization: Bearer <lamin-jwt>"
```

Then query a registry model:

```bash
curl "https://aws.us-east-1.lamin.ai/api/instances/<instance-id>/modules/<module-name>/<model-name>?limit=10" \
  -H "Authorization: Bearer <lamin-jwt>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

| Method | Endpoint                                                                              | Description                                                   |
| ------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `GET`  | `/api/instances/{instance_id}/schema`                                                 | Inspect the schema                                            |
| `GET`  | `/api/instances/{instance_id}/schema/{module_name}/{model_name}`                      | Inspect model relations                                       |
| `POST` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}`                     | [Query entries](#query-entries)                               |
| `POST` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/{id_or_uid}`         | [Get one entry](#get-one-entry)                               |
| `POST` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/fields/{field_path}` | [Query field values](#query-field-values)                     |
| `POST` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/query_features`      | [Query linked features](#query-linked-features)               |
| `POST` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/relatives`           | [Query hierarchical relatives](#query-hierarchical-relatives) |
| `POST` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/group-by`            | [Group entries](#group-entries)                               |
| `GET`  | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/{id}/counts`         | Count related entries                                         |

### Query entries

Optional JSON body fields:

- `select`: fields to return.
- `filter`: field filters, for example `{ "name": { "contains": "sample" } }`.
- `order_by`: sorting, for example `[{ "field": "created_at", "descending": true }]`.
- `search`: search text.
- `search_in`: fields to search in.
- `scope`: branch or space scope, for example `{ "branch_ids": [1] }`.

Example body:

```json
{
  "select": ["uid", "name"],
  "filter": { "name": { "contains": "sample" } },
  "scope": { "branch_ids": [1] }
}
```

### Get one entry

Optional JSON body fields:

- `select`: fields to return.
- `scope`: branch or space scope.

### Query field values

Optional JSON body fields:

- `filter`
- `order_by`
- `search`
- `search_in`
- `scope`

### Query linked features

Optional JSON body fields:

- `select`
- `filter`
- `order_by`
- `search`
- `search_in`
- `scope`

### Query hierarchical relatives

Required JSON body field:

- `relatives`: traversal settings.

Optional JSON body fields:

- `select`
- `filter`
- `order_by`
- `search`
- `search_in`
- `scope`

Example body:

```json
{
  "relatives": {
    "field": "uid",
    "values": ["<ulabel-uid>"],
    "kind": "ancestors",
    "depth": 1
  }
}
```

### Group entries

Required JSON body fields:

- `dimensions`: fields to group by.
- `measures`: aggregations such as `count`, `sum`, `min`, `max`, or `mean`.

Optional JSON body fields:

- `filter`
- `scope`

Example body:

```json
{
  "dimensions": [{ "field_name": "suffix" }],
  "measures": [{ "field_name": "id", "agg_func": "count", "alias": "count" }]
}
```

## Specific registries

The generic endpoints above work for every registry model. Some entities also
have dedicated endpoints for actions not covered by generic model queries.

### Artifacts

| Method | Endpoint                                                  | Description                                                                           |
| ------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `POST` | `/api/instances/{instance_id}/artifacts/upload`           | [Upload and register an Artifact](#upload-and-register-an-artifact)                   |
| `POST` | `/api/instances/{instance_id}/artifacts/create`           | [Register an Artifact from a storage path](#register-an-artifact-from-a-storage-path) |
| `GET`  | `/api/instances/{instance_id}/artifacts/by-path?path=...` | Get an Artifact by storage path                                                       |

#### Upload and register an Artifact

Multipart form body:

- `file`: required.
- `kwargs`: optional JSON string.

#### Register an Artifact from a storage path

JSON body:

- `path`: required storage path.
- `kwargs`: optional Artifact parameters.

```bash
curl "https://aws.us-east-1.lamin.ai/api/instances/<instance-id>/artifacts/create" \
  -H "Authorization: Bearer <lamin-jwt>" \
  -H "Content-Type: application/json" \
  -d '{"path":"s3://your-bucket/path/file.h5ad","kwargs":{}}'
```

Related docs: [create an artifact](../tutorial.md#create-an-artifact),
[access artifacts](../tutorial.md#access-artifacts).

### Transforms

| Method | Endpoint                                  | Description                               |
| ------ | ----------------------------------------- | ----------------------------------------- |
| `POST` | `/api/instances/{instance_id}/transforms` | [Create a Transform](#create-a-transform) |

#### Create a Transform

JSON body:

- `key`: required.
- `kind`: required.
- `source_code`: required.
- `kwargs`: optional.

Related docs: [track changes](../tutorial.md#track-changes),
[launch computational pipelines](../launch.md).

### Universal labels

| Method   | Endpoint                                                                                        | Description                                               |
| -------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `POST`   | `/api/instances/{instance_id}/modules/core/ulabel/relatives`                                    | [Query the ULabel hierarchy](#query-the-ulabel-hierarchy) |
| `PUT`    | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/{id}/{label_field}/{label_id}` | [Attach a label](#attach-or-detach-a-label)               |
| `DELETE` | `/api/instances/{instance_id}/modules/{module_name}/{model_name}/{id}/{label_field}/{label_id}` | [Detach a label](#attach-or-detach-a-label)               |

#### Query the ULabel hierarchy

Use the same body as
`POST /api/instances/{instance_id}/modules/{module_name}/{model_name}/relatives`.

#### Attach or detach a label

Attach or detach a label using the target entry id, label field, and label id in
the path.

Related docs: [annotate an artifact](../tutorial.md#annotate-an-artifact),
[manage biological ontologies](../tutorial.md#manage-biological-ontologies).

### Records

| Method | Endpoint                                            | Description                                     |
| ------ | --------------------------------------------------- | ----------------------------------------------- |
| `POST` | `/api/instances/{instance_id}/records/{uid}/export` | [Export a Record table](#export-a-record-table) |

#### Export a Record table

Optional JSON body field:

- `kwargs`: export parameters.

Related docs: [manage records](../records.md).
