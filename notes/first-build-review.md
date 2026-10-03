# First implementation review

**Historical stage-one record:** After visual approval, the remaining primary case studies and About were completed. Current seven-page scope and verification are recorded in `primary-build-review.md`. The three-page scope below describes the initial build review.

Reviewed October 3, 2026. Scope: Home, Projects index, Camera Rig case study, shared navigation/footer, CSS, JavaScript, and public assets. No additional pages or deployment configuration were created.

## Follow-up QA after the supplied portrait

Repeated the full three-page review at all four widths after adding Justin's photograph. The original visual direction and page scope are retained. This pass also exercised actual mobile navigation from Home to Projects to Camera Rig to Contact, the resume download, desktop/mobile resizing, and navigation without JavaScript on every page.

Additional fixes:

- Reset the mobile menu on crossing into desktop navigation so returning to mobile starts with a closed menu and accurate `aria-expanded` state.
- Indicated Projects as the current navigation location while viewing its Camera Rig case study.
- Updated the Camera Rig image-source sentence to include the user-supplied photograph. Its caption identifies Justin without implying sole ownership of the completed system.
- Renamed the results region's accessible label to “Camera Rig testing results,” which also makes sense in the stacked mobile layout.
- Removed redundant mobile font/figure/grid declarations, reused the shared image sizing for the Heven logo, and combined identical collage span rules. Mobile section links inherit their shared flex alignment. CSS/JS cache versions now match across the three pages.

The new photo decodes and enlarges correctly at 1440, 1024, 768, and 390 px. Tab/Shift+Tab remain on Close; Escape restores focus to the original photo link. No larger layout redesign or additional engineering claims were needed. Continue to visually review the long homepage collage, tablet reading density, and the portrait placement in the integration section.

## Verification

- Exercised all three directory routes in Microsoft Edge at **1440, 1024, 768, and 390 px**, with rendered screenshot review. No page-level horizontal overflow, missing images, or broken card layouts. Technical figures remain contained; mobile results keep each result beside its qualification.
- Checked **74 distinct local URLs**, including relative navigation, directory routes, assets, resume PDF, favicon, and fragment destinations. All resolve. No console or script errors after fixes.
- The main Resume link opens the public PDF directly; Home also offers download. The public PDF is byte-identical to the resume designated in `personal-info.txt`.
- Contact URLs, location, availability, and display preferences match `personal-info.txt`, which explicitly permits phone display. Verified mailto/tel syntax and the supplied LinkedIn destination. No messages/calls were initiated; external account availability was not authenticated.
- All pages have one H1, no skipped heading levels, and descriptive image alt text. Keyboard checks cover skip-to-content focus, mobile menu activation/Escape/focus return, image activation, modal focus wrapping, dismissal, and restored image-link focus. Normal image clicks trigger no download or browser-tab navigation.
- Key navigation/action/footer/capability/figure links have at least 44 px height; footer links also have 44 px minimum width. Focus indicators are visible. Navigation works without JavaScript. Reduced motion disables smooth scrolling/transitions. Mobile table/row-header semantics remain exposed in Edge's accessibility tree.
- Checked palette contrast: minimum **5.87:1** for the implemented text colors on checked light surfaces; white on accent **7.39:1**. This practical review does not substitute for testing additional browsers or assistive technologies.

## Fixes

