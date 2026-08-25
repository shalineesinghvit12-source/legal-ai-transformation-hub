# Business requirements document

## Business problem

Customer-support staff spend time locating approved policy language, drafting repetitive replies, and obtaining informal review. Responses can vary, knowledge may be outdated, and decision evidence is difficult to reconstruct.

## Objective

Provide policy-grounded draft responses for selected low-risk customer inquiries while preserving mandatory human approval, source control, auditability, and a measurable adoption process.

## Stakeholders

| Role | Responsibility |
| --- | --- |
| Business sponsor | Owns outcome and pilot decision |
| Process owner | Defines scope, service levels, and exceptions |
| Policy or knowledge owner | Approves documents and retirement dates |
| Reviewer | Edits and approves or rejects every draft |
| Security and privacy | Approve data, access, retention, and connector controls |
| Power Platform owner | Owns environment, connections, support, and deployment |
| Change and learning lead | Training, communications, feedback, and adoption |

## In scope

- Synthetic policy documents and customer inquiries
- One approved mailbox folder
- English-language text emails
- Policy-grounded draft generation
- Teams human review and editing
- Approved reply dispatch
- SharePoint audit logging
- UAT, training, feedback, and pilot measurement

## Out of scope

- Legal advice or legal conclusions
- Automatic sending without human approval
- Client, matter, privileged, or regulated production data
- Attachment analysis
- Sentiment-based automated decisions
- Power BI
- iManage, Intapp, or Litera production integration
- Multilingual production support

## Functional requirements

| ID | Requirement |
| --- | --- |
| FR-01 | The flow shall start only for a message in the approved mailbox or folder. |
| FR-02 | The system shall convert the message to plain text and create a correlation ID. |
| FR-03 | The system shall record receipt before invoking the agent. |
| FR-04 | The agent shall use only approved SharePoint policy knowledge. |
| FR-05 | The agent shall not follow instructions embedded in customer email content. |
| FR-06 | The agent shall clearly state when approved information is insufficient. |
| FR-07 | The flow shall present the source inquiry and editable draft to a reviewer. |
| FR-08 | The flow shall not send a response until the reviewer approves it. |
| FR-09 | A rejected response shall not be sent. |
| FR-10 | The system shall record the AI draft, final response, reviewer, decision, and timestamps. |
| FR-11 | Terminal failures shall enter a visible support queue. |
| FR-12 | Duplicate trigger events shall not create duplicate replies. |

## Nonfunctional requirements

- Least-privilege access
- Synthetic data during portfolio development
- Human accountability for every outbound reply
- Traceable knowledge ownership and document lifecycle
- Recoverable failure handling
- Accessible Teams review experience
- Clear separation of proposed, targeted, and validated benefits
- Environment-specific connections excluded from source control

## Pilot measures

| Measure | Definition |
| --- | --- |
| Review cycle time | Time from email receipt to reviewer decision |
| Draft acceptance rate | Approved drafts divided by reviewed drafts |
| Edit rate | Approved drafts materially edited by reviewer |
| Unsupported-answer rate | Inquiries where sufficient approved knowledge was unavailable |
| Automation success rate | Completed flow runs divided by eligible messages |
| Reviewer confidence | Post-review survey rating from 1 to 5 |
| Rework incidents | Incorrect or duplicate outbound messages |

Targets must be labeled as targets. Resume claims require measured pilot evidence and sponsor validation.

## Acceptance criteria

1. Supported inquiries produce a relevant draft based on active policy content.
2. Missing policy information produces an explicit escalation, not an invented answer.
3. No response is sent without human approval.
4. A reviewer can edit the draft before approval.
5. Rejection prevents dispatch.
6. Every processed message has an auditable correlation ID.
7. Duplicate processing is prevented or safely reconciled.
8. Unauthorized users cannot access the knowledge library or review list.
9. All UAT priority-one scenarios pass.
10. Actual benefits are not claimed until measured.

