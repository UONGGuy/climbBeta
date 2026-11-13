# climbBeta

A simple, up-to-date directory of climbing gyms in London.

## Scope (v1)

**In scope:**
- List every climbing gym in London
- Each gym shows: name, borough, website, notes, last verified date
- Data editable by me and friends via Google Sheets — no code changes to update
- Data converted from Google Sheets to JSON

**Out of scope for v1 (see Ideas):**
- User accounts, reviews, ratings
- Maps, search, filters
- Images or photo galleries
- User submissions

**Done when:** live URL lists 15–20 gyms and adding a new one takes under 2 minutes via the sheet.

## Data

Source of truth: a Google Sheet, exposed as JSON via Google Apps Script.

Endpoint: `https://script.google.com/macros/s/XXXX/exec`

Columns: `id, name, borough, website, notes, last_verified`

## Running locally

(to be added once the frontend is scaffolded)

## Ideas (don't build yet)

- Page per gym
- Facilities per gym
- Filter by borough
- Map pins
- Freshness indicator on stale entries
- Info pages for beginners
- Database links for all waivers for all relevant activities
- Submit ratings and reviews
- User authentication and authorisation.
- Generate revenue from traffic volume?