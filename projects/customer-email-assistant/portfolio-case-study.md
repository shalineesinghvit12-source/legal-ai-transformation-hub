# Portfolio Case Study: Governed AI Policy Response Assistant

## Situation

Business teams answer recurring questions by searching policy documents, deciding which guidance applies, drafting an email and obtaining informal review. The process is slow, inconsistent and difficult to audit. Purely automatic AI responses would introduce unacceptable accuracy, privacy and legal risks.

## Objective

Design a controlled low-code pilot that shortens drafting time while keeping a person accountable for every external response.

## Solution

- Outlook receives an inquiry in an approved shared mailbox.
- Power Automate creates a correlation ID and SharePoint audit record.
- A published Copilot Studio agent drafts a response using approved SharePoint knowledge.
- Teams presents the inquiry and editable draft to an authorized reviewer.
- Only an approved response is sent; rejected or sensitive cases are escalated.
- SharePoint records the draft, final text, reviewer, decision, timing and exception state.

## My contribution

- framed and prioritized the use case using value, feasibility and risk
- defined scope, stakeholders, functional requirements and acceptance criteria
- redesigned the end-to-end process with approval and exception paths
- selected Microsoft 365 components for a low-code MVP
- designed knowledge metadata, access controls and audit data
- wrote grounded Copilot instructions and the Power Automate workflow specification
- created synthetic policies, test inquiries, UAT scenarios and a demo plan
- defined pilot measures without claiming unverified savings

## Responsible AI controls

The agent must use approved knowledge, identify insufficient evidence, resist instructions embedded in inbound email, avoid legal advice and escalate high-risk matters. Human approval is mandatory before sending. Synthetic data is used for portfolio testing.

## Pilot measurement

The baseline and target will be agreed before UAT. Measures include median handling time, first-pass acceptance, edit rate, escalation precision, unsupported-answer rate, send-without-approval incidents and audit completeness. Quantified benefits will be reported only after an adequate test sample.

## Delivery status

Requirements, design, agent instructions, flow blueprint, Adaptive Card, governance and test pack are complete. Live tenant configuration, screenshots, executed UAT and solution export remain pending and are not represented as complete.

## Relevance to AI transformation

The case study demonstrates use-case discovery, process analysis, Microsoft Copilot, Power Automate, Microsoft 365 integration, stakeholder alignment, responsible AI governance, change planning, UAT, benefits measurement and structured delivery.
