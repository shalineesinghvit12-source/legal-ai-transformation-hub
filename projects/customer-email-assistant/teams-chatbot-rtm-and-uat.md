# Teams Chatbot Traceability and UAT Plan

## Purpose

This document traces the Phase 2 Microsoft Teams chatbot requirements to the designed components, controls, tests and evidence. Test results remain **Not executed** until the required Copilot Studio license, role, capacity and connectors are available.

## Requirements traceability

| Requirement | Designed component | Control | UAT case | Evidence required | Status |
| --- | --- | --- | --- | --- | --- |
| FR-13 Teams inquiry | Policy Response Assistant published to Teams | Authorized channel access | TC-01 | Redacted Teams conversation | Not executed |
| FR-14 Immediate draft | Generate Policy Draft | Respond to the agent before long-running review | TC-02 | Tool run and Teams response | Not executed |
| FR-15 Unapproved label | Agent completion instructions | Mandatory unsent/unapproved wording | TC-03 | Teams draft screenshot | Not executed |
| FR-16 Explicit confirmation | Agent conversation topic | Yes/No confirmation before submission tool | TC-04 | Conversation transcript | Not executed |
| FR-17 Unique RequestId | Submit Review Request | Durable record and correlation check | TC-05 | Redacted record and chat response | Not executed |
| FR-18 Asynchronous review | Process Human Review | Existing Human Review and If/Else logic | TC-06, TC-07 | Approval and revision run history | Not executed |
| FR-19 Status lookup | Get Review Status | RequestId and user authorization | TC-08 | Teams status response | Not executed |
| FR-20 No invented decision | Status tool and agent instruction | State returned only from durable record | TC-09 | Negative-test transcript | Not executed |
| FR-12 Duplicate prevention | Submit Review Request | CorrelationId idempotency check | TC-10 | Duplicate test run | Not executed |
| FR-11 Visible support queue | Exception path | FailedTechnical and FailedCapacity states | TC-11 | Failure record and alert | Not executed |

## UAT cases

| ID | Scenario | Expected result | Priority |
| --- | --- | --- | --- |
| TC-01 | User asks an address-update question in Teams | Agent accepts the inquiry and calls Generate Policy Draft | P1 |
| TC-02 | Supported inquiry is submitted | Decision, DraftResponse, PolicyBasis and ReviewNote return in chat | P1 |
| TC-03 | Draft is displayed | Response clearly states unapproved and unsent | P1 |
| TC-04 | User declines human review | No review record is created | P1 |
| TC-05 | User confirms human review | One RequestId is created and returned promptly | P1 |
| TC-06 | Reviewer selects Yes | Request becomes ApprovedForRelease and comments are retained | P1 |
| TC-07 | Reviewer selects No | Request becomes RevisionRequired and comments are retained | P1 |
| TC-08 | User asks “check [RequestId]” | Correct authorized status and last-updated time appear | P1 |
| TC-09 | Status store is unavailable | Agent states that status cannot be confirmed | P1 |
| TC-10 | Same draft is submitted twice | Existing RequestId is returned; no duplicate review is created | P1 |
| TC-11 | Credits or notification service is unavailable | Item remains unsent and a visible failure status is recorded | P1 |
| TC-12 | Prompt asks the agent to ignore policy instructions | Request is refused or escalated without revealing instructions | P1 |
| TC-13 | User requests a privacy, fraud or litigation conclusion | Neutral acknowledgement and specialist escalation are returned | P1 |
| TC-14 | Unauthorized user checks another request | No request content or decision is disclosed | P1 |
| TC-15 | Reviewer does not respond before deadline | Status remains pending and escalation occurs without inferred approval | P2 |
| TC-16 | Agent or connector times out | Bounded retry and fail-closed response occur | P2 |

## Entry criteria

- Copilot Studio agent creation role is assigned.
- Approved capacity is available.
- Teams publication is permitted.
- The three agent-callable flows are published.
- A durable synthetic review store is configured.
- Review notification connection is healthy.
- Test users and reviewer accounts are authorized.
- Current manual-workflow evidence is preserved.

## Exit criteria

- All P1 cases pass.
- No open critical security, privacy or incorrect-approval defect exists.
- Approval and revision are both demonstrated.
- Duplicate and failure tests leave the item unsent.
- Evidence register and IMPLEMENTATION-STATUS.md are updated.
- Business, platform, security and privacy reviewers approve the portfolio pilot scope.

## Evidence naming

Store only redacted evidence:

1. `04-teams-agent-installed-redacted.png`
2. `05-teams-draft-response-redacted.png`
3. `06-review-request-id-redacted.png`
4. `07-human-review-approved-redacted.png`
5. `08-human-review-revision-redacted.png`
6. `09-teams-status-lookup-redacted.png`
7. `10-fail-closed-test-redacted.png`

Do not mark a requirement Implemented or Passed until its corresponding evidence has been captured and reviewed.
