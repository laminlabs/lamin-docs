# Account

These endpoints get account details, exchange API keys for JWTs, and manage
service accounts.

See [Authentication](authentication.md) for the common credential flow.

## Account endpoints

| Method | Endpoint           | Description                                                     |
| ------ | ------------------ | --------------------------------------------------------------- |
| `GET`  | `/api/account`     | [Get the authenticated account](#get-the-authenticated-account) |
| `POST` | `/api/account/jwt` | [Exchange an API key for a JWT](#exchange-an-api-key-for-a-jwt) |

### Get the authenticated account

```bash
curl "https://aws.us-east-1.lamin.ai/api/account" \
  -H "Authorization: Bearer <lamin-jwt>"
```

### Exchange an API key for a JWT

JSON body:

- `api_key`: required Lamin API key.

```bash
curl "https://aws.us-east-1.lamin.ai/api/account/jwt" \
  -H "Content-Type: application/json" \
  -d '{"api_key":"<your-lamin-api-key>"}'
```

## Service account endpoints

| Method   | Endpoint                                                                 | Description                                                           |
| -------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| `PUT`    | `/api/service-accounts`                                                  | [Create a service account](#create-a-service-account)                 |
| `GET`    | `/api/service-accounts/organizations/{organization_id}`                  | List service accounts                                                 |
| `GET`    | `/api/service-accounts/{organization_id}/{handle}`                       | Get a service account                                                 |
| `PATCH`  | `/api/service-accounts/{organization_id}/{handle}`                       | [Update a service account](#update-a-service-account)                 |
| `DELETE` | `/api/service-accounts/{organization_id}/{handle}`                       | Delete a service account                                              |
| `POST`   | `/api/service-accounts/{organization_id}/{handle}/api-keys`              | [Create a service account API key](#create-a-service-account-api-key) |
| `GET`    | `/api/service-accounts/{organization_id}/{handle}/api-keys`              | List service account API keys                                         |
| `DELETE` | `/api/service-accounts/{organization_id}/{handle}/api-keys/{api_key_id}` | Revoke a service account API key                                      |

### Create a service account

JSON body:

- `handle`: required service-account handle.
- `organization_id`: required owning organization id.
- `name`: optional display name.

### Update a service account

Optional JSON body field:

- `name`: display name.

### Create a service account API key

JSON body:

- `expires_at`: optional expiry datetime.
- `description`: optional description.

The plaintext API key is returned once. Store it immediately.
