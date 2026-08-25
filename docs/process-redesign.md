# Process redesign

## Current state

```mermaid
flowchart TD
    A["Idea shared by email or meeting"] --> B["Manual clarification"]
    B --> C["Spreadsheet business case"]
    C --> D["Unstructured approvals"]
    D --> E["Pilot with limited adoption evidence"]
```

Common issues: incomplete requirements, duplicate proposals, inconsistent evaluation, unclear ownership, approval delays, limited auditability, and benefits reported without a stable baseline.

## Future state

```mermaid
flowchart TD
    A["Copilot-guided discovery"] --> B["Structured Dataverse record"]
    B --> C["Explainable score and business case"]
    C --> D["Risk-based human governance"]
    D --> E["Measured pilot and adoption loop"]
```

## Control-point improvements

| Pain point | Redesign | Measure |
| --- | --- | --- |
| Incomplete intake | Copilot asks for missing required information | First-pass completeness |
| Inconsistent prioritization | Versioned weighted score plus human decision | Decision consistency and lead time |
| Approval ambiguity | Risk-based RACI and recorded conditions | Approval aging and overdue reviews |
| AI error risk | Confidence threshold, citations, human correction | Accuracy and override rate |
| Weak adoption | Targeted training and scheduled feedback | Training, activation, satisfaction |
| Unverified value | Baseline and validated benefits review | Expected vs validated hours |

