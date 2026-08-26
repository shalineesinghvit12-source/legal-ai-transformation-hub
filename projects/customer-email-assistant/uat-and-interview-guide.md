# UAT and interview guide

## Evidence-based test status

| ID | Test | Status | Evidence or result |
| --- | --- | --- | --- |
| UAT-01 | Workflow validation and publication | Passed | Published workflow screenshot |
| UAT-02 | Supported address-update inquiry | Passed | Safe draft, policy basis, and review note returned |
| UAT-03 | Human Review request delivery | Partial | Outlook form rendered with Yes/No and comments |
| UAT-04 | Human Review callback | Blocked | Tenant endpoint returned HTTP 400 |
| UAT-05 | Teams notification | Blocked | HumanInTheLoopNotificationFailed / 502 |
| UAT-06 | Complete workflow run | Blocked | Environment had no available Copilot Credits |
| UAT-07 | Approval branch execution | Not executed | Depends on successful callback and credits |
| UAT-08 | Revision branch execution | Not executed | Depends on successful callback and credits |
| UAT-09 | Prompt injection | Planned | Execute after capacity is available |
| UAT-10 | Missing/conflicting policy | Planned | Execute after capacity is available |

The full production UAT catalogue is retained as a roadmap; only results supported by screenshots or platform errors are marked passed or partial.

## 60-second interview explanation

I built and published a low-code policy-response workflow in Microsoft Copilot Studio. Two manual inputs feed a governed Agent that uses embedded synthetic policies, treats the inquiry as untrusted content, and returns a draft, policy basis, and reviewer note. The workflow then creates a Human Review request, evaluates a Yes/No approval decision, and records separate approved or revision outcomes with reviewer comments. I validated the Agent node and confirmed that the Outlook review form was delivered. The tenant then blocked the callback and complete run through connector and Copilot Credit constraints. I documented those failures instead of claiming end-to-end completion, and defined the production roadmap for managed knowledge, durable audit storage, monitoring, environment promotion, and full UAT.

## Interview questions and answers

### What did you personally implement?

I configured and published the Copilot Studio Workflow, defined the two trigger inputs, wrote the Agent instructions and synthetic policies, configured Human Review, built the approval condition, added separate outcome variables, tested the Agent, and maintained the evidence and governance documentation.

### Is this a Power Automate project?

The working asset is a **Copilot Studio Workflow** that uses Microsoft’s low-code workflow and Human Review capabilities. Power Automate is documented as the target production orchestration option for mailbox triggers, durable records, notifications, retries, and downstream actions; it is not represented as an executed cloud flow.

### Did you implement RAG or a vector database?

No. The validated build uses inline governed synthetic policy context because the tenant did not provide an approved file-upload or SharePoint knowledge source. The production design proposes managed knowledge and retrieval after governance and access approval.

### How do you reduce hallucination and prompt-injection risk?

The Agent may rely only on the embedded policy set, must identify its policy basis, must state when support is absent, treats the customer inquiry as untrusted data, escalates high-risk topics, and never sends a response autonomously.

### Why is Human Review mandatory?

External communication can create privacy, legal, operational, and reputational risk. Human Review preserves accountability and provides an explicit decision and reviewer-comment trail before any future outbound action.

### What did the failed callback teach you?

A rendered approval form is not proof of a completed workflow. Production readiness requires callback validation, service health, licensing and capacity checks, timeout and retry behavior, support ownership, and test evidence across both branches.

### How does this demonstrate AI transformation?

The work covers use-case selection, requirements, process redesign, low-code configuration, responsible-AI controls, stakeholder ownership, UAT, evidence management, constraint diagnosis, and a staged production roadmap—not only prompt writing.

### What would you do next?

Secure approved capacity; move policies to a managed knowledge source; repair or replace the Human Review callback; add correlation IDs and durable audit records; configure monitoring and exception handling; package the solution; promote through controlled environments; and execute full UAT with business, legal, privacy, security, records, architecture, and platform owners.

## Evidence-safe resume bullets

- Built and published a governed Microsoft Copilot Studio Workflow for policy-response drafting with mandatory Human Review and approval branching.
- Designed prompt-injection, escalation, data-minimization, and no-autonomous-send controls using synthetic policy content.
- Validated Agent-node output and Human Review request delivery; documented tenant credit and notification dependencies that blocked complete execution.
- Produced requirements, RACI, risk controls, UAT artefacts, evidence, and a staged production roadmap for a low-code AI pilot.

Do not claim production deployment, end-to-end completion, a SharePoint knowledge connection, a Power Automate cloud-flow run, customer-email dispatch, or measured time savings until evidence exists.
