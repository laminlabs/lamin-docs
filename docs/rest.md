# REST

See the Swagger UI [here](https://aws.us-east-1.lamin.ai/_docs).

Currently, our hosted offer is based on 4 REST APIs for 4 AWS data centers:

- `https://aws.us-east-1.api.lamin.ai`
- `https://aws.us-west-2.api.lamin.ai`
- `https://aws.eu-central-1.api.lamin.ai`
- `https://aws.eu-west-2.api.lamin.ai`

For example, this is how you would call the endpoint to retrieve your own account metadata:

```
# If you're not already logged in:
# from lamindb_setup import login
# login(...)

from lamindb_setup import settings
import requests

requests.get(
    f"https://aws.us-east-1.lamin.ai/api/account",
    headers={"Authorization": f"Bearer {settings.user.access_token}"}
)
```
