# Manage access

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
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/60OjDFhxOmQqKWN30000.png" style="width: 90%;"/>
</div>

3. Change the access role if you want the collaborator to have more than read access.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/TT84gfGO05SZuNKx0000.png" style="width: 90%;"/>
</div>

Note that you can also manage spaces from the **Spaces** tab of your **Organization** tab and attach spaces to multiple instances, if desired.

### Use a restricted space

By passing `space` to `ln.track()`, you configure the `space` in which you save records during a tracked compute session.

```python
ln.track(space="Our space")
ln.ULabel(name="new label").save()  # saved into space "Our space"
```

To move an entity from one space to another, set the `.space` field of its record.

```python
space = ln.Space.get(name="my space")  # select a space
ulabel = ln.ULabel.get(name="existing label")
ulabel.space = space
ulabel.save()  # save in space "my space"
```

If a record isn't yet saved, setting the `.space` field determines the space in which you save the record.

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

1. From the space collaborators view, click **Add collaborator** and select a user.

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

## Example

One way of using spaces to restrict access within an instance is this.

1.  **Default space: `"All"`**

    - Purpose: Contains common assets like ontologies, tutorials, and non-sensitive datasets accessible to everyone within the instance.
    - Access: _Every_ instance collaborator has read or higher levels of access.

2.  **Restricted space 1: `"Curation"`**

    - Purpose: Stores sensitive curated data requiring stricter access control.
    - Access example:
      - A `"Curation Team"` has write access.
      - A `"ML Team"` has read access.
      - No access granted to other teams by default.

3.  **Restricted space 2: `"ML"`**
    - Purpose: Contains machine learning models, development resources, and potentially experimental data.
    - Access example:
      - Only `"ML Team"` has access (read/write as needed).
      - Completely isolated from other teams & individuals unless explicitly granted.

## Definitions

Lamin's access management is built on:

1.  **Organizations:** An organizational account can group users, instances, and other entities belonging to the same organization.
2.  **Teams:** Groups of users within an organization. Roles and permissions can be assigned collectively to teams.
3.  **Instances:** LaminDB instances are the central databases at the heart of the data platform similar to how git repositories are central to GitHub.
4.  **Spaces:** You can divide a LaminDB instance into multiple spaces to restrict access. You can manage space collaborators in the same way as instance collaborators.
5.  **Storage locations:** Access to storage locations in the cloud are implied by a user's access to instances & spaces.

### Spaces

Spaces are areas within instances that allow specific permissions to be set on subsets of data for organization resources by department, project, or sensitivity level:

- Each space has its own set of collaborators with their roles and permissions, independent of instance-level roles.
- Users must be both instance collaborators AND space collaborators to access resources in a space within an instance.
- Spaces must be attached to an instance before records from that instance can be assigned to the space (you need both instance and space admin permissions to create this attachment).
- Spaces are applied at the database record level, and a record can only belong to one space.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/rbMZRx714tQe4kZQ0000.png" style="width: 90%;"/>
</div>

The default space of an instance:

- **Default space:** Every instance includes a default space with the name `"All"` upon creation. This space holds common resources that are meant to be accessible to all instance collaborators.
- **Read collaborators:** All collaborators added to an instance automatically receive read access to the default `"All"` space.
- **Write collaborators:** Collaborators granted write or admin permissions at the instance level automatically receive write access to the default `"All"` space.

### Teams

Teams provide a way to manage permissions for groups of users for instances and spaces.
Users can be collaborators either directly as individual users or through team membership.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/61iaMcMV4NtDxFnb0000.png" style="width: 70%;"/>
</div>

## Role definitions

### Organization roles

- **Admins:** Have complete access and control over all resources within the organization, including managing teams, instances, spaces, and organization settings.
- **Managers:** Can manage teams, instances, and spaces but may have limitations on modifying organization-level settings.
- **Members:** Can be granted access to specific resources (teams, instances, spaces) based on assignments. Default access might be limited.
- **Guests:** Intended for external collaborators with limited access, typically restricted to specific instances or spaces they are explicitly invited to.

### Team roles

- **Admins:** Can add/remove team members, define member roles within the team context, and manage team resources or settings. Can typically perform any action a member can.
- **Members:** Can access resources granted to the team (e.g., specific instances or spaces).

### Instance roles

- **Admins:** Can add/remove collaborators from the instance, define collaborator roles within the instance, and manage instance settings. For data access, automatically receive write access to the default "All" space only.
- **Read collaborators:** Automatically receive read access to the default "All" space only.
- **Write collaborators:** Automatically receive write access to the default "All" space only.

**Note:** Permissions for spaces other than the default "All" space must be managed separately and independently of the instance collaborator role.

### Space roles

- **Admins:** Have full control over the specific space, including managing permissions and content within that space.
- **Read collaborators:** Can read data and view resources within that specific space across accessible instances.
- **Write collaborators:** Can read, add, and modify data or resources within that specific space across accessible instances.

## How does it work?

Rather than configuring storage permissions on AWS and database permissions on Postgres, LaminHub allows you to manage collaborators for databases and storage locations in a similar way to how you manage access on Notion, Google Workspace, or Microsoft SharePoint.

However, in contrast to a typical SaaS product like GitHub, LaminHub leaves you in full control of your data with direct API access to databases and storage locations on AWS.

Based on an identity provider (Google, GitHub, SSO, OIDC) and a role-based permission system, LaminDB users automatically receive:

- **Storage access** with federated access tokens for data on AWS. These tokens are short-lived and thereby minimize attack surface. (This will soon be replaced by endpoints proxying S3).
- **Database access** with a database connection string associated with a JWT token applying user permissions through Postgres row-level security (RLS).

LaminHub's permission system makes it easy to minimize attack surfaces by implementing the principle of least privilege.
