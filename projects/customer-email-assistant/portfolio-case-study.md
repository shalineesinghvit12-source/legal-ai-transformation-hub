# Portfolio Case Study: Governed AI Policy Response Assistant

## Situation

Business teams frequently search policy material, interpret the applicable rule, draft a response, and obtain informal review. This creates delay, inconsistent wording, and weak evidence of who approved what. Fully autonomous customer communication would introduce unacceptable policy, privacy, and legal risk.

## Objective

Create a low-code prototype that demonstrates policy-grounded drafting while keeping a human accountable for release decisions.

## Implemented prototype

The published Copilot Studio Workflow accepts a synthetic email subject and inquiry, invokes a governed Agent, sends the draft to Human Review, evaluates a Yes/No approval decision, and records either an approved-for-release or revision-required outcome.

The three short synthetic policies were embedded directly in the Agent instructions because the tenant did not provide an approved file-upload or SharePoint knowledge option for this build. This is accurately described as inline governed context, not vector-search RAG.

## My contribution

- framed and prioritized the use case using value, feasibility, and risk
- defined stakeholders, scope, requirements, acceptance criteria, and exceptions
- designed the target and constrained prototype processes
- configured the Copilot Studio Workflow and Agent instructions
- created identity, complaint, privacy, and prompt-injection controls
- implemented Human Review, an approval condition, and outcome recording
- created synthetic policies, test inquiries, governance artifacts, and UAT evidence
- diagnosed licensing, capacity, callback, and managed-notification constraints
- maintained an evidence register that separates passed, partial, blocked, and planned work

## Evidence-based results

- workflow health check: passed
- workflow publication: passed
- routine identity-policy Agent test: passed
- Outlook Human Review request delivery: passed
- approval callback: blocked by tenant HTTP 400 response
- Teams review notification: blocked by tenant managed-service error
- complete workflow execution: blocked by unavailable Copilot Credits

No performance improvement, production readiness, or end-to-end approval is claimed.

## Responsible-AI controls

The Agent treats customer input as untrusted, uses only embedded approved synthetic policy context, refuses unsupported commitments, avoids legal advice, protects restricted information, and escalates legal, privacy, fraud, security, discrimination, and regulatory cases. No automated external-send action was added.

## Production roadmap

A production pilot would require managed policy knowledge, role-based permissions, licensing capacity, validated approval notifications, durable audit storage, correlation IDs, monitoring, exception handling, solution packaging, environment promotion, complete UAT, and formal stakeholder approval.

## Relevance to AI transformation

The work demonstrates use-case discovery, process analysis, Copilot Studio configuration, Microsoft workflow design, responsible-AI governance, stakeholder controls, test strategy, evidence management, platform-constraint diagnosis, and a practical route from prototype to governed pilot.
