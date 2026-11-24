# 🌱 Dunamis: AI Business Advisor for Small Businesses

**Big-company advice. Small-business price.**
An affordable AI consultation website and phone app that gives small businesses ideas and advice tailored to their sector.

## What's inside
| Folder | Contents |
|---|---|
| `web/` | Website (`index.html`), consultation app (`app.html`, installable on phones), pricing & toolkit store (`store.html`), sector knowledge base (`sectors.js`) |
| `server/` | Node.js server that hosts the site and streams AI advice from the Claude API |
| `brand/` | Logo (`logo.svg`), app icon (`logo-mark.svg`), brand guide with colours, fonts and voice |
| `docs/` | Product details & pricing, marketing strategy, scaling plan |

## Run it on your computer
Needs Node.js 20+.
```bash
cd dunamis/server
npm install
export ANTHROPIC_API_KEY=your-key-here   # from console.anthropic.com; without it, the app shows offline sector tips
npm start
```
Open http://localhost:3000.

Settings (environment variables):
| Variable | Default | Meaning |
|---|---|---|
| `ANTHROPIC_API_KEY` | none | Your Claude API key (keep it secret, never commit it) |
| `DUNAMIS_MODEL` | `claude-opus-5-5` | AI model used for advice |
| `DUNAMIS_EFFORT` | `low` | `low` = faster/cheaper; `medium`/`high` = deeper answers |
| `RATE_PER_HOUR` | `30` | Max questions per visitor per hour |
| `PORT` | `3000` | Server port |

## Put it online
1. Push this repo to GitHub (done).
2. Create a free/cheap web service on **Render** or **Railway** → root directory `dunamis/server`, build `npm install`, start `npm start`.
3. Add `ANTHROPIC_API_KEY` in the host's environment settings.
4. Connect your domain (e.g. dunamis.app, check availability first).

## Turn on payments (the store)
Create products in Stripe (or Paystack / Flutterwave / M-Pesa), make **Payment Links**, and paste them into the `CHECKOUT` list at the bottom of `web/store.html`.

## Phone app
- **Now:** open the site on a phone → "Install app" / "Add to Home Screen". It works like an app, even offline for tips.
- **App stores:** wrap `web/` with [Capacitor](https://capacitorjs.com) to publish on Google Play and the Apple App Store (see `docs/scaling-plan.md`).

## Customise
- **Add or edit a sector:** copy a block in `web/sectors.js`.
- **Change prices/products:** edit `PLANS` and `PRODUCTS` in `web/store.html`.
- **Change the advisor's style:** edit `SYSTEM` in `server/server.js`.
- **Rename the brand:** search and replace "Dunamis"; check the name and domain are free and not trademarked in your countries first.

Dunamis gives general business guidance, not legal, tax or financial-investment advice.
