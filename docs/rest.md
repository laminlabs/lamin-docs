# REST

```{toctree}
:maxdepth: 1
:caption: Hub
:hidden:

hub/authentication
hub/service-endpoints
```

This page documents the REST API of LaminHub.

## Swagger UI

The comprehensive REST API reference is documented via the Swagger UI [here](https://lamin.ai/_docs).

## Example

To use the API from within Python, you can directly pass the token that LaminDB uses internally.

Authenticate via the CLI and pass your API key:

```bash
$ lamin login
```

Use `requests` and pass the token as in the example below:

```python
import lamindb_setup as lns
import requests

response = requests.get(
    "https://lamin.ai/api/account",
    headers={"Authorization": f"Bearer {lns.settings.user.access_token}"}
)
response.json()
# {...}
```

## Deployments

Use `https://lamin.ai/api` for hosted deployments. Requests are automatically routed to the appropriate region.

Hosted services are currently available in four AWS regions:

- US East (N. Virginia): `us-east-1`
- US West (Oregon): `us-west-2`
- EU Central (Frankfurt): `eu-central-1`
- EU West (London): `eu-west-2`

On-prem deployments have their own APIs.