- Stacked Home and Camera Rig heroes at narrow tablet widths. Relaxed the desktop hero heading width to reduce fragmented wrapping.
- Made secondary project summaries one column below 950 px for readable tablet descriptions. Four primary cards retain greater visual emphasis.
- Changed card and survey-iteration images to contain sizing, preserving complete aircraft/interfaces. Technical plots/drawings and enlarged images remain uncropped. The requested varied collage retains its presentation crops and three-column mobile grid; technical tiles use contain sizing.
- Enlarged touch targets, extended focus styles to the results region, and made the main content a working skip-link focus destination.
- Wrapped Tab/Shift+Tab on the modal's sole interactive control, Close. Escape/backdrop dismissal and restored focus remain intact. Enhanced figure links say “Enlarge image” instead of implying a new tab.
- Added a locally authored JP favicon matching the header, eliminating the missing-favicon request. Updated asset cache versions across all three pages.
- Removed obsolete text-only Heven CSS and the unused monospace utility; consolidated secondary-grid rules and removed the superseded mobile table minimum width/redundant declarations. Cleaned class whitespace and put stylesheet rules on separate lines. No inline styles, frameworks, or dependencies were added. JavaScript serves only the menu and image viewer.
- Changed the Projects label to “Four primary projects” to avoid implying four complete case studies. Removed internal editing instructions from technical captions and tightened copy without introducing facts.

## Content review

Compared copy against the approved plan, current resume, cover letter, personal information, project-evidence notes, and capstone final report/presentation. Home retains the approved hierarchy with the subsequently requested collage after selected work.

The Camera Rig page distinguishes Justin's requirements/concept/analysis/final-design work and gimbal CAD/drawings from Matthew's mast work and Jeffrey's testing/integration. Complete-system outcomes remain team results. It explains requirements, mechanism choices, analysis assumptions, prototypes, manufacturing, integration, testing, and next-iteration implications.

Copy correctly describes teleoperated capture, a two-axis gimbal, measured height datum, the missed extension-speed target, reconstruction artifacts, final stair limitation, and untested environmental/fatigue requirements. The 8.110 MPa value follows analysis text/plot rather than the inconsistent caption. No distortion-free, autonomous-navigation, blanket-compliance, or universal safety-factor claims were introduced. Heven remains at public resume detail; GT Supersonics remains deemphasized.

## Source safety

- SHA-256 comparison confirms **all 945 original source files retain their paths and bytes**. The archive now has 946 files because the Boreas paper was previously added at the user's request. This review changed no source files.
- Public files contain no source-directory references, absolute workspace paths, Jira/Confluence links, internal documents, customer material, private spreadsheets, CAD archives, or diagrams derived from confidential information.
- Assets comprise shared CSS/JS, one deliberately selected public resume, 51 curated raster images (including Justin's supplied portrait), and the JP SVG favicon. Provenance is in `image-sources.md` and `home-collage-sources.json`. The former Boreas flight photo remains a deliberately curated, currently unused public asset.

## Items for Justin's visual review

- Review tablet hero stacking, full-image card previews, primary/secondary balance, and the Heven logo treatment.
- The requested 32-image collage makes Home longer. Every image remains included with lazy loading and enlarged views. Decide whether its length and preview crops suit recruiter skimming. Exports total approximately 7.9 MB; a later size pass could reduce transfer cost while retaining every photo.
- Older aircraft/robot images remain limited by PDF resolution. Full-resolution originals would improve current cards. A closer final-rig photo would reveal more hardware than the hallway hero.
- Collage alt text describes visible scenes without unverified project/ownership attribution. Review people and context before public launch.

## Unresolved facts and useful additions

- **Camera Rig:** confirm as-built controller and motor/driver models; whether 6.5 kg includes the camera; and your assembly/integration/testing contribution beyond the final-report credits. Disputed models remain omitted; mass ambiguity remains explicit.
- Raw angular data, test conditions/sample counts, a public demonstration video, wiring/integration photos, and fabrication close-ups would strengthen the existing case study. These are optional improvements rather than blockers for visual approval.
- **Survey overview:** the resume reports four airframes, while the historical PDF documents three; dimensions conflict between versions. The index presents three documented historical iterations and omits disputed dimensions/performance metrics. The fourth aircraft's identity/photo can follow later.
- The unchanged public resume itself includes broader Camera Rig claims and a controller identification that conflict with the final report. Review those resume statements separately before final publication. Website copy remains conservative.

Only the three approved pages exist. Remaining case studies, About, secondary pages, and deployment are deferred pending Justin's visual approval.
