# Business requirements document

> [!NOTE]
> **Requirements baseline and production target.** This document defines the intended pilot controls and acceptance criteria. The currently validated portfolio build is a published Copilot Studio Workflow using manual inputs, inline synthetic policy context, Human Review, approval branching, and outcome variables. See [IMPLEMENTATION-STATUS.md](IMPLEMENTATION-STATUS.md) for evidence and tenant limitations.

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

## In scope for a production pilot

- Synthetic policy documents and customer inquiries
- One approved mailbox folder
- English-language text emails
- Policy-grounded draft generation
- Human review and editing
- Approved reply dispatch
- Durable audit logging
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
| FR-01 | The workflow shall start only from an approved trigger. |
| FR-02 | The system shall normalize the message and create a correlation ID. |
| FR-03 | The system shall record receipt before invoking the agent. |
| FR-04 | The agent shall use only approved policy knowledge. |
| FR-05 | The agent shall not follow instructions embedded in customer content. |
| FR-06 | The agent shall clearly state when approved information is insufficient. |
| FR-07 | The workflow shall present the source inquiry and draft to a reviewer. |
| FR-08 | The workflow shall not send a response until the reviewer approves it. |
| FR-09 | A rejected response shall not be sent. |
| FR-10 | The system shall record the AI draft, final response, reviewer, decision, and timestamps. |
| FR-11 | Terminal failures shall enter a visible support queue. |
| FR-12 | Duplicate trigger events shall not create duplicate replies. |
| FR-13 | An authorized user shall be able to submit a policy inquiry through Microsoft Teams. |
| FR-14 | The conversational agent shall return the draft without waiting for the human-review decision. |
| FR-15 | The draft shall be labelled unapproved and unsent. |
| FR-16 | The agent shall obtain explicit user confirmation before creating a review request. |
| FR-17 | Each submitted review shall receive a unique RequestId. |
| FR-18 | The existing Human Review, approval condition and outcome logic shall process the queued request asynchronously. |
| FR-19 | An authorized user shall be able to retrieve review status by RequestId from Teams. |
| FR-20 | The agent shall not report approval or revision unless the durable review record contains that state. |

## Nonfunctional requirements

- Least-privilege access
- Synthetic data during portfolio development
- Human accountability for every outbound reply
- Traceable knowledge ownership and document lifecycle
- Recoverable failure handling
- Accessible review experience
- Clear separation of proposed, targeted, and validated benefits
- Environment-specific connections excluded from source control

## Pilot measures

| Measure | Definition |
| --- | --- |
| Review cycle time | Time from receipt to reviewer decision |
| Draft acceptance rate | Approved drafts divided by reviewed drafts |
| Edit rate | Approved drafts materially edited by reviewer |
| Unsupported-answer rate | Inquiries where sufficient approved knowledge was unavailable |
| Automation success rate | Completed runs divided by eligible messages |
| Reviewer confidence | Post-review survey rating from 1 to 5 |
| Rework incidents | Incorrect or duplicate outbound messages |

Targets must be labeled as targets. Resume claims require measured pilot evidence and sponsor validation.

## Acceptance criteria

1. Supported inquiries produce a relevant draft based on active policy content.
2. Missing policy information produces an explicit escalation, not an invented answer.
3. No response is sent without human approval.
4. A reviewer can assess the draft before approval.
5. Rejection prevents dispatch.
6. Every processed message has an auditable correlation ID.
7. Duplicate processing is prevented or safely reconciled.
8. Unauthorized users cannot access knowledge or review records.
9. All priority-one UAT scenarios pass.
10. Actual benefits are not claimed until measured.
11. A Teams message can invoke the conversational agent.
12. The chatbot returns the complete draft structure within the synchronous tool-response limit.
13. Human Review does not block the Teams conversation.
14. Approval and revision both update the correct RequestId.
15. Duplicate submissions return the existing RequestId.
16. Status lookup does not expose a request to an unauthorized user.
17. Technical failure leaves the response unsent.
18. The implementation evidence is updated only after the Teams scenarios pass.
