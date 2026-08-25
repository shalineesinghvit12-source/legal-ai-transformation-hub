# Power Platform deployment guide

## Prerequisites

- Microsoft Power Platform development environment with Dataverse
- Copilot Studio entitlement
- Power Automate premium capability for Dataverse and any premium connectors used
- AI Builder capacity or an approved alternative AI endpoint
- Teams, SharePoint, Outlook, Forms, and Power BI access as required
- Maker, system customizer, and environment-administration access for the setup team

Licensing and connector availability vary by tenant. Confirm them with the Microsoft 365 and Power Platform administrators before committing the production architecture.

## Environment strategy

Use separate Development, Test, and Production environments. Create an unmanaged solution in Development and deploy managed solutions downstream through Power Platform Pipelines.

Recommended solution name: `LegalAITransformationHub`

Recommended publisher prefix: `lai`

## Environment variables

| Variable | Example development value |
| --- | --- |
| `lai_SharePointSiteUrl` | Development demonstration site |
| `lai_DocumentLibraryName` | `SyntheticLegalDocuments` |
| `lai_ReviewerGroupId` | Development reviewer group |
| `lai_DefaultConfidenceThreshold` | `0.85` |
| `lai_HighConfidenceThreshold` | `0.90` |
| `lai_FeedbackFormUrl` | Development form URL |
| `lai_DashboardUrl` | Development Power BI report URL |
| `lai_RetentionDays` | `90` for demo data |

## Connection references

- Microsoft Dataverse
- Microsoft Teams
- SharePoint
- Office 365 Outlook
- Approvals
- Microsoft Forms
- AI Builder or approved AI service

Use service principals or governed service accounts where organizational policy allows. Do not bind production flows to a developer's personal connection.

## Build sequence

1. Create choices, then tables and relationships from `dataverse/schema.csv`.
2. Configure security roles: Submitter, Reviewer, Portfolio Manager, Platform Administrator, Dashboard Reader.
3. Create the model-driven application and views.
4. Implement child flow `LAI-01 Calculate Opportunity Score`.
5. Implement governance flow `LAI-02 Route Governance Review`.
6. Implement document flow `LAI-03 Process Legal Document`.
7. Implement adoption flow `LAI-04 Manage Adoption Feedback`.
8. Configure the Copilot agent and allow only the approved actions.
9. Load synthetic sample records.
10. Execute automated tests and UAT.
11. Export unmanaged source for GitHub and managed package for Test.
12. Validate connection references, environment variables, security roles, audit settings, and ownership after import.

## Production-readiness checklist

- DLP policies reviewed
- Managed environment enabled if required
- Tenant and Dataverse auditing configured
- Retention and legal-hold requirements approved
- AI model and data-processing terms approved
- Accessibility and performance tested
- Monitoring and support ownership assigned
- Business continuity and rollback tested
- User communication and training approved
- Success metrics baselined before launch

