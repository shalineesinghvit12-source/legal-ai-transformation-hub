# Governed AI Policy Response Assistant

> A published low-code Copilot Studio workflow demonstrating policy-grounded drafting, human review, approval branching, transparent AI governance, and an evidence-based resilience roadmap.

## Executive summary

This portfolio project shows how a business analyst can move an AI use case from problem framing through requirements, process design, responsible-AI controls, low-code configuration, testing, evidence capture, and exception-handling design.

The implemented prototype uses the Microsoft Copilot Studio Workflows experience. A manual test inquiry is passed to a governed Agent, routed to Human Review, evaluated through an approval condition, and recorded as either approved for release or requiring revision.

![Published Copilot Studio workflow](projects/customer-email-assistant/evidence/screenshots/01-published-copilot-workflow.png)

## Verified delivery status

| Component | Verified status |
| --- | --- |
| Published Copilot Studio workflow | Complete |
| Governed Agent instructions and inline synthetic policy context | Complete |
| Routine identity-policy Agent test | Passed |
| Outlook Human Review request delivery and rendering | Passed |
| Human Review response callback | Blocked by tenant HTTP 400 restriction |
| Teams Human Review notification | Blocked by tenant notification policy |
| Complete workflow execution | Blocked because the environment has no available Copilot Credits |
| Production exception handling | Designed; implementation pending capacity |
| End-to-end UAT and measured benefits | Not claimed |
| Power BI | Not used |

See the [implementation status](projects/customer-email-assistant/IMPLEMENTATION-STATUS.md), [evidence register](projects/customer-email-assistant/evidence/README.md), and [exception-handling design](projects/customer-email-assistant/exception-handling.md).

## Implemented workflow

~~~mermaid
flowchart LR
    A["Manual test input"] --> B["Governed AI Agent"]
    B --> C["Human Review"]
    C --> D{"Approved?"}
    D -->|Yes| E["Record Approved Outcome"]
    D -->|No| F["Record Revision Outcome"]
~~~

### Controls demonstrated

- synthetic portfolio data only
- inbound inquiry treated as untrusted content
- policy-only drafting with no unsupported commitments
- explicit legal, privacy, fraud, security, and regulatory escalation
- no automatic external send
- human approval required before release
- reviewer comments retained in outcome variables
- separate approved and revision branches
- fail-closed exception-handling design
- honest documentation of blocked tests and platform constraints

## Target production architecture

The repository also contains a future-state design using Outlook, Power Automate, SharePoint or another governed knowledge repository, Teams approvals, and an audit store. Those files are clearly labeled as target architecture and were not represented as the implemented tenant build.

The production resilience pattern uses validation, correlation IDs, bounded retries, Try/Catch/Finally Scopes, Run after conditions, durable error records, alerts, timeout escalation, duplicate prevention, and explicit termination states.

## Skills demonstrated

- AI use-case discovery and prioritization
- business requirements and process redesign
- Copilot Studio low-code configuration
- prompt and instruction design
- human-in-the-loop control design
- responsible AI and prompt-injection controls
- UAT planning and evidence management
- exception handling and operational resilience design
- Microsoft 365 integration design
- risk register, RACI, operating model, and go-live gates
- licensing, capacity, connector, and tenant-policy diagnosis
- stakeholder-ready technical documentation

## Five-minute review path

1. Review the [actual implementation status](projects/customer-email-assistant/IMPLEMENTATION-STATUS.md).
2. Inspect the [published workflow and Human Review evidence](projects/customer-email-assistant/evidence/README.md).
3. Read the [one-page case study](projects/customer-email-assistant/Governed_AI_Policy_Response_Assistant_Case_Study.pdf).
4. Review the [exception-handling and resilience design](projects/customer-email-assistant/exception-handling.md).
5. Read the [portfolio case study](projects/customer-email-assistant/portfolio-case-study.md).
6. Review the [business requirements](projects/customer-email-assistant/business-requirements.md).
7. Inspect the [governed Agent instructions](projects/customer-email-assistant/copilot-agent-instructions.md).
8. Review the [governance controls](projects/customer-email-assistant/governance-and-controls.md) and [UAT scorecard](projects/customer-email-assistant/evidence/uat-scorecard.md).

## Responsible-use statement

This is an independent portfolio demonstration using synthetic policies and inquiries. It is not a production system, legal advice, or an implementation for any employer or law firm. Production use would require business-owner, legal, privacy, security, records, architecture, and platform-administrator approval.

## License

MIT. See [LICENSE](LICENSE).
