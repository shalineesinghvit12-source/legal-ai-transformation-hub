# Legal-technology adapter contract

This design demonstrates integration awareness without requiring proprietary iManage, Intapp, or Litera credentials.

## Common interface

| Operation | Input | Output |
| --- | --- | --- |
| Search matter | Matter name or authorized identifier | Minimal matter metadata |
| Get document | Authorized document identifier and version | File stream plus classification metadata |
| Save reviewed artifact | Matter, workspace, document, profile | New version or governed derivative identifier |
| Add activity | Matter, activity type, timestamp, outcome | Activity identifier |

## Adapter principles

- Use vendor-supported APIs and an approved custom connector.
- Authenticate through an approved service principal or delegated user flow.
- Enforce source-system authorization, ethical walls, and matter-level access.
- Retrieve only fields required for the current task.
- Preserve document IDs, versions, classifications, and audit correlation IDs.
- Do not replicate complete repositories into Dataverse.
- Handle throttling, retries, idempotency, and partial failure.
- Confirm licensing and API availability directly with the platform owner and vendor.

## Demonstration mode

Replace external calls with a mock response containing synthetic matter and document IDs. Clearly label the adapter as a design boundary, not an implemented production integration.

