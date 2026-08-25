# UAT, demonstration, and interview guide

## UAT scenarios

| ID | Scenario | Expected result |
| --- | --- | --- |
| UAT-01 | Supported policy question | Relevant draft and policy basis returned |
| UAT-02 | Information absent from knowledge | Explicit insufficient-information response |
| UAT-03 | Conflicting policy content | Human escalation, no invented resolution |
| UAT-04 | Prompt injection in email | Embedded instructions ignored |
| UAT-05 | Legal threat or litigation | Escalated, not treated as ordinary service reply |
| UAT-06 | Privacy or security incident | Escalated to designated process |
| UAT-07 | Reviewer edits and approves | Edited response sent and logged |
| UAT-08 | Reviewer rejects | No response sent; rejection logged |
| UAT-09 | Blank final response | Approval blocked or routed to correction |
| UAT-10 | Duplicate trigger | No duplicate review card or reply |
| UAT-11 | Agent connector failure | Failed status and support notification |
| UAT-12 | Teams connector failure | Failed status; no customer response |
| UAT-13 | Outlook send failure | Failed status and visible manual queue |
| UAT-14 | Unauthorized policy user | Restricted content is not surfaced |
| UAT-15 | Retired policy document | Retired content is not used as approved basis |

## Ten-minute team demonstration

1. **Problem and current state, 1 minute:** inconsistent searching, drafting, and informal approvals.
2. **Controlled knowledge, 1 minute:** show active synthetic policies and ownership metadata.
3. **Inbound message, 1 minute:** send a synthetic email to the pilot folder.
4. **Grounded drafting, 2 minutes:** show the Power Automate run and agent response.
5. **Human review, 2 minutes:** edit and approve the Teams card.
6. **Audit, 1 minute:** show draft, final response, reviewer, and timestamps in SharePoint.
7. **Failure or escalation, 1 minute:** demonstrate a privacy incident or unsupported question.
8. **Adoption and next steps, 1 minute:** show pilot measures, feedback route, limitations, and ownership.

## 60-second interview explanation

I designed a low-code AI Customer Email Assistant using Microsoft Copilot Studio, Power Automate, SharePoint, Outlook, and Teams. Power Automate detects an eligible email and calls a published Copilot Studio agent. The agent drafts a response using only approved SharePoint policy knowledge and treats the email as untrusted content. Every draft is posted to an editable Teams Adaptive Card, and nothing is sent until a human reviewer verifies and approves it. SharePoint records the original inquiry, AI draft, final response, reviewer, decision, timestamps, and exceptions. I also defined knowledge ownership, UAT, failure paths, adoption feedback, and pilot measures. This demonstrates workflow redesign and governed AI adoption, not just chatbot configuration.

## Interview questions and answers

### Why use Copilot Studio and Power Automate together?

Copilot Studio handles grounded natural-language drafting. Power Automate handles the deterministic process: email trigger, state changes, Teams review, dispatch, audit, retries, and failure routing. This separation keeps AI flexible while business controls remain predictable.

### Did you create a vector database?

No. I configured SharePoint as a managed Copilot Studio knowledge source. Microsoft handles the retrieval infrastructure, and SharePoint access is evaluated through the authenticated user's permissions. I would not claim that I built or administered a separate Azure AI Search vector index.

### How do you reduce hallucination risk?

The agent uses only approved knowledge, refuses to fill unsupported gaps, identifies its policy basis, treats email content as untrusted, and requires human verification. UAT includes missing, conflicting, adversarial, and high-risk cases.

### Why is human review mandatory?

Customer communication creates operational, reputational, privacy, and legal risk. The reviewer remains accountable, can edit the response, and confirms the final message against approved sources. The system logs the draft and final response for traceability.

### How does this align with AI transformation rather than simple automation?

The work includes process analysis, knowledge governance, stakeholder ownership, low-code delivery, security controls, UAT, change communication, adoption feedback, operational support, and benefits measurement. The technology is one part of the transformation plan.

### How would you integrate legal platforms later?

I would use vendor-supported APIs and approved Power Platform connectors, preserve source-system permissions and ethical walls, and add the integration only after security, privacy, records, and legal-technology review. The portfolio demonstration does not include proprietary credentials.

## Resume bullets after implementation

Use only bullets supported by completed evidence:

- Designed and implemented a low-code, policy-grounded customer email drafting pilot using Copilot Studio, Power Automate, SharePoint, Outlook, and Teams.
- Embedded mandatory human review through editable Teams Adaptive Cards and captured end-to-end decision evidence in SharePoint.
- Defined knowledge governance, prompt-injection controls, exception handling, UAT scenarios, operating ownership, and adoption measures for an AI-enabled workflow.
- Partnered across business, security, privacy, knowledge, and platform roles to translate a manual email process into a governed pilot design.

Do not state an 80% reduction unless an executed pilot, documented baseline, adequate sample, and accountable sponsor validate that result. Until then, describe cycle-time reduction as a target.

