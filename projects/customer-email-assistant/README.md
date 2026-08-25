# Governed AI Policy Response Assistant

A low-code Microsoft Copilot Studio and Power Automate pilot for drafting policy-grounded email responses, routing every draft through a human reviewer, and retaining an auditable decision record.

## Portfolio objective

Demonstrate how a business analyst can take an AI opportunity from discovery through requirements, process redesign, governance, low-code solution design, UAT and adoption planning. The MVP deliberately excludes Power BI, Power Apps, Dataverse and custom code.

## Target process

1. An email arrives in an approved shared mailbox.
2. Power Automate converts the email body to plain text and creates a correlation ID.
3. Power Automate calls a published Copilot Studio agent using **Execute Agent and wait**.
4. The agent grounds its draft in the approved SharePoint policy library.
5. Power Automate posts the inquiry and draft to a Teams Adaptive Card.
6. A reviewer edits the draft and selects Approve or Reject.
7. Only an approved human-edited response is sent.
8. SharePoint records the source message, draft, final response, reviewer, decision, timestamps, and exception state.

## Important platform clarification

SharePoint knowledge in Copilot Studio is configured as a managed knowledge source and uses Microsoft Graph Search while respecting the agent user's permissions. This project does not claim that the business analyst creates or administers a separate Azure AI Search vector database.

## Project files

| File | Purpose |
| --- | --- |
| `implementation-guide.md` | Click-by-click tenant build sequence |
| `tenant-implementation-and-evidence-guide.md` | Practical MVP build, troubleshooting and proof-capture checklist |
| `final-no-sharepoint-implementation-guide.md` | Final end-to-end build using local file upload and OneDrive Excel |
| `business-requirements.md` | BA-ready scope, requirements, controls, and acceptance criteria |
| `sharepoint-design.md` | Policy library and audit-list configuration |
| `copilot-agent-instructions.md` | Governed instructions to paste into Copilot Studio |
| `power-automate-flow.md` | Flow actions, mappings, exception paths, and test notes |
| `adaptive-card.json` | Editable Teams human-review card |
| `uat-and-interview-guide.md` | UAT scenarios, demonstration plan, interview answers, and resume wording |
| `portfolio-case-study.md` | Concise business case for recruiters and hiring managers |
| `Governed_AI_Policy_Response_Assistant_Case_Study.pdf` | One-page recruiter-ready case study |
| `governance-and-controls.md` | Risk register, RACI and operational controls |
| `demo-script.md` | Five-minute demonstration and evidence-capture sequence |
| `samples/` | Synthetic policies and test inquiries |
| `evidence/` | UAT scorecard and evidence register |

## Honest delivery status

| Component | Status |
| --- | --- |
| Business requirements and control design | Complete |
| Copilot Studio instructions | Build-ready |
| Power Automate workflow specification | Build-ready |
| Teams Adaptive Card | Build-ready template |
| SharePoint structure | Build-ready |
| Tenant connections and published agent | Requires Microsoft tenant |
| Live end-to-end results | Not claimed until UAT is executed |

## Data policy

Use synthetic policy files and synthetic customer emails for portfolio development. Do not upload client, employee, matter, privileged, confidential, or production mailbox content to a personal demonstration environment.

## Official Microsoft references

- [Add SharePoint as Copilot Studio knowledge](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-sharepoint)
- [Copilot Studio knowledge sources](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio)
- [Call a Copilot Studio agent from Power Automate](https://learn.microsoft.com/en-us/power-automate/call-copilot-studio-agent)
- [Trigger a flow when email arrives](https://learn.microsoft.com/en-us/power-automate/email-triggers)
- [Create Teams Adaptive Card flows](https://learn.microsoft.com/en-us/power-automate/create-adaptive-cards)
