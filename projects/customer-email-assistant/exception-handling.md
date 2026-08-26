# Exception handling and operational resilience

## Current position

The published prototype implements the governed business path:

**Start → Agent → Human Review → Approval decision → Approved or Revision outcome**

It does **not** yet implement production-grade technical exception handling. That gap is intentional and recorded, not hidden. The observed failures, including unavailable Copilot Credits, Human Review callback HTTP 400, and Teams notification failure, are treated as engineering evidence for the next iteration.

## Safety principle

The workflow must **fail closed**. If drafting, review, notification, persistence, or approval fails, no external response is sent. The item moves to a visible manual-review or support state with a correlation ID and diagnostic record.

## Failure matrix

| Failure point | Detection | Automated response | Business outcome |
| --- | --- | --- | --- |
| Invalid or empty input | Required-field validation | Stop before Agent call | Return InvalidInput |
| Agent timeout or service error | Failed/timed-out Agent action | Exponential retry for transient errors, then Catch | Queue for manual drafting |
| Unsupported or unsafe Agent output | Output and policy-basis validation | Do not continue to release path | Route to Human Review or specialist queue |
| Human Review notification failure | Failed/timed-out review action | Retry notification; use alternate approved channel if configured | Keep status ReviewNotificationFailed |
| Reviewer timeout | Review deadline exceeded | Remind once, then escalate | Keep item unsent |
| Approval callback failure | Failed callback or missing decision | Record error; require manual reconciliation | Keep item unsent |
| Audit-store failure | Failed write | Retry; write to fallback operational log | Block release until durable record exists |
| Outbound-send failure | Failed email action | Retry only when idempotency is guaranteed | Queue for support; prevent duplicate send |
| Licensing or credit exhaustion | Platform error / capacity monitoring | Stop Agent execution and alert owner | Manual process remains active |
| Broken connection or permission | Connector failure | Alert platform owner; disable unsafe path | Manual process remains active |
| Duplicate event | Existing correlation or message ID | Ignore or reconcile duplicate | Prevent duplicate review and reply |

## Target Power Automate pattern

Microsoft recommends Run after, Scopes, retry policies, logging, notifications, and Terminate for robust flow error handling.

### 1. Initialize operational fields

Create these variables at the start:

| Variable | Type | Purpose |
| --- | --- | --- |
| CorrelationId | String | Trace one inquiry across every action |
| ProcessStatus | String | Current business state |
| FailedAction | String | Action or scope that failed |
| ErrorCode | String | Connector or platform error code |
| ErrorMessage | String | Redacted diagnostic message |
| RetryCount | Integer | Controlled retry evidence |
| MessageId | String | Duplicate prevention |

### 2. Use three Scopes

- **TRY – Process inquiry:** validate input, create audit record, call Agent, validate output, create Human Review, evaluate decision, and perform the permitted business action.
- **CATCH – Record and notify:** configure **Run after** for has failed, has timed out, and is skipped; capture the failed action using workflow results; update status; write a redacted error record; notify the support owner; then terminate as failed.
- **FINALLY – Close run:** configure **Run after** for success or failure; write end time, duration, final state, and correlation ID.

### 3. Configure retries selectively

Use exponential retry only for transient network, throttling, and service-unavailability errors. Do not retry invalid input, denied permissions, unsafe AI output, or a business rejection. Outbound email retry requires an idempotency check using MessageId and the audit record.

### 4. Add timeouts and escalation

Set a review deadline. If no decision arrives, send one reminder and escalate to the process owner. The workflow remains in AwaitingHumanReview or ReviewTimedOut; it must never infer approval.

### 5. Terminate accurately

Use Terminate with an explicit status so failed runs do not appear successful. Recommended terminal states:

- Succeeded
- RevisionRequired
- ManualReviewRequired
- FailedTechnical
- FailedCapacity
- CancelledDuplicate

## Copilot Studio prototype improvements

Within the current prototype, add the following when tenant capacity permits:

1. Validate that EmailSubject and CustomerInquiry are not blank.
2. Add a classification output such as SafeToReview, Escalate, or InsufficientPolicyBasis.
3. Route unsafe or unsupported output directly to a specialist Human Review path.
4. Add a reviewer timeout branch and a visible status variable.
5. Store error code, error message, correlation ID, decision, reviewer comments, and timestamps in a durable approved data source.
6. Retest both approval branches, callback behavior, unavailable credits, notification failure, and duplicate submission.

## Monitoring and ownership

| Control | Owner | Minimum evidence |
| --- | --- | --- |
| Failed-run alert | Power Platform support | Alert with correlation ID and failed scope |
| Daily exception queue | Process owner | Open items by age and status |
| Capacity monitoring | Platform owner | Credit threshold and exhaustion alert |
| Connection health | Platform owner | Broken-connection notification |
| Monthly control review | Business, legal, privacy, security | Failure trends, unsafe outputs, overrides, and corrective actions |

Do not place customer content, credentials, access tokens, or sensitive connector payloads in failure notifications or GitHub evidence.

## Validation criteria

Exception handling is complete only when evidence shows:

- every injected failure enters the expected Catch path;
- no failure can reach an outbound-send action;
- a durable error record contains correlation ID, time, state, and redacted diagnostic details;
- transient retries are bounded;
- duplicate runs do not create duplicate responses;
- reviewer timeout and escalation work;
- support owners can locate and reconcile each failed item;
- both approved and revision paths still pass after resilience changes.

## References

- [Employ robust error handling in Power Automate](https://learn.microsoft.com/en-us/power-automate/guidance/coding-guidelines/error-handling)
- [Troubleshoot a cloud flow](https://learn.microsoft.com/en-us/power-automate/fix-flow-failures)
- [Copilot Studio error codes](https://learn.microsoft.com/en-us/troubleshoot/power-platform/copilot-studio/authoring/error-codes)
