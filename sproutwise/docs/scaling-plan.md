# SproutWise Scaling Plan

How to grow from this MVP to thousands of paying businesses.

## Stage 1: Launch (0–500 users)
**Tech (what's in this repo)**
- One Node.js server (`server/server.js`) serves the website/app and the `/api/advice` AI endpoint
- Host on Render, Railway or Fly.io (≈ $5–10/month). Set `ANTHROPIC_API_KEY` in the host's secret settings, never in code
- Custom domain + HTTPS (required for the installable app)
- Payments: paste Stripe Payment Links / Paystack / Flutterwave links into `CHECKOUT` in `web/store.html`
- Simple per-IP rate limit is built in (`RATE_PER_HOUR`)

**Business:** founder-led sales, 20 beta users, 2 partners, validate pricing.

## Stage 2: Product-market fit (500–5,000 users)
**Tech to add**
- **Accounts & plan limits:** Supabase or Firebase Auth + Postgres (users, profiles, plans, usage counts)
- **Billing:** Stripe Billing subscriptions + webhooks to update plans; local mobile money in Africa/Asia
- **Conversation history** stored per user; monthly growth reports generated in batch (Message Batches API = 50% cheaper)
- **Analytics:** Plausible/PostHog; log question topics (anonymised) to improve sector playbooks
- **App stores:** wrap the PWA with Capacitor → Google Play ($25 once) and Apple App Store ($99/yr)
- **WhatsApp bot:** WhatsApp Business Cloud API calling the same `/api/advice` logic

**Team:** founder + 1 developer (part-time) + 1 community/content person.

## Stage 3: Scale (5,000–100,000 users)
**Architecture**
```
Phone app / Website / WhatsApp
          │
   CDN (static site)  ──►  API servers (autoscaling, stateless)
                                 │
              ┌──────────────────┼──────────────────┐
          Postgres            Redis               Claude API
     (users, billing)   (rate limits, queues)   (AI advice)
```
- Move static files to a CDN (Cloudflare/Netlify); run API servers behind a load balancer with autoscaling
- Redis for rate limits and caching common answers
- Background job queue for reports and generators
- Monitoring & alerts (Sentry, uptime checks), daily backups
- Cost controls: prompt caching, per-plan model choice, monthly AI spend alerts
- Security & privacy: GDPR/POPIA/NDPR-style data policy, encrypted data, data-deletion button

**Growth engines**
- B2B2C partner licences: banks/MFIs/NGOs pay per member per year (e.g. $1–3) to offer SproutWise
- Localisation: 5+ languages, local regulations and holidays per country
- Expert marketplace: vetted human advisors, SproutWise takes 20%
- Toolkit store expanded with sector-specific templates

**Team:** CEO, CTO, 2–3 engineers, growth lead, partnerships lead, support, country ambassadors.

## Funding options
- Bootstrap from early subscriptions + toolkit sales
- Small-business and women-entrepreneur grants and accelerator programmes
- Pre-seed/angel round once you show ~$2–5k monthly recurring revenue and good retention

## Key risks & mitigations
| Risk | Mitigation |
|---|---|
| AI gives wrong or risky advice | Clear system rules, "check with a professional" for legal/tax/medical, feedback button, review flagged answers |
| AI costs grow faster than revenue | Plan limits, caching, cheaper model for free tier, monitor cost per user |
| Low willingness to pay | Regional pricing, partner-funded licences, mobile-money payments |
| Competition from free chatbots | Sector playbooks, local context, action-focused format, WhatsApp, community, human experts |
