# Commercial readiness, launch and operation

**Read this when**: at concept/first playable as well as submission. Primary pages checked
2026-09-21. Dashboard eligibility and current detailed policy win over an older
marketing overview; the agent drafts decisions and performs already authorized
work, not financial commitments merely because this checklist exists.

## Start before content is finished

Inspect organization/team roles, verification, app identity/category, age audience,
requested data/features, distribution regions and paid-account status. Assign a
human owner for legal identity, bank/tax details and terms; never put documents or
secrets in public Git. DUC/platform access and DPA are separate tasks. Check actual
Requirements/Tasks: the DPA guide makes it conditional, and absence of a required
assessment is not proof that all privacy obligations disappear.

[Learning path](https://developers.meta.com/horizon/resources/developer-learning-path/),
[organization verification](https://developers.meta.com/horizon/resources/publish-organization-verification/),
[financial setup](https://developers.meta.com/horizon/resources/publish-account-management-bank-tax/),
[DPA](https://developers.meta.com/horizon/resources/publish-data-protection-assessment/).

## Decide the revenue model, then wire and test it

Present premium, F2P, add-ons and subscriptions against audience, repeat value,
ongoing content/support cost and region/age restrictions. No generic “best” model.
Record pricing/promotion decisions with the operator. Premium pricing removes no
applicable platform entitlement, purchase/restoration or commercial-readiness
obligation; a short schedule is not evidence that a model is feasible. Integrate the applicable
Meta purchase/entitlement path, backend validation and idempotent fulfillment;
exercise cancel, decline, reconnect, consume, restore, refund/revocation and
multiple-account behavior. For subscriptions also test renew, expire, cancellation
and tier/trial semantics using official test users/payment fixtures. A test user
with a real card can still incur a real charge; use documented test methods.

[Monetization map](https://developers.meta.com/horizon/resources/monetization/),
[add-on integration](https://developers.meta.com/horizon/resources/add-ons-integration/),
[test subscriptions](https://developers.meta.com/horizon/resources/test-subscriptions/).

## Pre-launch decisions are time-sensitive

Consult [pre-launch listings](https://developers.meta.com/horizon/resources/pre-launch-listings/)
**before the initial submission**. Its detailed guide constrains listing changes,
pricing and date changes. The inspected overview and detailed page disagree on
Coming Soon lead time (180 versus 360 days); the overview implies advance revenue,
while the detailed page says users are charged 24 hours before launch. Record the
conflict, use the detailed current flow and confirm Dashboard eligibility before
promising dates or cash flow. Do not assume pre-orders finance months of work.

For submission, [publish-submit](https://developers.meta.com/horizon/resources/publish-submit/)
recommends at least two weeks of review lead time; treat this as a planning buffer,
not a guaranteed SLA. Separate 2D/immersive/PC requirement sets. Provide reviewer
steps, test access and reproducible explanations of online/MR/multiplayer features.
Reply to actual findings; do not claim every rejection enumerates every defect.
[Review lifecycle](https://developers.meta.com/horizon/resources/publish-app-review/).

## Launch marketing is an evidence-backed workstream

Write audience, product promise, acquisition/retention goal, channel, format,
CTA, owner, timeline, budget and measurable hypothesis in `docs/xr/launch-plan.md`
or an existing equivalent. Propose owned community/devlogs, earned press/creators,
shared channels and paid ads based on audience and capacity. Preparing a press kit
or outreach draft does not authorize sending it or purchasing ads.

Schedule real gameplay capture from a representative build. Record shots and
source builds; derive trailer, stills and short variants from reusable editable
masters. Use Foundry/Blender/media tools if available for production, but inspect
rights and actual delivery. `references/store-asset-production.md` supplies the
Store-specific acceptance procedure (load it from this skill's reference table).

[Marketing plan](https://developers.meta.com/horizon/resources/gtm-marketing-plan/),
[asset production](https://developers.meta.com/horizon/resources/gtm-marketing-assets/),
[marketing overview](https://developers.meta.com/horizon/resources/market-your-app/).

## Measure after launch

Track crash/ANR, frame/thermal regressions, onboarding completion, sessions and
retention, purchases/restores/refunds, support and content/service cost. Define
metric cohort, window, time zone, attribution and delay before comparison.

The [Marketing Attribution dashboard](https://developers.meta.com/horizon/resources/publish-marketing-analytics/)
is retired. The [Funnel guide](https://developers.meta.com/horizon/resources/publish-funnel-analytics/)
itself describes migration to real-time analytics; resolve the current Dashboard
surface instead of promising the legacy route. Event-surface and delayed last-touch
attribution are not interchangeable. Treat approximate unique-user aggregates as
such, not exact per-person campaign tracking.

[Creative A/B testing](https://developers.meta.com/horizon/resources/ab-testing-instructions/)
is distinct from pricing experiments. Record a hypothesis, primary metric and
stopping rule. One-variable tests support attribution; changing several assets
measures the bundle. Review/eligibility and automatic winner publication are
separate decisions. Statistical confidence is not a guaranteed uplift. Check
current controls rather than copying thresholds from a dated example.

Prepare support ownership, review responses, release notes, save/backend migrations,
service recovery, SDK/OS policy deadlines and required recurring assessments.
Propose monitoring with actionable thresholds; schedule it only when authorized.
