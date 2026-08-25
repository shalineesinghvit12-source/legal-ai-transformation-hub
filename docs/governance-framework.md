# AI governance framework

## Decision gates

| Gate | Owner | Required evidence | Exit criteria |
| --- | --- | --- | --- |
| Triage | AI Transformation Manager | Problem, sponsor, volume, value | Complete intake and duplicate check |
| Feasibility | Technology and Data | Systems, data, integration, effort | Viable architecture and delivery estimate |
| Risk | Legal, Security, Privacy | Data class, privilege, harm, retention | Controls accepted and residual risk recorded |
| Pilot | Product owner and PMO | UAT, evaluation, training, rollback | Pilot approval and named accountable owner |
| Production | Governance forum | Metrics, support model, monitoring | Formal approval with conditions documented |
| Benefits review | Business sponsor | Adoption, accuracy, time, satisfaction | Continue, improve, scale, or retire decision |

## Mandatory controls

1. Use approved, scoped knowledge sources only.
2. Label AI output as draft and potentially incomplete.
3. Require human review when confidence is below 0.85 or a high-risk clause is detected.
4. Store prompt version, model/action version, extracted output, reviewer corrections, and final decision.
5. Prevent unsupported file types and scan uploads using the organization's approved security service.
6. Separate development, test, and production environments.
7. Use environment variables and connection references, never embedded credentials.
8. Apply least privilege to submitters, reviewers, portfolio managers, and administrators.
9. Test prompt injection, data leakage, hallucination, bias, access control, failure recovery, and audit completeness.
10. Define rollback, incident, retention, and user-support procedures before production.

## Confidence policy

| Condition | Action |
| --- | --- |
| Confidence >= 0.90 and no risk indicator | Reviewer sampling permitted during pilot |
| Confidence 0.85-0.89 | Human validation required |
| Confidence < 0.85 | Human validation and correction required |
| High-risk clause, privileged data, or policy violation | Stop processing and route to designated reviewer |
| Unsupported or unreadable document | Reject safely and notify requester |

## Responsible-use notice

The solution supports administrative review and transformation decisions. It does not replace qualified legal judgment. Users remain responsible for verifying all outputs against source documents and applicable firm policy.

