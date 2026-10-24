# Test Case Matrix

| ID | Area | Scenario | Expected result | Priority |
|---|---|---|---|---|
| FUN-01 | Home | Open homepage | HTTP < 400; title and content visible | P1 |
| FUN-02 | Navigation | Open catalog | Catalog loads and products render | P1 |
| FUN-03 | Search | Search “cotton” and unmatched term | Results or clear empty state | P1 |
| FUN-04 | Product | Open product detail | Name, price, imagery and variants visible | P1 |
| FUN-05 | Variant | Choose size/colour | Selection is clear; unavailable variant blocked | P1 |
| FUN-06 | Cart | Add item/change quantity/remove | SKU, quantity, subtotal and count update | P1 |
| FUN-07 | Inventory | Buy last unit in two sessions | Only one order succeeds; no negative stock | P1 |
| FUN-08 | Checkout | Valid sandbox payment | One order and confirmation; no duplicate charge | P1 |
| FUN-09 | Payment failure | Declined sandbox payment | Clear error; order not marked paid | P1 |
| FUN-10 | Payment retry | Replay webhook or retry request | Idempotency prevents duplicate side effects | P1 |
| FUN-11 | Responsive | Mobile/tablet/desktop | No clipped controls or unintended overflow | P1 |
| INT-01 | Integration | Successful order updates stock | Inventory decremented exactly once | P1 |
| PERF-01 | Performance | API/page baseline | API p95 < 800 ms target; LCP ≤ 2.5 s | P1 |
| PERF-02 | Reliability | Controlled staging load | Error rate < 1%; no crash | P1 |
| A11Y-01 | Accessibility | Keyboard and screen-reader smoke test | Labels, focus, headings and contrast reviewed | P1 |
| SEC-01 | Security | Authorization/input/session checks | No unauthorized data exposure | P1 |

For every run record test ID, build, environment, browser/device, tester, date, actual result, pass/fail/blocked, evidence, defect ID, severity and retest result.
