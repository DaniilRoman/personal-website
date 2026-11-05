# Simple Analytics Badge Implementation Plan

**Goal:** Show a compact official Simple Analytics badge in the shared footer.

**Architecture:** Override the PaperMod footer in the site layouts, retaining its existing behavior and adding the official linked badge beside the credits. The badge hides its counter and uses the site's dark theme.

**Tech Stack:** Hugo, PaperMod, HTML, CSS.

**Spec:** docs/superpowers/specs/2026-11-05-simple-analytics-badge-design.md

## Task: Add and verify the badge

- [ ] Build the site and confirm representative pages do not yet contain the badge.
- [ ] Copy the theme footer into the site overrides and add the official badge beside the credits.
- [ ] Build the site and verify the badge link and image appear in the footer on representative pages and the tracking script remains present.
- [ ] Review the diff, commit, open and merge a PR, and verify the main-branch deployment.
