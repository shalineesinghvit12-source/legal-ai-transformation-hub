# Five-Minute Demonstration Script

## Preparation

- Use only the synthetic policies and inquiries in this repository.
- Confirm that the Copilot agent is published and the flow is turned on.
- Open the SharePoint knowledge library, Outlook test mailbox, Teams review channel and SharePoint audit list.
- Start recording only after checking that no tenant identifiers or unrelated messages are visible.

## Demonstration

### 0:00-0:40 - Business problem

Explain that staff currently search policy documents and manually draft repetitive responses. The pilot aims to reduce drafting effort while keeping a reviewer accountable.

### 0:40-1:20 - Governed knowledge

Show the three synthetic policies in SharePoint. Point out status, owner, effective date, review date, category and confidentiality metadata.

### 1:20-2:10 - Trigger and orchestration

Send test case T01 to the test mailbox. Show the Power Automate run and identify the email trigger, audit-record creation and Copilot action.

### 2:10-3:10 - Human review

Open the Teams Adaptive Card. Show the original inquiry, grounded draft, editable final-response field and Approve/Reject controls. Make a small edit and approve.

### 3:10-4:00 - Auditability

Show the sent email and matching SharePoint audit record, including correlation ID, reviewer, decision, draft, final response and timestamps.

### 4:00-4:40 - Risk scenario

Run T04 or T06. Show that legal threats or hostile prompt instructions are escalated rather than answered automatically.

### 4:40-5:00 - Outcome and next step

Explain the pilot measures and clarify that benefits will be reported after executed UAT, not assumed in advance.

## Evidence to capture

Save redacted screenshots as `01-knowledge-library.png` through `05-audit-record.png`. Add a link to the recording in `evidence/README.md`. Never commit connection strings, tenant IDs, personal data or production messages.
