# End-to-End Microsoft Teams Chatbot Blueprint

## Purpose

This blueprint defines how I will extend the published **Policy Response Review Workflow** into a user-facing Microsoft Teams chatbot while preserving and reusing the workflow logic already configured in Copilot Studio.

The target experience is:

1. A user asks a policy question in Teams.
2. A Copilot Studio agent analyzes the inquiry and returns a governed draft.
3. The user chooses whether to submit the draft for human review.
4. A reviewer approves or requests revision.
5. The decision is recorded and can be checked from Teams.
6. No external customer response is sent automatically.

This is the Phase 2 implementation design. The current verified implementation remains the published manual workflow documented in [IMPLEMENTATION-STATUS.md](IMPLEMENTATION-STATUS.md).

## Why the workflow is split

The existing workflow contains a Human Review action that can wait for a person. A conversational tool must return to the agent promptly, so the Teams agent should not wait inside that long-running review step.

I will reuse the current configuration through three components:

| Component | Purpose | Response pattern |
| --- | --- | --- |
| Generate Policy Draft | Validate the Teams inquiry, run the governed Agent and return the structured draft | Synchronous |
| Submit Review Request | Create a durable review record and return a RequestId | Synchronous acknowledgement |
| Process Human Review | Run the existing Human Review, If/Else and approved/revision outcome logic | Asynchronous |
| Get Review Status | Return the latest review state to the Teams conversation | Synchronous |

## End-to-end architecture

~~~mermaid
flowchart TD
    A["User asks question in Teams"] --> B["Copilot Studio conversational agent"]
    B --> C["Generate Policy Draft tool"]
    C --> D["Governed draft returned to Teams"]
    D --> E{"Submit for human review?"}
    E -->|No| F["End with draft marked unapproved"]
    E -->|Yes| G["Submit Review Request tool"]
    G --> H["Create durable review record"]
    H --> I["Return RequestId to Teams"]
    H --> J["Process Human Review"]
    J --> K{"Reviewer decision"}
    K -->|Approve| L["Record ApprovedForRelease"]
    K -->|Revise| M["Record RevisionRequired"]
    N["User asks for status in Teams"] --> O["Get Review Status tool"]
    O --> H
~~~

## Reuse of the current workflow

No existing workflow evidence should be deleted. Preserve the published workflow and create solution-aware copies for the Teams implementation.

| Current node | Reused in Phase 2 |
| --- | --- |
| Manual Start inputs | Become EmailSubject and CustomerInquiry inputs on Generate Policy Draft |
| Governed Agent | Reused in Generate Policy Draft with the same synthetic policy controls |
| Structured Agent response | Returned to Teams as Decision, DraftResponse, PolicyBasis and ReviewNote |
| Human Review | Moved to Process Human Review, triggered after a review record is created |
| ApprovalDecision and ReviewerComments | Stored against the RequestId |
| If/Else approval branch | Reused without changing its decision rule |
| Approved outcome variables | Written as ApprovedForRelease |
| Revision outcome variables | Written as RevisionRequired |

## Component 1: Teams conversational agent

**Display name:** Policy Response Assistant

### Responsibilities

- Receive the user’s inquiry in Microsoft Teams.
- Capture or infer EmailSubject and CustomerInquiry.
- Call Generate Policy Draft.
- Present the structured draft and policy basis.
- Clearly state that the draft is not approved.
- Ask whether the user wants to submit it for human review.
- Call Submit Review Request only after confirmation.
- Return the RequestId and explain how to check status.
- Never send an external customer email.

### Suggested agent instructions

Use the governed policy instructions from [copilot-agent-instructions.md](copilot-agent-instructions.md) and add:

> When a user asks a policy question, call Generate Policy Draft. Present the returned draft as unapproved. Ask for explicit confirmation before calling Submit Review Request. After submission, return the RequestId and state that the response remains unsent until human approval. When the user asks about an existing request, call Get Review Status. Do not claim that approval, revision or dispatch occurred unless the corresponding tool returns that state.

## Component 2: Generate Policy Draft

### Trigger and response

- Trigger: **When an agent calls the flow**
- Required inputs:
  - EmailSubject
  - CustomerInquiry
- Required outputs:
  - Decision
  - DraftResponse
  - PolicyBasis
  - ReviewNote
  - SafeToSubmit
  - ErrorCode

### Processing

1. Validate that EmailSubject and CustomerInquiry are present.
2. Generate a CorrelationId.
3. Treat both values as untrusted user content.
4. Run the existing governed Agent instructions.
5. Validate that every required output section is present.
6. Set SafeToSubmit to false for missing policy basis, unsafe content or technical failure.
7. Use **Respond to the agent** to return the structured result.

## Component 3: Submit Review Request

### Trigger and response

- Trigger: **When an agent calls the flow**
- Inputs:
  - CorrelationId
  - EmailSubject
  - CustomerInquiry
  - DraftResponse
  - PolicyBasis
  - ReviewNote
- Outputs:
  - RequestId
  - SubmissionStatus
  - UserMessage

### Processing

1. Validate the structured draft.
2. Check for an existing request using CorrelationId.
3. Create a durable record with status QueuedForReview.
4. Return RequestId and a safe acknowledgement to Teams.
5. Do not wait for reviewer action inside the conversational call.

