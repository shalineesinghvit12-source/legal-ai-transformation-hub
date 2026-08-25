# Evidence Register

This folder distinguishes verified delivery evidence from planned evidence. Do not use mock screens or design diagrams as proof of a live implementation.

| ID | Evidence | Status | Acceptance condition |
| --- | --- | --- | --- |
| E01 | Requirements and acceptance criteria | Complete | Reviewed in `business-requirements.md` |
| E02 | Copilot Studio instructions | Complete | Instructions stored and versioned |
| E03 | Power Automate workflow blueprint | Complete | Actions, mappings and exceptions documented |
| E04 | Teams Adaptive Card template | Complete | JSON validates successfully |
| E05 | Synthetic test pack | Complete | Policies and test cases contain no real data |
| E06 | Governed policy context | Complete | Synthetic policies embedded in the Agent instructions because tenant knowledge options were restricted |
| E07 | Published Copilot Studio workflow | Complete | See `screenshots/01-published-copilot-workflow.png` |
| E08 | Workflow orchestration | Complete (design) | Published flow shows trigger, AI Agent, Human Review, approval condition and outcome branches |
| E09 | Human-review execution | Partial | Outlook review form delivered; callback failed under tenant restrictions, so no success screenshot is claimed |
| E10 | SharePoint audit-record screenshot | Pending | Correlation ID, reviewer, decision and timestamps visible |
| E11 | Executed UAT scorecard | Pending | Results reviewed and signed by pilot owner |
| E12 | Demonstration recording | Pending | End-to-end synthetic scenario completed |
| E13 | Exported solution package | Pending | Tenant export contains no secrets or personal data |

## Verified implementation evidence

![Published Copilot Studio policy response workflow](screenshots/01-published-copilot-workflow.png)

**E07 - Published workflow:** Copilot Studio shows the published low-code workflow with manual test inputs, a governed AI Agent, Human Review, an approval decision, and separate approved/revision outcome records.

**Validation status:** The Agent node produced a policy-grounded draft in a successful node test. The Human Review request rendered in Outlook, but its response callback returned HTTP 400; Teams delivery returned a tenant-side notification error. A complete workflow run was also blocked because the DePaul environment had no available Copilot Credits. These constraints are recorded transparently and are not represented as successful end-to-end execution.

## Screenshot standards

- Use PNG format and crop to the relevant interface.
- Redact tenant URLs, email addresses and identifiers.
- Add a short caption stating what the image proves.
- Do not show real client, employee, matter or privileged data.
- Do not mark an item complete until another person can reproduce the result.
