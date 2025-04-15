# Access management

This document outlines the access control system, detailing its architecture, key features, roles, and implementation guidelines.

## Quickstart

### Example

A typical organization might structure its spaces within instances like this:

1.  **`"All"` dpace (default):**

    - **Purpose:** Contains common assets like ontologies, tutorials, and non-sensitive datasets accessible to everyone within the instance.
    - **Access:** Generally broad read access for instance collaborators.

2.  **`"Curation"` space:**

    - **Purpose:** Stores sensitive curated data requiring stricter access control.
    - **Access example:**
      - `"Curation Team"` has write access.
      - `"ML Team"` has read access.
      - No access granted to other teams by default.

3.  **`"ML"` space:**
    - **Purpose:** Contains machine learning models, development resources, and potentially experimental data.
    - **Access example:**
      - Only `"ML Team"` has access (read/write as needed).
      - Completely isolated from other teams unless explicitly granted.

### Getting started guide 2

#### 1. Set up your organization structure

- Ensure you have access to your designated **organization** and verify that you or another user in your organization has sufficient organization permissions (organization admin role). Contact support if no one has the required permissions to properly set up your access control structure.

#### 2. Add or remove an instance collaborator

1. Click on the settings icon in your instance (or via https://lamin.ai/your-organization/your-instance/settings), then select the **Collaborators** tab. You'll see a list of current collaborators with their roles.

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

#### 3. Make space within an instance to restrict access

Spaces allow you to partition your data with separate access controls within the same instance.

To create spaces:

1. Go to **Spaces** in the left sidebar of your organization settings (or via https://lamin.ai/your-organization/spaces), then click **Create space**.

   <div align="center">
     <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/LA45MBNYosthrCKb0000.png" style="width: 90%;"/>
   </div>

2. Enter a name for your space and click **Save**.

   <div align="center">
     <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/bRTJgrDBVJg0Xv7X0000.png" style="width: 90%;"/>
   </div>

To add a collaborator to your space:

1. Click the three-dot menu next to the space and select **Manage collaborators**.

   <div align="center">
     <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/HdcNNk4mrS0kkwpr0000.png" style="width: 90%;"/>
   </div>

2. Click **Add collaborator** and select a user.

   <div align="center">
     <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/8538ULC90NWkEixx0000.png" style="width: 90%;"/>
   </div>

To attach an existing space to an instance:

1. Click the three-dot menu next to the space and select **Manage instances**.

   <div align="center">
     <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/LHFcJ58FGpRCVYWH0000.png" style="width: 90%;"/>
   </div>

2. Click **Attach instance** and select an instance.

   <div align="center">
     <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/8Jt9qChPmWzDOkMM0000.png" style="width: 90%;"/>
   </div>

#### 4. Make a team to bulk-manage access for multiple users

Teams allow you to manage permissions for groups of users collectively, making it easier to handle access for departments or project groups.

To create a team:

1. Go to **Teams** in the left sidebar of your organization settings (or via https://lamin.ai/your-organization/teams), and click **Create team**.

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

## Concepts

Our access management is built on a four-tier hierarchy, providing granular control over resources:

1.  **Organizations:** An organizational account can group users, instances, and other entities belonging to the same organization.
2.  **Teams:** Groups of users within an organization. Roles and permissions can be assigned collectively to teams.
3.  **Instances:** LaminDB instances are the central databases at the heart of the data platform similar to how git repositories are central to GitHub.
4.  **Spaces:** You can divide a LaminDB instance into multiple spaces to restrict access. You can manage space collaborators in the same way as instance collaborators.

## Key features

### Spaces

Spaces are areas within instances that allow specific permissions to be set on subsets of data for organization resources by department, project, or sensitivity level:

- Each space has its own set of collaborators with their roles and permissions, independent of instance-level roles.
- Users must be both instance collaborators AND space collaborators to access resources in a space within an instance.
- Spaces must be attached to an instance before records from that instance can be assigned to the space (you need both instance and space admin permissions to create this attachment).
- Spaces are applied at the database record level, and a record can only belong to one space.

<div align="center">
  <img src="https://lamin-site-assets.s3.amazonaws.com/.lamindb/rbMZRx714tQe4kZQ0000.png" style="width: 90%;"/>
</div>

### All space

- **Default "All" space:** Every instance includes a default `"All"` space upon creation. This space holds common resources that are meant to be accessible to all instance collaborators.
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
