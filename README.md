# Justin Park Engineering Portfolio

Personal engineering portfolio website focused on mechanical engineering, UAV systems, robotics, and systems integration.

The finished static site is in `website/`. It has Home, Projects, four concise primary project pages, About, and a custom 404 page. No framework, package installation, build process, backend, or analytics is required.

## Preview locally

From the repository root:

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory website
```

Open `http://127.0.0.1:8765/`. Serve only `website`, so private source materials and planning notes stay outside the public server. Python's basic server does not apply Cloudflare `_headers` or automatically use the custom 404 page for missing routes; those are hosting features.

Run the dependency-free static checks with `python scripts/check-site.py`. This verifies page headings, metadata, local links, image paths, anchors, public-file types, and resume identity when the private source is available. Desktop/mobile browser validation is recorded in the completion review.

## Content and assets

- Public pages and shared CSS/JavaScript: `website/`
- Current public resume: `website/assets/documents/justin-park-resume.pdf`
- Deliberately selected public images: `website/assets/images/`
- Evidence, provenance, and reviews: `notes/`
- Private read-only reference files: `source-materials/` (ignored by Git)

Detailed content-inventory and project-evidence notes are preserved locally but ignored by Git because they include private company evidence. Publish only the site directory, not repository notes.

The current resume governs education, roles, and dates. `personal-info.txt` governs contact/display preferences. Final project documents govern completed configurations and results. Avoid publishing internal Heven documents or introducing unsupported performance claims.

## Deployment

Deploy **only `website/`** using Cloudflare Pages. Use the existing GitHub repository, production branch `main`, framework preset **None**, build command `exit 0`, and build output directory `website`. Leave the root directory at the repository root. No environment variables or secrets are needed.

See [deployment instructions](notes/deployment-readiness.md) for account authorization, exact settings, and the final live-site checks. See [the completion review](notes/completion-review.md) for validation and remaining optional content improvements.

No public origin has been selected. Canonical URLs, absolute social-preview image URLs, and a sitemap should be added once the final deployment URL is confirmed; the pages already include titles, descriptions, and text sharing metadata.
