# Permissions

These endpoints manage LaminHub access for organizations, teams, spaces, and
instances.

For concepts, UI workflows, and role definitions, see
[Manage access permissions](../permissions.md).

## Organization permissions

Organization permissions control who can manage organization-owned resources such
as teams, spaces, service accounts, and instances.

| Method   | Endpoint                                                    | Description                                                     |
| -------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| `PUT`    | `/api/organizations`                                        | [Create an organization](#create-an-organization)               |
| `GET`    | `/api/organizations/{organization_id}`                      | Get an organization                                             |
| `GET`    | `/api/organizations/{organization_id}/members`              | List organization members                                       |
| `PUT`    | `/api/organizations/{organization_id}/members/{account_id}` | [Add an organization member](#add-an-organization-member)       |
| `PATCH`  | `/api/organizations/{organization_id}/members/{account_id}` | [Update an organization member](#update-an-organization-member) |
| `DELETE` | `/api/organizations/{organization_id}/members/{account_id}` | Remove an organization member                                   |

### Create an organization

JSON body:

- `handle`: required organization handle.

### Add an organization member

JSON body:

- `role`: optional organization role. Defaults to `member`.

### Update an organization member

JSON body:

- `role`: required organization role.

Related docs: [organization roles](../permissions.md#organization-roles),
[security](../security.md).

## Team permissions

Teams group users so they can be added to instances or spaces together.

| Method   | Endpoint                                     | Description                                   |
| -------- | -------------------------------------------- | --------------------------------------------- |
| `PUT`    | `/api/teams`                                 | [Create a team](#create-a-team)               |
| `GET`    | `/api/teams/{team_id}`                       | Get a team                                    |
| `PATCH`  | `/api/teams/{team_id}`                       | [Update a team](#update-a-team)               |
| `DELETE` | `/api/teams/{team_id}`                       | Delete a team                                 |
| `GET`    | `/api/teams/organizations/{organization_id}` | List teams in an organization                 |
| `GET`    | `/api/teams/{team_id}/members`               | List team members                             |
| `PUT`    | `/api/teams/{team_id}/members/{account_id}`  | [Add a team member](#add-a-team-member)       |
| `PATCH`  | `/api/teams/{team_id}/members/{account_id}`  | [Update a team member](#update-a-team-member) |
| `DELETE` | `/api/teams/{team_id}/members/{account_id}`  | Remove a team member                          |

### Create a team

JSON body:

- `name`: required team name.
- `organization_id`: required organization id.
- `description`: optional description.

### Update a team

Optional JSON body fields:

- `name`
- `description`

### Add a team member

JSON body:

- `role`: optional team role. Defaults to `member`.

### Update a team member

JSON body:

- `role`: required team role.

Related docs: [teams](../permissions.md#teams),
[team roles](../permissions.md#team-roles).

## Space permissions

Spaces restrict access within an instance. Users or teams can be space
collaborators with read, write, or admin access.

| Method   | Endpoint                                         | Description                                                 |
| -------- | ------------------------------------------------ | ----------------------------------------------------------- |
| `PUT`    | `/api/spaces`                                    | [Create a space](#create-a-space)                           |
| `GET`    | `/api/spaces/{space_id}`                         | Get a space                                                 |
| `PATCH`  | `/api/spaces/{space_id}`                         | [Update a space](#update-a-space)                           |
| `DELETE` | `/api/spaces/{space_id}`                         | Delete a space                                              |
| `GET`    | `/api/spaces/organizations/{organization_id}`    | List spaces in an organization                              |
| `PUT`    | `/api/spaces/{space_id}/instances/{instance_id}` | Attach a space to an instance                               |
| `DELETE` | `/api/spaces/{space_id}/instances/{instance_id}` | Detach a space from an instance                             |
| `GET`    | `/api/spaces/{space_id}/instances`               | List instances using a space                                |
| `GET`    | `/api/spaces/instances/{instance_id}`            | List spaces attached to an instance                         |
| `GET`    | `/api/spaces/{space_id}/collaborators`           | List space collaborators                                    |
| `PUT`    | `/api/spaces/{space_id}/collaborators`           | [Add a space collaborator](#add-a-space-collaborator)       |
| `PATCH`  | `/api/spaces/{space_id}/collaborators`           | [Update a space collaborator](#update-a-space-collaborator) |
| `DELETE` | `/api/spaces/{space_id}/collaborators`           | [Remove a space collaborator](#remove-a-space-collaborator) |
| `PUT`    | `/api/spaces/{space_id}/record-attachments`      | [Move an entry into a space](#move-an-entry-into-a-space)   |

### Create a space

JSON body:

- `name`: required space name.
- `organization_id`: required organization id.
- `description`: optional description.

### Update a space

Optional JSON body fields:

- `name`
- `description`

### Add a space collaborator

JSON body:

- `account_id`: account collaborator id. Mutually exclusive with `team_id`.
- `team_id`: team collaborator id. Mutually exclusive with `account_id`.
- `role`: optional space role. Defaults to `read`.
- `add_guest_if_missing`: optional. If `true`, add a missing account as an
  organization guest before adding it to the space.

### Update a space collaborator

JSON body:

- `account_id`: account collaborator id. Mutually exclusive with `team_id`.
- `team_id`: team collaborator id. Mutually exclusive with `account_id`.
- `role`: optional space role.

### Remove a space collaborator

Query parameters:

- `account_id`: account collaborator id. Mutually exclusive with `team_id`.
- `team_id`: team collaborator id. Mutually exclusive with `account_id`.

### Move an entry into a space

JSON body:

- `module_name`: required module name.
- `model_name`: required model name.
- `record_id`: required entry id in the instance database.

Related docs: [spaces](../permissions.md#spaces),
[space roles](../permissions.md#space-roles),
[use a restricted space](../permissions.md#use-a-restricted-space).

## Instance permissions

Instance collaborators control access to an instance. Collaborators can be users
or teams.

| Method   | Endpoint                                     | Description                                                         |
| -------- | -------------------------------------------- | ------------------------------------------------------------------- |
| `GET`    | `/api/instances/{instance_id}/collaborators` | List instance collaborators                                         |
| `PUT`    | `/api/instances/{instance_id}/collaborators` | [Add an instance collaborator](#add-an-instance-collaborator)       |
| `PATCH`  | `/api/instances/{instance_id}/collaborators` | [Update an instance collaborator](#update-an-instance-collaborator) |
| `DELETE` | `/api/instances/{instance_id}/collaborators` | [Remove an instance collaborator](#remove-an-instance-collaborator) |

### Add an instance collaborator

JSON body:

- `account_id`: account collaborator id. Mutually exclusive with `team_id`.
- `team_id`: team collaborator id. Mutually exclusive with `account_id`.
- `role`: optional instance role. Defaults to `read`.
- `add_guest_if_missing`: optional. If `true`, add a missing account as an
  organization guest before adding it to the instance.

### Update an instance collaborator

JSON body:

- `account_id`: account collaborator id. Mutually exclusive with `team_id`.
- `team_id`: team collaborator id. Mutually exclusive with `account_id`.
- `role`: required instance role.

### Remove an instance collaborator

Query parameters:

- `account_id`: account collaborator id. Mutually exclusive with `team_id`.
- `team_id`: team collaborator id. Mutually exclusive with `account_id`.

Related docs: [manage instance collaborators](../permissions.md#manage-instance-collaborators),
[instance roles](../permissions.md#instance-roles).
