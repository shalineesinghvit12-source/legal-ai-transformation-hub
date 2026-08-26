# Demonstration script

> [!IMPORTANT]
> This script demonstrates only the **validated Copilot Studio Workflow prototype**. Do not simulate a successful approval callback or customer email send. The tenant blocked those steps; the limitation is part of the engineering evidence.

## Preparation

- Open the published workflow and its five visible stages.
- Open the redacted evidence register in [evidence/README.md](evidence/README.md).
- Use only the synthetic address-update test case.
- Hide tenant IDs, personal messages, and connection details.

## Five-minute technical walkthrough

### 0:00–0:45 — Business problem

Explain that policy-response drafting is repetitive but fully autonomous customer communication creates accuracy, privacy, legal, and reputational risk.

### 0:45–1:40 — Implemented workflow

Show: **Start → Agent → Human Review → If/Else → Approved or Revision outcome**. State that the trigger is manual for safe demonstration and repeatable UAT.

### 1:40–2:35 — Governed Agent

Show the two inputs, the embedded synthetic policies, prompt-injection safeguards, escalation rules, and required structured output: decision, draft, policy basis, and review note.

### 2:35–3:25 — Agent test evidence

Open the successful Agent-node screenshot. Explain why the address update is drafted but not completed and why prohibited identity or payment data is not requested.

### 3:25–4:10 — Human Review evidence

Open the redacted Outlook screenshot. Describe it accurately: the review request was delivered and rendered with Yes/No and reviewer-comment inputs. The callback later returned HTTP 400, so approval completion is not claimed.

### 4:10–4:40 — Decision and audit design

Show the If/Else condition and separate outcome variables. Explain that the branch design is published and health-checked, while a complete run remains blocked by tenant credits and notification constraints.

### 4:40–5:00 — Production roadmap

Close with managed knowledge, durable audit storage, monitoring, retry and timeout handling, solution packaging, environment promotion, and full UAT after capacity and connector approval.

## Recommended closing statement

“I built and published a governed Copilot Studio Workflow, validated the Agent response and Human Review request delivery, documented the blocked tenant dependencies, and separated the working prototype from the production target architecture.”
