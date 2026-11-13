# Tech Stack & Decisions

## Chosen
| Area | Choice | Why |
|---|---|---|
| Frontend | Astro | Static, fast, zero JS by default, free hosting; good styling path |
| Styling | Tailwind (planned) | Fast clean look, well-supported in Astro |
| Data source | Google Sheets + Apps Script JSON | Friends already edit the sheet; no backend or code needed to update |
| Hosting | Netlify/Vercel free tier | Auto-deploy on push; allows commercial use later |
| Repo | GitHub, public/private TBD | Standard, free, integrates with hosting |

## Notes
- Data from Google Apps Script deployed to: https://script.google.com/macros/s/AKfycbxaq0YhpbUiV2XYokvIAdU_g99c7dZHI7xre0kPpfJfIKQu90cEJITSHrItw5Y7mSQ-Eg/exec

## Open points
- [ ] Static build vs client-side fetch: if Sheet updates should appear without rebuild, may need client fetch. Decide after v1 ships.
- [ ] Tailwind vs plain CSS — pick at M1 scaffold.
- [ ] Monetization: ads (AdSense) vs affiliate links. Revisit once traffic exists.
- [ ] Page-per-gym vs single list — parked in README Ideas.
- [ ] Data to JSON: Sheet stores free-text tags in "Board climbing".
      v1 ignores this field. When the site renders boards, add a parser
      in the script to emit structured {type, variant, angle, year, mode}
      objects alongside the raw string. Do NOT restructure the sheet.
- [ ] Data to JSON: Sheet to contain full urls.

## Rejected / not now
- Postgres/Supabase — overkill for v1; no writes/auth; few dozen rows. Revisit if data grows or site needs submissions.
- Flask + SQL — was v0's stall point; no product need.