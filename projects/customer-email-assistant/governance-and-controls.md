# Governance and Operating Controls

## Decision ownership

| Role | Accountability |
| --- | --- |
| Business owner | Approves use case, policy scope, pilot measures and go-live decision |
| Policy owner | Confirms that knowledge documents are current and approved |
| AI transformation lead | Owns requirements, process design, delivery plan and benefit tracking |
| Platform administrator | Manages environments, connectors, DLP policy and solution deployment |
| Security and privacy | Reviews data classification, access, retention and incident handling |
| Reviewer | Validates every draft and owns the final response |
| Support team | Monitors failures, exceptions and service performance |

## Risk register

| ID | Risk | Treatment | Evidence |
| --- | --- | --- | --- |
| R1 | Hallucinated or unsupported response | Approved knowledge only, uncertainty instruction and human review | Copilot instructions and UAT-03 |
| R2 | Prompt injection in inbound text | Treat email as untrusted content and test hostile instructions | UAT-08 |
| R3 | Unauthorized knowledge access | Managed knowledge-source permissions, least privilege, and access review | Access review record |
| R4 | Sensitive information exposure | Synthetic pilot data, DLP policy, restricted logs and retention review | Privacy approval |
| R5 | Incorrect message sent externally | Mandatory approval branch; no direct AI-to-email path | Flow screenshot and UAT-06 |
| R6 | Duplicate responses | Internet Message ID duplicate check | UAT-09 |
| R7 | Policy becomes outdated | Owner, status, effective date and review date metadata | Monthly knowledge review |
| R8 | Flow or connector failure | Try/catch/finally scopes, error log and support notification | UAT-10 |
| R9 | Overstated benefits | Baseline first; report observed results with sample size | Pilot scorecard |

## Go-live gates

The pilot cannot proceed to production until:

1. Business, policy, security, privacy and platform owners approve the scope.
2. Knowledge documents and permissions are reviewed.
3. All critical UAT scenarios pass with evidence.
4. No send-without-approval route exists.
5. Monitoring, ownership, incident handling and rollback are documented.
6. Retention and deletion requirements are approved.
7. Training and reviewer guidance are completed.

## Feedback loop

Reviewer edits are sampled weekly during the pilot. The team classifies corrections as missing knowledge, outdated policy, retrieval failure, drafting quality, routing error or reviewer preference. Only approved knowledge and instruction changes are released, retested and recorded.
