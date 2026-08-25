# User acceptance testing

| ID | Scenario | Expected result |
| --- | --- | --- |
| UAT-01 | Submit complete opportunity through Copilot | Opportunity created with all mandatory fields |
| UAT-02 | Omit business sponsor | Agent requests missing sponsor before creation |
| UAT-03 | Submit duplicate opportunity | Possible duplicate shown to portfolio manager |
| UAT-04 | Score high-value, low-effort proposal | Reproducible score and Quick Win recommendation |
| UAT-05 | Set risk to Critical | Governance review required regardless of score |
| UAT-06 | Governance reviewer requests changes | Submitter receives request and record remains pending |
| UAT-07 | Upload unsupported executable | File rejected and safe audit event recorded |
| UAT-08 | Upload synthetic agreement | Structured fields and summary produced |
| UAT-09 | Extraction confidence below threshold | Human review task created |
| UAT-10 | Reviewer corrects extracted date | Before/after values and rationale stored |
| UAT-11 | Prompt-injection text embedded in document | Document instruction ignored and event flagged |
| UAT-12 | Unauthorized user opens privileged record | Access denied and security event available to admins |
| UAT-13 | AI action fails or times out | Retry policy executes then creates support incident |
| UAT-14 | User submits negative feedback | Improvement action assigned to product owner |
| UAT-15 | Dashboard refreshes | Portfolio totals reconcile with Dataverse source |

