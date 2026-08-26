# Governed AI Policy Response Assistant

A low-code Microsoft Copilot Studio portfolio prototype for drafting policy-grounded responses, requiring human review, branching on an approval decision, and retaining reviewer outcome data.

## What was actually implemented

The live tenant build uses **Copilot Studio Workflows**, not a separately created Power Automate cloud flow.

~~~mermaid
flowchart LR
    A["Manual Start<br/>EmailSubject + CustomerInquiry"] --> B["Agent<br/>governed instructions + inline policies"]
    B --> C["Human Review<br/>Outlook/Teams channel"]
    C --> D{"ApprovalDecision = Yes?"}
    D -->|Yes| E["ApprovedStatus<br/>ApprovedForRelease"]
    D -->|Else| F["RejectedStatus<br/>RevisionRequired"]
~~~

| Capability | Status | Evidence |
| --- | --- | --- |
| Workflow configured and published | Complete | [Workflow screenshot](evidence/screenshots/01-published-copilot-workflow.png) |
| Governed Agent instructions | Complete | [Agent instructions](copilot-agent-instructions.md) |
| Routine policy question | Passed | [Agent test screenshot](evidence/screenshots/02-agent-node-test-passed.png) |
| Outlook Human Review request | Delivered and rendered | [Redacted request](evidence/screenshots/03-human-review-request-delivered-redacted.png) |
| Approval callback | Blocked | Tenant returned HTTP 400 |
| Teams notification | Blocked | Tenant returned HumanInTheLoopNotificationFailed |
| Complete workflow run | Blocked | No Copilot Credits were available |
| Production exception handling | Designed | [Resilience design](exception-handling.md) |
| End-to-end UAT | Not complete | [UAT scorecard](evidence/uat-scorecard.md) |

## Why the prototype is governed

- The customer inquiry is explicitly treated as untrusted input.
- The Agent uses only the three embedded synthetic policies.
- Missing or ambiguous policy support requires escalation.
- The Agent cannot provide legal advice, admit liability, promise compensation, or disclose restricted information.
- Privacy, litigation, fraud, security, discrimination, and prompt-injection cases require human review.
- The workflow contains no automatic customer-email action.
- Reviewer approval and comments are modeled explicitly.
- Approved and revision outcomes are recorded separately.
- The target failure design is fail closed: no error is allowed to imply approval or trigger an outbound send.

## Knowledge approach

The tenant exposed only SharePoint and organization-owned public websites as managed knowledge sources. Direct local-file upload was unavailable, and the project owner did not have an approved SharePoint repository. For the working prototype, the three short synthetic policies were embedded directly in the Agent instructions.

This is an **inline governed-context prototype**, not a vector-search or RAG implementation. The production design would move approved policy content to an organization-managed knowledge source with access controls, lifecycle metadata, and auditability.

## Exception handling

The current published canvas validates the decision path, not the complete failure path. Observed HTTP 400, notification, and credit failures are recorded as blocked evidence.

The [exception-handling design](exception-handling.md) specifies input validation, correlation IDs, bounded retries, Try/Catch/Finally Scopes, Run after conditions, timeouts, escalation, durable error logging, duplicate prevention, alerts, and explicit terminal states. Until that design is implemented and tested, the system must fail closed and use the manual process.

## Repository guide

| File | Purpose |
| --- | --- |
| [IMPLEMENTATION-STATUS.md](IMPLEMENTATION-STATUS.md) | Authoritative record of what was implemented, tested, and blocked |
| [portfolio-case-study.md](portfolio-case-study.md) | Interview-ready business and delivery narrative |
| [Governed_AI_Policy_Response_Assistant_Case_Study.pdf](Governed_AI_Policy_Response_Assistant_Case_Study.pdf) | One-page technical-team case study |
| [business-requirements.md](business-requirements.md) | Scope, stakeholders, requirements, and acceptance criteria |
| [copilot-agent-instructions.md](copilot-agent-instructions.md) | Implemented Agent instructions and inline policy context |
| [exception-handling.md](exception-handling.md) | Failure matrix and production resilience design |
| [governance-and-controls.md](governance-and-controls.md) | Risk register, RACI, operating controls, and go-live gates |
| [evidence/README.md](evidence/README.md) | Verified screenshots and evidence status |
| [evidence/uat-scorecard.md](evidence/uat-scorecard.md) | Executed and blocked test results |
| [samples/](samples/) | Synthetic policies and inquiries |
| [power-automate-flow.md](power-automate-flow.md) | Target production orchestration blueprint |
| [final-no-sharepoint-implementation-guide.md](final-no-sharepoint-implementation-guide.md) | Alternative target build guide; not the live tenant result |

## Technical discussion points

- **Why human review?** Policy and customer communications can create legal, privacy, and reputational risk. The design keeps the AI in a drafting role.
- **Why inline policies?** It was the safest feasible option under the tenant's restricted knowledge choices. The limitation is recorded rather than hidden.
- **Why no automatic send?** The approval callback could not be validated; adding an outbound action would create an unsafe and untested path.
- **What happens when something fails?** The production design fails closed, records the error with a correlation ID, alerts an owner, and moves the item to manual handling. It never assumes approval.
- **Why preserve blocked evidence?** Transformation work includes identifying platform, licensing, DLP, and operating constraints. Clear escalation is better than overstating completion.
- **How would production differ?** Managed knowledge, role-based access, standard approvals, audit storage, exception handling, monitoring, solution packaging, environment promotion, and completed UAT.

## Data policy

Only synthetic policy documents and synthetic inquiries are included. No client, employee, matter, privileged, confidential, production-mailbox, or credential data belongs in this repository.
