# Cloudflare deployment and production domain

Updated October 3, 2026. Intended production origin: **https://justinsejinpark.com** (HTTPS, apex domain). Deploy only `website/`. Keep source materials and notes outside the public output. No framework, dependencies, secrets, analytics, or contact form are required.

The user authorizes deployment and connection to the purchased domain when account access permits. All other portfolio constraints remain in effect. Stop for user authentication, GitHub access approval, or domain approval; do not handle passwords or MFA on the user's behalf.

## Current access boundary

Cloudflare and GitHub are connected. The existing Pages project is **engineering-portfolio**, with hostname **engineering-portfolio-is3.pages.dev**. Its initial output directory was blank; this was corrected to **website**, with command **exit 0**, repository root unchanged, and production branch **main**. Retrying produced successful deployment **9d3f8f5f-81fb-41a1-8db4-d5d0957c35d7** from commit **0357d99** at 4:25 PM Eastern on October 3, 2026.

The open **Confirm new DNS record** screen proposes **CNAME @ → engineering-portfolio-is3.pages.dev**, TTL Auto, for **justinsejinpark.com**. Click **Activate domain** to approve that record and domain connection, then tell this chat to resume. The agent stopped before this explicit domain approval, as requested. No DNS record was changed by the agent. Apex HTTPS/certificate and live-domain verification remain pending.

## Completed Pages verification

At `https://engineering-portfolio-is3.pages.dev`, all **83 public files** matched the curated local website (text line endings normalized; binary images and current resume matched exactly). All eight HTML pages served the expected security headers. Six missing/private routes returned the custom HTTP 404: a nested nonexistent page, source contact file, evidence note, deployment note, README, and Git configuration. A browser check confirmed homepage rendering without horizontal overflow at 1280 px, production canonical metadata, loaded hero/wordmark, working image dialog and Escape dismissal, and no console warnings/errors. The unchanged layout retains the earlier complete desktop/mobile QA recorded in the completion review. These checks verify Pages hosting, not yet the apex domain.

## Pages deployment

1. Open **Workers & Pages** in that Cloudflare account. Reuse a suitable existing project if one serves this repository; otherwise choose **Create application → Pages → Import an existing Git repository**.
2. If prompted, approve the Cloudflare GitHub integration for **`this-sjin/engineering-portfolio` only**. This approval is a user-action boundary.
3. Select the repository. Choose a project name if creating one; no assigned `pages.dev` hostname is assumed.
4. Production branch: **main**. Framework: **None**. Build command: **exit 0**. Build output: **website**. Leave root directory at the repository root and environment variables empty.
5. Select **Save and Deploy**. Record the actual project and assigned `pages.dev` URL after success.

Settings follow Cloudflare's [static HTML guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/) and [Git integration guide](https://developers.cloudflare.com/pages/get-started/git-integration/).

## Connect the purchased domain

1. Verify `justinsejinpark.com` is an active Cloudflare zone in the **same account** as the Pages project. Stop for the user if ownership, verification, or approval is required.
2. In the Pages project, select **Custom domains → Set up a domain**.
3. Enter **justinsejinpark.com**, click **Continue**, and review the proposed DNS record. The user completes any required confirmation. Cloudflare can automatically create the required CNAME for a zone managed in that account.
4. Wait for the domain and HTTPS certificate to become active, then verify **https://justinsejinpark.com**.

Associate the domain through Pages before relying on DNS; do not merely add a standalone CNAME. Follow Cloudflare's [custom-domain instructions](https://developers.cloudflare.com/pages/configuration/custom-domains/). `www` is not configured or required; if added later, provision its domain/certificate before redirecting it to the apex. Do not guess a `pages.dev` redirect or change unrelated DNS records.

## Production metadata prepared

- Seven pages: canonical links, `og:url`, absolute public Open Graph/Twitter images, image dimensions and alternatives.
- `sitemap.xml`: seven indexable routes under the production origin, excluding 404, PDFs, sources, and notes.
- `robots.txt`: allows crawling and references `https://justinsejinpark.com/sitemap.xml`.
- Relative navigation and asset paths remain usable locally. The custom 404 remains noindex.
- No credentials or account identifiers are stored in the repository.

## Verify after connection

- Open all seven pages directly, including nested route reloads and mobile navigation.
- Open the current Resume PDF and check approved contact links.
- Enlarge a gallery image and dismiss with Escape; inspect console/network for missing assets or CSP errors.
- Verify HTTPS, canonical/Open Graph metadata, sharing images, `/sitemap.xml`, and `/robots.txt` on the apex.
- Confirm a missing nested route returns HTTP 404 with working navigation. Private source and note paths must return 404.
- Verify deployed `_headers`; see Cloudflare's [headers documentation](https://developers.cloudflare.com/pages/configuration/headers/).

Local checks do not establish domain connection, certificate issuance, or production HTTP behavior. Record actual deployment and live verification only after they occur.
