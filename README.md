# climbBeta

A simple, up-to-date directory of climbing gyms in London.

## Scope (v1)

**In scope:**
- List every climbing gym in London
- Each gym shows: name, franchiser, location, website (as text), last verified date
- Data editable by me and friends via Google Sheets — no code changes to update
- Data converted from Google Sheets to JSON

**Out of scope for v1 (see Ideas):**
- User accounts, reviews, ratings
- Maps, search, filters
- Images or photo galleries
- User submissions
- Rendering board features, facilities, opening hours, etc. (data is carried but not displayed)

**Done when:** live URL lists 15–20 gyms and adding a new one takes under 2 minutes via the sheet.

## Data

Source of truth: a Google Sheet (`ClimbingGyms` tab), exposed as JSON via Google Apps Script.

- **Endpoint:** `https://script.google.com/macros/s/AKfycbxaq0YhpbUiV2XYokvIAdU_g99c7dZHI7xre0kPpfJfIKQu90cEJITSHrItw5Y7mSQ-Eg/exec`
- **Row layout:** Row 1 = title/notes (ignored), Row 2 = headers, Row 3+ = one gym per row.
- **Headers** are camelCased in the JSON by the script (e.g. `Climbing offered` → `climbingOffered`).
- **`id`** is auto-derived from `Name` if blank (lowercase, hyphenated).
- **`last_verified`** becomes `lastVerified` (ISO date string or blank).
- **`Website`** is a label, not a URL. The site renders it as text. Real links come later via a `Website URL` column.

### Updating the data

1. Edit the Google Sheet. Friends can do this too.
2. That's it — the `/exec` endpoint reads the sheet live. No export, no commit needed for data changes.

### Updating the Apps Script

The script lives in Google Apps Script, synced to this repo via `clasp`.

- Local files: `Code.gs`, `appsscript.json` (committed); `.clasp.json` (gitignored).
- After editing locally: `clasp push`.
- Then **redeploy**: Apps Script → Deploy → Manage deployments → edit (pencil) → **Version: New version** → Deploy.
  - **Never create a new deployment** — that changes the `/exec` URL and breaks the frontend.
- The `/exec` URL stays stable across new versions.

## Running locally

```bash
npm install
npm run dev