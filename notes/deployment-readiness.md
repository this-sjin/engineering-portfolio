# Cloudflare deployment readiness

Prepared October 3, 2026. The deployable directory is `website/`; source materials and notes must remain outside it. No framework, build dependencies, secrets, or domain purchase is needed for a first Pages deployment.

## Remaining user-controlled steps

1. Sign in to the intended Cloudflare account and open **Workers & Pages**.
2. Select **Create application → Pages → Import an existing Git repository**. If prompted, authorize the Cloudflare GitHub integration for `this-sjin/engineering-portfolio` only.
3. Select that repository and begin setup. Choose a project name in your account.
4. Set production branch to `main`, framework preset to **None**, build command to `exit 0`, and build output directory to `website`. Keep the root directory at the repository root and leave environment variables empty.
5. Select **Save and Deploy**. Copy the actual assigned `https://…pages.dev` URL after the deployment succeeds. A custom domain is optional and can be configured later.

These settings follow Cloudflare's [static HTML guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/) and [Git integration guide](https://developers.cloudflare.com/pages/get-started/git-integration/). No Pages project or account selection is assumed from the GitHub repository name.

## Live verification

- Open Home, Projects, About, and all four primary project routes directly, including on mobile. Reload a nested project route.
- Open the Resume PDF, verify the displayed version, and check email, phone, and LinkedIn links.
- Enlarge a gallery image and dismiss it with Escape; verify mobile navigation.
- Visit a nonexistent nested route. Confirm the custom “Page not found” page returns HTTP 404 and its navigation works.
- Check browser console/network results for missing assets or CSP violations. The committed `_headers` file supplies restrictive same-origin content rules, anti-framing, content-type, referrer, and browser permission headers; see Cloudflare's [headers documentation](https://developers.cloudflare.com/pages/configuration/headers/).
- Confirm `/source-materials/personal-info.txt` and internal document paths return 404. Only `website/` should be deployed.

## After the final public URL is known

Use the confirmed production origin for canonical and `og:url` metadata, absolute project/social-preview image URLs, and `sitemap.xml`. Add the sitemap URL to `robots.txt`. These were intentionally omitted rather than filled with an invented domain or a localhost address. Titles, descriptions, Open Graph text metadata, and favicon are already present.

The current request authorizes deployment preparation and a Git push. Prior instructions explicitly deferred public deployment, and no Cloudflare account/project or production URL has been selected in this session. Hosting creation and live verification remain at the user-controlled account/authorization boundary.
