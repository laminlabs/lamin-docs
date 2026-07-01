# Authentication

Use these REST calls to get LaminHub credentials without the LaminDB Python client.

Replace the placeholders in angle brackets.

## 1. Get a Lamin JWT

Exchange a Lamin API key for a Lamin JWT:

```bash
curl -sS -X POST "https://aws.us-east-1.lamin.ai/api/account/jwt" \
  -H "Content-Type: application/json" \
  -d '{"api_key":"<your-lamin-api-key>"}'
```

Response:

```json
{ "accessToken": "<lamin-jwt>" }
```

## 2. Get an instance database JWT

Use the Lamin JWT to get a JWT for a specific LaminDB instance database:

```bash
curl -sS "https://aws.us-east-1.lamin.ai/api/instances/<instance-id>/db_token" \
  -H "Authorization: Bearer <lamin-jwt>"
```

Response:

```json
{ "token": "<instance-db-jwt>" }
```

## 3. Get S3 credentials

Use the Lamin JWT to get short-lived AWS credentials scoped to an S3 path.

```bash
curl -sS -X POST "https://hub.lamin.ai/functions/v1/get-cloud-access-v1" \
  -H "Authorization: Bearer <lamin-jwt>" \
  -H "Content-Type: application/json" \
  -d '{"path":"s3://your-bucket/optional-prefix"}'
```

Response:

```json
{
  "Credentials": {
    "AccessKeyId": "<aws-access-key-id>",
    "SecretAccessKey": "<aws-secret-access-key>",
    "SessionToken": "<aws-session-token>",
    "Expiration": "..."
  },
  "StorageAccessibility": {
    "storageRoot": "s3://your-bucket/optional-prefix"
  }
}
```
