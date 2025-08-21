# REST

## Swagger UI

The comprehensive REST API reference is documented via the Swagger UI [here](https://aws.us-east-1.lamin.ai/_docs).

## Example

To use the API from within Python, you can directly pass the token that LaminDB uses internally.

Authenticate via the CLI and pass your API key:

```bash
$ lamin login
```

Use `requests` and pass the token as in the example below:

```python
import lamindb as ln
import requests

requests.get(
    f"https://aws.us-east-1.lamin.ai/api/account",
    headers={"Authorization": f"Bearer {ln.setup.settings.user.access_token}"}
)
```

## Deployments

Currently, our hosted offer is based on 4 REST APIs for 4 AWS data centers:

- `https://aws.us-east-1.api.lamin.ai`
- `https://aws.us-west-2.api.lamin.ai`
- `https://aws.eu-central-1.api.lamin.ai`
- `https://aws.eu-west-2.api.lamin.ai`

On-prem deployments have their own APIs.

