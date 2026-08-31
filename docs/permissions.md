# Manage access permissions

Lamin allows you and your users to manage access similar to how you'd do it on GitHub, Google Drive, Microsoft Sharepoint, or Notion. Your infrastructure team stays in full control over storage & database permissions directly on AWS or GCP.

## How to

### Manage instance collaborators

You need to be an instance admin.

1. Click on the settings tab at the top right of your instance page, then select **Collaborators** on the left sidebar. You'll see a list of current collaborators with their roles.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/YoauPk6fyoedPfeY0000.png" style="width: 90%;"/>
</div>

2. Click **Add collaborator**, enter user handle and click **Save**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/9n4SBjsaCLagDapV0000.png" style="width: 90%;"/>
</div>

3. To remove a collaborator, click the three-dot menu next to their name and select **Remove collaborator**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/VNZWgVPOT8urR1uv0000.png" style="width: 90%;"/>
</div>

### Manage a restricted space

You need to be an instance admin.

To create a space:

1. Click on the settings tab at the top right of your instance page, then select **Spaces** on the left sidebar, then click **Create space**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/f9OPmq2zi0LhfhyK0000.png" style="width: 90%;"/>
</div>

2. Enter a name for your space and click **Save**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/TIlmKtBG63dse3sb0000.png" style="width: 90%;"/>
</div>

To add a collaborator to your space:

1. Click the three-dot menu next to the space and select **Manage collaborators**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/AJjcfgITI4YXWmOF0000.png" style="width: 90%;"/>
</div>

2. Click **Add collaborator** and select a user or team.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/60OjDFhxOmQqKWN30000.png" style="width: 60%;"/>
</div>

3. Change the access role if you want the collaborator to have more than read access.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/TT84gfGO05SZuNKx0000.png" style="width: 90%;"/>
</div>

Note that you can also manage spaces from the **Spaces** tab of your **Organization** tab and attach spaces to multiple instances, if desired.

(use-a-restricted-space)=

### Use a restricted space

To upload an artifact to a restricted {class}`~lamindb.Space`, pass a space name to `--space` in `lamin save`:

```python
lamin save ./myfile.txt --key myfile.txt --space "Our space"
```

You can pass the `space` argument when creating objects:

```python
space = ln.Space.get(name="Our space")  # get a space
ln.Artifact("./test.txt", key="test.txt", space=space).save()  # save artifact in space
```

You can pass a space or space name to {func}`~lamindb.track`, which automatically saves all artifacts, collections, transforms, runs and other subsequently created objects in that space:

```python
ln.track(space="Our space")
ln.Artifact("./myfile.txt", key="myfile.txt").save()  # saved into space "Our space"
```

To move an entity into a restricted space, set the `.space` field of its record:

```python
space = ln.Space.get(name="Our space")  # get a space
record = ln.Record.get(name="existing label")
record.space = space
record.save()  # saved in space "Our space"
```

