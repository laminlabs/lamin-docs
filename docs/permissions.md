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
4.  **Databases:** LaminDB instances are SQLite or Postgres databases operated through LaminDB.
5.  **Spaces:** You can divide a LaminDB instance into multiple spaces to restrict access. You can manage space collaborators in the same way as instance collaborators.
6.  **Storage locations:** Access to storage locations in the cloud are implied by a user's access to instances & spaces.

### Spaces

Spaces allow to restrict permissions for any object in a LaminDB instance:

- Each space has its own set of collaborators with their roles and permissions, independent of instance-level roles.
- Users must be both instance collaborators AND space collaborators to access resources in a space within an instance.
- Spaces must be attached to an instance before records from that instance can be moved into the space (you need both instance and space admin permissions to attach the space to an instance).
- Spaces are applied at the database record level and any database record can only belong to a single space.

The default space of an instance: Every instance includes a default `all` space analogous to the default `main` branch. This space holds common resources that are meant to be accessible to all instance collaborators.

- **Read collaborators:** All collaborators added to an instance automatically receive read access to the default `all` space.
- **Write collaborators:** Collaborators granted write or admin permissions to the instance automatically receive write access to the default `all` space.

### Teams

Teams provide a way to manage permissions for groups of users for instances and spaces.
Users can be collaborators either directly as individual users or through team membership.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/61iaMcMV4NtDxFnb0000.png" style="width: 70%;"/>
</div>

## Roles

### Organization roles

| Role         | Description                                                                                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Admins**   | Manage organization members, teams, instances, spaces, and organization settings (domains/SSO). Instance/space data access still requires instance/space roles.         |
| **Managers** | Same as admins, except they cannot grant/revoke the organization admin role or manage organization domains/SSO requirements.                                            |
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

- **Storage access** with federated access tokens for data on AWS. These tokens are short-lived and thereby minimize attack surface.
- **Database access** with a database connection string associated with a JWT token applying user permissions through Postgres row-level security (RLS).

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