## Component 4: Process Human Review

This component reuses the existing Human Review path.

### Trigger

A new review record with status QueuedForReview.

### Processing

1. Load the inquiry, draft, policy basis and review note by RequestId.
2. Send Human Review to the approved Outlook or Teams reviewer channel.
3. Capture ApprovalDecision and ReviewerComments.
4. Apply the existing If/Else rule.
5. If Yes, record ApprovedForRelease.
6. Otherwise, record RevisionRequired.
7. Store reviewer identity and timestamps.
8. Do not send an external customer email.

## Component 5: Get Review Status

- Trigger: **When an agent calls the flow**
- Input: RequestId
- Outputs:
  - ReviewStatus
  - ReviewerComments
  - LastUpdated
  - UserMessage

The tool must return only records the signed-in user is authorized to access.

## Review record

| Field | Purpose |
| --- | --- |
| RequestId | User-facing tracking identifier |
| CorrelationId | End-to-end diagnostic identifier |
| RequestedBy | Signed-in Teams user |
| EmailSubject | Inquiry context |
| CustomerInquiry | Original untrusted content |
| DraftResponse | AI-generated proposed response |
| PolicyBasis | Cited policy rule |
| ReviewNote | Reviewer guidance |
| ReviewStatus | Drafted, QueuedForReview, AwaitingReview, ApprovedForRelease, RevisionRequired or FailedTechnical |
| ApprovalDecision | Yes or No |
| ReviewerComments | Human decision context |
| CreatedOn / UpdatedOn | Audit timestamps |
| ErrorCode | Redacted operational status |

For a portfolio tenant, use only synthetic content. For an approved pilot, use a governed Dataverse table or SharePoint list with access, retention and audit controls.

## Teams conversation example

**User:** A customer wants to update their postal address. What should I send?

**Assistant:** I prepared a policy-grounded draft. It is not approved and has not been sent.

**Assistant:**  
Decision: Draft  
Draft response: [controlled response]  
Policy basis: Customer Identity Verification Policy  
Review note: Verify the permitted identity-check information.

**Assistant:** Would you like me to submit this draft for human review?

**User:** Yes.

**Assistant:** Submitted for review. Request ID: PR-2026-00124. No customer message will be sent automatically. Ask “check PR-2026-00124” for the latest status.

## Failure behavior

| Failure | Teams response | Workflow action |
| --- | --- | --- |
| Missing inquiry | Ask the user to provide the missing information | Do not call the Agent |
| Unsafe or unsupported draft | State that specialist review is required | SafeToSubmit = false |
| Drafting service unavailable | State that a draft could not be generated | Log FailedTechnical |
| Duplicate submission | Return the existing RequestId | Do not create another review |
| Review notification failure | State that submission is pending manual handling | Keep item unsent and alert owner |
| Reviewer timeout | State that the request remains pending | Escalate without inferring approval |
| Status record unavailable | State that status cannot be confirmed | Do not invent a decision |
| Capacity or licensing failure | Direct user to the manual process | Log FailedCapacity |

## Security and governance

- Publish the agent only to authorized Teams users.
- Use Microsoft Entra ID identity and least privilege.
- Enforce matter or policy access at the source.
- Disable unrestricted web search.
- Do not expose hidden instructions or unrelated records.
- Store reviewer decisions and configuration versions.
- Use synthetic data until the required business, legal, privacy, security, records and platform approvals are complete.
- Keep external customer dispatch out of scope until approval callbacks, audit and exception handling are fully tested.

## Implementation sequence

1. Obtain Copilot Studio agent creation permission and approved capacity.
2. Preserve the current published workflow as implementation evidence.
3. Create the Policy Response Assistant conversational agent.
4. Create Generate Policy Draft with When an agent calls the flow and Respond to the agent.
5. Reuse the existing Agent instructions and synthetic policies.
6. Create the durable review record.
7. Create Submit Review Request.
8. Copy the existing Human Review, If/Else and outcome logic into Process Human Review.
9. Create Get Review Status.
10. Add the three synchronous flows as tools to the conversational agent.
11. Test in the Copilot Studio chat panel.
12. Publish the agent.
13. Add the Teams and Microsoft 365 Copilot channel.
14. Install the agent in Teams and complete the UAT pack.
15. Capture redacted evidence and update IMPLEMENTATION-STATUS.md.

## UAT acceptance criteria

The Teams-chatbot phase is complete only when evidence shows:

- a Teams message invokes the agent;
- the agent returns all required draft sections;
- the draft is labelled unapproved;
- explicit user confirmation is required before review submission;
- a unique RequestId is returned;
- Human Review receives the correct request;
- approval and revision both update the durable status;
- the Teams agent returns the correct status by RequestId;
- duplicate submissions are reconciled;
- unsupported, injection-style and unsafe requests fail safely;
- unavailable connectors, credits and notifications leave the item unsent;
- no external customer email is dispatched.

## Microsoft references

- [Call an agent flow from an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-use-flow)
- [Create an agent flow as a tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow-create)
- [Connect and configure an agent for Teams and Microsoft 365](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- [Modify an existing flow to use with an agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-modify-use-with-agent)
- [Power Automate limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config)
