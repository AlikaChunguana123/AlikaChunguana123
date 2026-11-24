# SproutWise Product Details

## One-liner
SproutWise is an AI business advisor app (website + phone app) that gives small businesses practical, sector-specific ideas and advice for less than the price of a lunch per month.

## The problem
- Small businesses make up ~90% of businesses worldwide, and many fail within 5 years. Common reasons: cash flow, poor pricing, weak marketing.
- Consultants cost $50–$200+/hour, which is out of reach for most micro-businesses.
- Generic online advice isn't written for a market stall in Lagos or a salon in Lisbon.

## The solution
An always-available advisor that knows the owner's **sector, location, stage, team size and challenge**, and answers in plain language with concrete, low-cost next steps.

## Target customers
| Segment | Example | Need |
|---|---|---|
| Micro-business owners (1–5 people) | Market vendor, tailor, barber | Customers, pricing, cash flow |
| Early-stage founders | "Just an idea" stage | Validation, business plan, first customers |
| Growing small businesses (6–20) | Restaurant, delivery company | Hiring, systems, second location |
| Partners (B2B2C) | Banks, microfinance, NGOs, chambers of commerce | Support their members/borrowers at scale |

## Features
### MVP (built in this repo)
- Business profile (sector, location, stage, size, challenge), saved on the device
- 13 sectors with a built-in playbook: ideas, marketing, money, risks
- 5 topics: Ideas, Marketing, Money & pricing, Growth, Risks, each with quick-start questions
- Streaming AI answers with a "This week:" action step
- Offline mode: sector tips still work without internet
- Installable as a phone app (PWA) from the browser
- Website, pricing page and toolkit store

### Next (v1.1–v2)
- User accounts and plan limits (free 5/month, etc.)
- Payments: Stripe + local options (M-Pesa, Paystack, Flutterwave, MTN MoMo)
- Generators: 30-day marketing plan, business plan, pricing calculator, cash-flow forecast
- Monthly "growth check-in" report emailed or sent on WhatsApp
- **WhatsApp advisor bot**, since many owners live in WhatsApp
- Multi-language (French, Portuguese, Spanish, Swahili, Arabic…)
- Voice questions and answers for owners who prefer speaking
- Human expert marketplace for paid sessions
- Android/iOS store apps (wrap the PWA with Capacitor)

## Pricing (see `web/store.html`)
| Plan | Monthly | Yearly | For |
|---|---|---|---|
| Seed | $0 | $0 | Try it: 5 consultations/month |
| Sprout | $5 | $50 | Solo owners: 50/month |
| **Bloom** | **$12** | **$120** | Growing teams: unlimited (fair use), tools, 3 users |
| Harvest | $29 | $290 | Multi-location: 10 users, human advisor call |

**Toolkit store (one-time):** Business Plan Kit $15 · 90-Day Marketing Calendar $9 · Pitch Deck $12 · Money Tracker $7 · Mini Brand Kit $19 · 45-min Expert Session $29.

**Regional pricing:** adjust by purchasing power, e.g. Sprout ≈ $2–3 in lower-income markets. Discounts: students and women-led startups (year one) 50% off.

## Unit economics (estimate)
Using the default model (Claude Opus 5.5, $4 in / $20 out per million tokens) at "low" effort:
- One consultation ≈ 2,000 input + ~900 output tokens ≈ **$0.02–0.03**
- Sprout ($5, 50 questions): AI cost ≈ $1.30, payment fees ≈ $0.45, **≈ 65% gross margin**
- Bloom ($12, ~200 questions typical): AI cost ≈ $5, **≈ 50% margin**
- Levers: prompt caching (already on for the system prompt), shorter answers, or running the free tier on a cheaper model via `SPROUTWISE_MODEL` (e.g. Claude Haiku 5.5 at $0.10/$0.50, roughly 40× cheaper). Test answer quality before switching.

## Success metrics
- Activation: % of sign-ups asking 3+ questions in week 1 (target 40%)
- Free → paid conversion (target 4–6%)
- Monthly churn (target < 5%)
- "Did you try the This-week action?" Yes rate (target 50%)
- Customer outcome: owners reporting more sales after 90 days
