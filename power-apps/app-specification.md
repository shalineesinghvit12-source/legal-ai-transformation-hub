# Transformation Portfolio Power App

Build a model-driven application over the Dataverse tables, with a custom scoring page if desired.

## Navigation

1. Executive Portfolio
2. Opportunities
3. Governance Reviews
4. Document Pilots
5. Adoption and Feedback
6. Audit Events
7. Roadmap Assessments

## Core views

| View | Filter and columns |
| --- | --- |
| My Opportunities | Owner is current user; title, stage, RAG, score, target date |
| Prioritization Queue | Stage is Submitted or Triage; impact, effort, risk, score |
| Governance Queue | Decision pending; classification, risk, reviewer, age |
| Pilot Exceptions | Review required or failed; confidence, risk, owner, age |
| Benefits Review | Stage is Benefits; expected vs validated hours, adoption, satisfaction |
| Overdue Actions | Due date before today and not complete; owner, initiative, severity |

## Opportunity form tabs

- Summary: problem, sponsor, owner, stage, RAG, target date
- Process: current state, future state, systems, dependencies
- Prioritization: ratings, score, band, scoring explanation
- Governance: classification, risks, controls, decisions, conditions
- Delivery: milestones, RAID, pilot documents, acceptance
- Adoption: audience, training, communications, feedback
- Benefits: expected and validated metrics
- Audit: chronological events

## Security roles

| Role | Access |
| --- | --- |
| Submitter | Create and read own opportunities; submit feedback |
| Reviewer | Read assigned records; add decisions and corrections |
| Portfolio Manager | Manage portfolio, scores, stages, milestones, and benefits |
| Dashboard Reader | Read approved aggregated records |
| Platform Administrator | Configure solution; no automatic access to privileged document content |

## Power Fx examples

Priority badge:

```powerfx
Switch(
    ThisItem.PriorityBand,
    "Quick Win", ColorValue("#107C10"),
    "Strategic Initiative", ColorValue("#0078D4"),
    "Governance Review Required", ColorValue("#D13438"),
    ColorValue("#FFB900")
)
```

Required human-review indicator:

```powerfx
ThisItem.MinimumConfidence < Value(varConfidenceThreshold)
    || !IsBlank(ThisItem.RiskIndicators)
```

Never place confidential fields into client-side collections unless the user's role and business need are validated.