Artifacts saved into a restricted space are stored in a storage location that belongs to that space. Instance collaborators who are not space collaborators cannot obtain credentials for those files. See [Storage permissions, federated credentials, and spaces](#storage-permissions-federated-credentials-and-spaces).

### Manage teams

Teams allow you to manage permissions for groups of users collectively, making it easier to handle access for departments or project groups.

To create a team:

1. Go to **Teams** tab of your organization page, and click **Create team**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/SSdvjNqXhBqf0F2f0000.png" style="width: 90%;"/>
</div>

2. Enter a team name and click **Save**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/9qNxlJmAjvf8DYPH0000.png" style="width: 90%;"/>
</div>

To add members to your team:

1. Click the three-dot menu next to the team and select **Manage members**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/XRW2QhHPDnJvgpGS0000.png" style="width: 90%;"/>
</div>

2. Click **Add member** and select a user.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/ZOKcBJniLj8DG7cD0000.png" style="width: 90%;"/>
</div>

To add a team to a space:

1. From the space collaborators view, click **Add collaborator** and select a team.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/DHouTU5KeskTalTv0000.png" style="width: 90%;"/>
</div>

To add a team to your instance:

1. From the instance collaborators view click on the **Teams** tab and click **Add team**.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/r7KLAklCYyvxqPIe0000.png" style="width: 90%;"/>
</div>

2. Select a team.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/FVqQysRswPvDm0hX0000.png" style="width: 90%;"/>
</div>

### Manage bot accounts

You need to be an org admin. Access to bot accounts for other org members will be enabled soon (July 2026).

Bot accounts allow scoping access permissions within automations, including through AI agents. They authenticate via their API keys.

To create a bot account:

1. Go to the **Settings** tab of your organization page.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/I5h08zAwEoEaomzt0002.png" style="width: 90%;"/>
</div>

2. Click **+ New bot account**, enter a handle and name, and click **Create**. An API key dialog opens automatically.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/1uauEK7PCPLhNNYO0001.png" style="width: 90%;"/>
</div>

3. Enter a description and expiration for the key, then click **Generate key**. Copy the key — it's shown only once.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/HnGsLDn5gZDB81wu0001.png" style="width: 90%;"/>
</div>

4. The bot account now appears in the list.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/SWtpjE8nKGVMtZuy0001.png" style="width: 90%;"/>
</div>

To add a bot as a collaborator to an instance:

1. Go to the **People** tab of your organization page. The bot account is already listed there as a member. Click the three-dot menu next to it and select **Edit member's instances**, then select the instance you want the bot to collaborate on.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/KHTjLMznPILYKLct0001.png" style="width: 90%;"/>
</div>

2. The bot account is now an instance collaborator with read access.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/f3EWFWuL7Ht1Sn7P0001.png" style="width: 90%;"/>
</div>

You can also add bots as collaborators to spaces, just like you add human users as collaborators to spaces.

## An example

An `ML` and a `Curation` team collaborate across spaces to server the wider organization:

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/rbMZRx714tQe4kZQ0000.png" style="width: 90%;"/>
</div>

| Space                       | Description                                                                                                               | Access                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Default `all` space         | Contains common assets like ontologies, tutorials, and non-sensitive datasets accessible to everyone within the instance. | _Every_ instance collaborator has read or higher levels of access.                                                                |
| Restricted `Curation` space | Stores sensitive curated data requiring stricter access permissions.                                                      | A `"Curation Team"` has write access. A `"ML Team"` has read access. No access granted to other teams by default.                 |
| Restricted `ML` space       | Contains machine learning models, development resources, and potentially experimental data.                               | Only `"ML Team"` has access (read/write as needed). Completely isolated from other teams & individuals unless explicitly granted. |

## Definitions

Lamin's access management is built on:

1.  **Users:** _User accounts_ belong to human users and own resources like databases.
2.  **Organizations:** _Organizational accounts_ can be accessed by the organization's members and own resources like user accounts.
3.  **Teams:** Groups of users. Roles and permissions can be assigned to teams like for users.
4.  **Bot accounts:** _Bot accounts_ are bots owned by an organization — not tied to a human user. Use them for CI pipelines, automations, and agents. They authenticate with API keys.
5.  **Databases:** LaminDB instances are SQLite or Postgres databases operated through LaminDB.
6.  **Spaces:** You can divide a LaminDB instance into multiple spaces to restrict access. You can manage space collaborators in the same way as instance collaborators.
7.  **Storage locations:** Storage locations hold the files behind artifacts. There is no standalone storage role: for managed S3 locations, access is implied by a user's instance and space roles and enforced with short-lived federated AWS credentials. See [Storage permissions, federated credentials, and spaces](#storage-permissions-federated-credentials-and-spaces).

### Spaces

Spaces allow to restrict permissions for any object in a LaminDB instance:

- Each space has its own set of collaborators with their roles and permissions, independent of instance-level roles.
- Users must be both instance collaborators AND space collaborators to access resources in a space within an instance.
- Spaces must be attached to an instance before records from that instance can be moved into the space (you need both instance and space admin permissions to attach the space to an instance). Attaching a space creates a dedicated storage location for that space in the instance.
- Spaces are applied at the database record level and any database record can only belong to a single space. An artifact's record space and its storage location are related but distinct: the record space governs metadata access, the storage location governs file access.

The default space of an instance: Every instance includes a default `all` space analogous to the default `main` branch. This space holds common resources that are meant to be accessible to all instance collaborators.

- **Read collaborators:** All collaborators added to an instance automatically receive read access to the default `all` space.
- **Write collaborators:** Collaborators granted write or admin permissions to the instance automatically receive write access to the default `all` space.

### Teams

Teams provide a way to manage permissions for groups of users for instances and spaces.
Users can be collaborators either directly as individual users or through team membership.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/61iaMcMV4NtDxFnb0000.png" style="width: 70%;"/>
</div>

### Storage locations

Storage locations hold the files behind artifacts. LaminHub storage access control applies only to managed S3 locations that issue federated credentials. Access is not assigned on the storage location itself; it is derived from instance and space collaborators.

- Storage in the default `all` space inherits the instance collaborator role.
- Storage attached to a restricted space inherits the space collaborator role.
- Public managed storage still uses the collaborator role when the caller is a collaborator. Callers who are not collaborators (including anonymous) get read access.

To restrict files as well as metadata, keep artifacts in a storage location that belongs to the same restricted space. See [Storage permissions, federated credentials, and spaces](#storage-permissions-federated-credentials-and-spaces).

## Roles

### Organization roles

| Role         | Description                                                                                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Admins**   | Manage organization members, teams, instances, spaces, and organization settings (domains/SSO). Instance/space data access still requires instance/space roles.         |
| **Managers** | Same as admins, except they cannot grant/revoke the organization admin role or manage organization settings.                                                            |
| **Members**  | Can be granted access to specific resources (teams, instances, spaces) based on assignments, and manage teams and spaces they are admins of. Default access is limited. |
| **Guests**   | Intended for external collaborators with limited access, typically restricted to specific instances or spaces they are explicitly invited to.                           |

### Team roles

| Role        | Description                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Admins**  | Can add/remove team members, define member roles within the team context, and manage team resources or settings. Can typically perform any action a member can. |
| **Members** | Can access resources granted to the team (e.g., specific instances or spaces).                                                                                  |

### Instance roles

| Role                    | Description                                                                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Admins**              | Can add/remove collaborators from the instance, define collaborator roles within the instance, and manage instance settings. For data access, automatically receive write access to the default "All" space only. |
| **Read collaborators**  | Automatically receive read access to the default "All" space only.                                                                                                                                                |
| **Write collaborators** | Automatically receive write access to the default "All" space only.                                                                                                                                               |

**Note:** Permissions for spaces other than the default "All" space must be managed separately and independently of the instance collaborator role.

### Space roles

| Role                    | Description                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| **Admins**              | Have full control over the specific space, including managing permissions and content within that space. |
| **Read collaborators**  | Can read data and view resources within that specific space across accessible instances.                 |
| **Write collaborators** | Can read, add, and modify data or resources within that specific space across accessible instances.      |

## How does it work?

Rather than configuring storage permissions on AWS and database permissions on Postgres, LaminHub allows you to manage collaborators for databases and storage locations in a similar way to how you manage access on Notion, Google Workspace, or Microsoft SharePoint.

However, in contrast to a typical SaaS product like GitHub, LaminHub leaves you in full control of your data with direct API access to databases and storage locations on AWS.

Based on an identity provider (Google, GitHub, SSO, OIDC) and a role-based permission system, LaminDB users automatically receive:

- **Storage access** with federated access tokens for managed S3 locations on AWS. These tokens are short-lived and thereby minimize attack surface. The token's IAM policy is scoped to the storage locations your instance and space roles allow; see [below](#storage-permissions-federated-credentials-and-spaces). This storage access control is not enforced for unmanaged buckets, GCP, or local storage.
- **Database access** with a database connection string associated with a JWT token applying user permissions through Postgres row-level security (RLS).

(storage-permissions-federated-credentials-and-spaces)=

## Storage permissions, federated credentials, and spaces

This storage access control is enforced only for **managed S3** locations that use federated AWS credentials. Unmanaged S3 buckets, GCP, and local storage are not gated this way: callers use whatever credentials or filesystem access they already have.

For managed S3, storage access is not a separate role. LaminHub derives it from instance and space collaborators, then issues short-lived federated AWS credentials scoped to the storage locations you can access.

### How storage inherits permissions

Every storage location belongs to an instance and to a space.

| Storage location | Who receives credentials | Role used for the token |
| ---------------- | ------------------------ | ----------------------- |
| Default `all` space | Instance collaborators (directly or via a team) | Instance role (`read` / `write` / `admin`) |
| Restricted space | Space collaborators (directly or via a team) | Space role (`read` / `write` / `admin`) |
| Public managed storage, collaborator | Instance or space collaborators, as above | The collaborator role (`read` / `write` / `admin`) |
| Public managed storage, not a collaborator | Anyone, including anonymous callers | Read |

Public managed storage does not replace collaborator status. Collaborators still receive their instance or space role. Read access for everyone is only the fallback when the caller is not a collaborator.

Instance collaborators who are not also collaborators of a restricted private space cannot obtain credentials for that space's storage. Organization membership alone is also not enough: you need a concrete instance or space collaborator role.

If several rules match the same path, LaminHub uses the longest matching storage root and the highest role (`admin` > `write` > `read`).

### Federated credentials

When LaminDB reads or writes an object on a managed S3 bucket, it asks LaminHub for credentials for that path. LaminHub:

1. Resolves the path to a registered storage location.
2. Looks up your derived role for that location (instance role, space role, or public read).
3. Refuses the request if you have no role and the location is not public.
4. Otherwise returns a short-lived AWS STS token whose IAM policy is limited to that storage root.

The policy grants `s3:GetObject` and `s3:ListBucket` for read access, and additionally `s3:PutObject` and `s3:DeleteObject` for write or admin access. If the storage root is a prefix inside a bucket (`s3://bucket/space-uid`), listing and object access are constrained to that prefix: credentials for one space cannot list or read another space's prefix in the same bucket.

You do not configure these policies yourself. Connect the bucket from the **Infrastructure** page of your organization on LaminHub so collaborators receive access through their LaminHub roles instead of long-lived AWS keys.

To request credentials without the Python client, see [Get S3 credentials](hub/authentication.md#3-get-s3-credentials).

### Keeping artifact files inside a restricted space

A record's space and its storage location are related but distinct. Spaces restrict metadata in the database; managed S3 storage locations restrict the files through federated credentials.

- Saving an artifact into a restricted space automatically uses a storage location that belongs to that space, so on managed S3 the file lands under a prefix that only space collaborators can access.
- A space can be attached to many storage locations. Create another managed location with:

```python
space = ln.Space.get(name="Our space")
ln.Storage(root="create-s3", space=space).save()  # new managed location for the space
```

In the [example](#an-example) above, instance collaborators can read the default `all` space and its storage. They cannot read files in the `Curation` or `ML` storage locations unless they are also collaborators of those spaces. The `"ML Team"` can read Curation files because it has read access to the `Curation` space — its instance role alone would not be enough.

## Low-level access management

While not necessary, you can still manage access on the AWS, GCP, or database level yourself, provided you have sufficient permissions for the corresponding systems in your cloud infrastructure.

### How to configure an AWS S3 bucket for public read access?

For a public read-only instance the bucket should have certain policies configured.
You can read about s3 bucket policies [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html). For a public read-only instance the bucket should have `s3:GetObject` and `s3:ListBucket` permissions. The example policy is given below:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AddPerm",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    },
    {
      "Sid": "AllowList",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::your-bucket-name"
    }
  ]
}
```

Change `your-bucket-name` above to the name of your s3 bucket.
