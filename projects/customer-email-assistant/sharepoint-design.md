# SharePoint design

> [!IMPORTANT]
> **Target architecture reference - not the validated tenant build.** The implemented portfolio prototype uses Copilot Studio Workflows with manual inputs, inline governed synthetic policy context, Human Review, approval branching, and outcome variables. See [IMPLEMENTATION-STATUS.md](IMPLEMENTATION-STATUS.md) for verified results and tenant limitations.


## Document library: Approved Policy Knowledge

| Column | Type | Notes |
| --- | --- | --- |
| Policy Owner | Person | Accountable content owner |
| Policy Status | Choice | Draft, Active, Retired |
| Effective Date | Date | Required for Active content |
| Review Date | Date | Knowledge maintenance trigger |
| Confidentiality | Choice | Public, Internal, Confidential |
| Policy Category | Choice | Service, Billing, Privacy, Security, Escalation |
| Version | Single line text | Human-readable controlled version |

Only `Active` documents approved by the knowledge owner should be used for the pilot. Configure versioning and approval according to tenant policy.

## List: AI Email Review Log

| Column | Type | Required |
| --- | --- | --- |
| Title | Single line text | Yes; email subject |
| Correlation ID | Single line text | Yes; unique indexed value |
| Internet Message ID | Single line text | Yes; duplicate-control key |
| Sender Address | Single line text | Yes |
| Received Time | Date and time | Yes |
| Inquiry | Multiple lines plain text | Yes |
| AI Draft | Multiple lines plain text | No |
| Final Response | Multiple lines plain text | No |
| Reviewer | Person | No |
| Decision | Choice | Pending, Approved, Rejected, Escalated |
| Status | Choice | Received, Drafting, Awaiting Human Review, Sent, Rejected, Failed |
| Knowledge Basis | Multiple lines plain text | No |
| Sent Time | Date and time | No |
| Error Summary | Multiple lines plain text | No; sanitized |
| Flow Run ID | Single line text | No |

## Views

- **Pending Review:** Status equals `Awaiting Human Review`
- **Approved and Sent:** Status equals `Sent`
- **Rejected:** Status equals `Rejected`
- **Failed:** Status equals `Failed`
- **Knowledge Review Due:** Review Date is within 30 days

## Access

- Knowledge owners can maintain the policy library.
- Reviewers can read policies and update assigned review records.
- Support owners can read run metadata and sanitized errors.
- General pilot users should not receive list-administration rights.
- Do not assume hidden columns or views provide security. Enforce permissions at the site, library, list, and item level as required.

