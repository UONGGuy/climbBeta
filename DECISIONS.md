# Tech Stack & Decisions

Living record of what we're using, why, and what's still open.
Update in place. Resolved open points move up into "Chosen".

## Chosen

| Area | Choice | Why |
|---|---|---|
| Frontend | Astro | Content-driven, static HTML by default, zero JS unless needed. Fast, free to host, good styling path. Fits "look nice" and later traffic/monetization without hosting cost. |
| Styling | Tailwind (planned) | Fast clean look, well-supported in Astro. To be added at scaffold. |
| Data source | Google Sheets + Apps Script JSON | Friends already edit the sheet; no backend or code needed to update data. Endpoint is the stable `/exec` URL. |
| Data shape | `{ data, _header_map, _dropdown_options }` | Records + reference metadata + auto-generated schema docs. v1 renders `data` only; dropdowns carried for later filters. |
| JSON keys | camelCase | Native for JS/TS frontend. Sheet headers stay human-readable; the script camelCases at the boundary. |
| Hosting | Netlify or Vercel (free tier) | Auto-deploy on push to `main`; allows commercial use later. |
| Repo | GitHub | Standard, free, integrates with hosting. |
| Apps Script source | Synced via `clasp` | Version-controlled in repo (`Code.gs`, `appsscript.json`). `.clasp.json` gitignored. Redeploy = Manage deployments → New version (URL stays stable). |

## Open points

- [ ] **Tailwind vs plain CSS** — decide at Astro scaffold (M1). Leaning Tailwind.
- [ ] **Static build vs client-side fetch** — if sheet updates should appear without a rebuild, add client fetch. Decide after v1 ships. v1 can rebuild on data change.
- [ ] **Board features modelling** — sheet stores free-text tags in "Board climbing". v1 ignores this field. When the site renders boards, add a parser in the script to emit structured `{type, variant, angle, year, mode}` objects alongside the raw string (`boardClimbingRaw` kept for display). **Do NOT restructure the sheet.** Revisit only if tags prove unparseable.
- [ ] **`Website` → `Website URL`** — v1 renders `website` as text (it's a label). Later: add a `Website URL` column, use it as `href` with the label as link text; fall back to plain text when blank.
- [ ] **Blank-field display rules** — `location` and `lastVerified` can be empty. v1 rule: omit the line (decide at scaffold if this changes).
- [ ] **Monetization** — ads (AdSense) vs affiliate links. Revisit once traffic exists.
- [ ] **Page-per-gym vs single list** — parked in README Ideas.
- [ ] **Data quality pass** — typos ("Ravernsbourne", "Houndslow"), franchiser naming inconsistency ("Center" vs "Centre"). Cosmetic; do not fix during v1.

## Rejected / not now

- **Postgres / Supabase** — overkill for v1: no writes from the site, no auth, few dozen rows. Revisit if data grows or submissions are added.
- **Flask + SQL** — was v0's stall point; no product need.
- **Drive snapshot of JSON** — dropped. `/exec` is the source of truth; a committed snapshot from the `/exec` response is the fallback if ever needed.
- **`.claspignore` to skip pull** — not possible; `.claspignore` only affects push. Unwanted `.gs` files are pulled but not committed.