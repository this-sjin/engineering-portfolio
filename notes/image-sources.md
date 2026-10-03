# Public image and document provenance

Stage one, October 2, 2026. Sources were read only. Public assets are curated copies under `website/assets/`; no public page references `source-materials`. No Heven/internal imagery is exported.

## Image exports

**First-build review, October 3:** Added `website/assets/images/site-mark.svg`, a locally authored JP monogram matching the header (64 × 64 SVG view box, graphite background, white Arial letters). It is a favicon, not an engineering image. Existing curated raster files were unchanged. Card/iteration previews now use contain sizing; full-size images remain uncropped. Modal keyboard focus and touch-target sizing were refined. See `first-build-review.md` for review results.

**Heven logo addition:** At the user's request, replaced the text-led internship card media on Home and Projects with the supplied Heven Aerotech logo. `website/assets/images/heven/heven-aerotech-logo.png` is an unchanged 784 × 410 PNG copy of `C:/Users/justi/AppData/Local/Temp/codex-clipboard-bb331dec-34dd-4f20-944b-f072ec84279b.png`. It is presented with contain sizing and whitespace, without cropping or modification. This is employer branding supplied by the user, not project photography or an internally reconstructed diagram. No Heven technical copy or private source material changed.

Images extracted at native resolution; images larger than 1,600 px were proportionally reduced to that bound. Photos use WebP quality 88; drawings/plots use lossless WebP. Transparent pixels are composited onto white; no generative alteration, geometry changes, added technical labels, or invented content. No crops baked into exports. CSS contains technical images; selected card photos use cover framing.

| Public asset | Original source (relative to source-materials) | Embedded locator | Native → export pixels | Subject / use |
| --- | --- | --- | --- | --- |
| `website/assets/images/camera-rig/completed-rig.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Presentation.pptx` | `ppt/media/image11.png` | 978 × 1304 → 978 × 1304 | Completed camera rig on quadruped; final presentation, slide 4 |
| `website/assets/images/camera-rig/team.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Presentation.pptx` | `ppt/media/image14.png` | 1718 × 1289 → 1600 × 1200 | Capstone team and prototype |
| `website/assets/images/camera-rig/gimbal.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Report.docx` | `word/media/image11.png` | 974 × 828 → 974 × 828 | Labeled gimbal; final report Figure 11 |
| `website/assets/images/camera-rig/mast.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Report.docx` | `word/media/image20.png` | 980 × 806 → 980 × 806 | Labeled mast/base; final report Figure 12 |
| `website/assets/images/camera-rig/assembly.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Presentation.pptx` | `ppt/media/image7.png` | 1532 × 1107 → 1532 × 1107 | Gimbal assembly drawing; final presentation slide 6 |
| `website/assets/images/camera-rig/mockup.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Report.docx` | `word/media/image14.jpg` | 1536 × 2048 → 1200 × 1600 | Early printed mounting interface, not final rig |
| `website/assets/images/camera-rig/roll-stress.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Report.docx` | `word/media/image63.png` | 1250 × 674 → 1250 × 674 | Roll-axis stress plot; preserve 8.110 MPa plot value, correct erroneous report caption |
| `website/assets/images/camera-rig/reconstruction.webp` | `project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Presentation.pptx` | `ppt/media/image10.png` | 1234 × 692 → 1234 × 692 | Reconstruction output; final presentation slide 8 |
| `website/assets/images/survey-aircraft/flying-wing.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `2:X14.png` | 575 × 432 → 575 × 432 | Flying wing in workshop; PDF page 2 upper |
| `website/assets/images/modular-quadcopter/completed-quad.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `1:X20.png` | 384 × 288 → 384 × 288 | Assembled quadcopter outdoors; PDF page 1 lower |
| `website/assets/images/additional-projects/boreas.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `3:X20.png` | 767 × 578 → 767 × 578 | Boreas flight photograph; PDF page 3 upper |
| `website/assets/images/additional-projects/boreas-field.webp` | `project-documents/Boreas SUAS 2022/auvsi_suas-2022-journals-amador_valley_high_school.pdf` | PDF page 1, embedded `Im1.jpg` | 961 × 721 → 961 × 721 | Current Boreas overview image: completed aircraft in a field, with frame and landing gear clearly visible |
| `website/assets/images/additional-projects/armor.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `3:X18.png` | 383 × 508 → 383 × 508 | Fabricated armor mounting plates; PDF page 3 lower |
| `website/assets/images/additional-projects/mind-inator.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `5:X16.png` | 286 × 381 → 286 × 381 | Completed Mind-inator robot; PDF page 5 top right |
| `website/assets/images/additional-projects/robogrinder-restoration.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `4:X17.png` | 512 × 344 → 512 × 344 | Large VT RoboGrinder quadcopter on workshop bench; restoration overview |
| `website/assets/images/survey-aircraft/aircraft-one.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `4:X19.png` | 384 × 288 → 384 × 288 | First survey airframe; UAV 1 iteration overview |
| `website/assets/images/survey-aircraft/aircraft-two.webp` | `old-portfolio/Justin Portfolio 2.pdf` | `2:X37.png` | 512 × 384 → 512 × 384 | Conventional-tail survey airframe; UAV 2 iteration overview |

## Historical portfolio coverage update

At the user's request, the Projects index now explicitly represents all nine project entries from `Justin Portfolio 2.pdf`:

| PDF entry | Site representation |
| --- | --- |
| Stabilized camera rig (p1) | Primary card and full Camera Rig case study |
| FDM quadcopter (p1) | Primary Modular Quadcopter overview |
| Survey UAV 3 (p2) | Survey family primary card and illustrated iteration 3 |
| Survey UAV 2 (p2) | Illustrated iteration 2 within the survey family |
| Boreas (p3) | Secondary team-project overview |
| Armor mounting (p3) | Secondary RoboGrinder armor overview |
| Large-scale quadcopter (p4) | Added secondary RoboGrinder restoration overview |
| Survey UAV 1 (p4) | Illustrated iteration 1 within the survey family |
| Mind-inator (p5) | Secondary robot overview |

The four primary projects retain larger cards and images. Three survey iterations remain one development family; restoration remains distinct from the personal modular quadcopter. New copy uses documented design/fabrication/integration scope and omits unsupported performance numbers. Three added photos are native-resolution WebP copies using the same export method above; no source files were modified. No additional full case-study pages were created.

## Resume

`website/assets/documents/justin-park-resume.pdf` is a byte-identical copy of `source-materials/resume/Drone Resume.pdf`, the public resume specified in `personal-info.txt`. Navigation opens the PDF directly; homepage CTA offers download. No separate Resume page.

## Copy authority and exclusions

- `personal-info.txt` is authoritative for contact, location, availability, public links and display preferences. It explicitly says **Show phone number on website: Yes**, so stage one displays the number. No GitHub link is present.
- Current resume supplies formal dates/education and the Heven public overview. No Jira/Confluence details, private names, proprietary diagrams, specifications or screenshots are included.
- Camera-rig team credit follows final-report section 16. Technical outcome copy follows the final report; disputed controller/motor models and blanket compliance claims are omitted.
- Roll stress caption uses the plotted 8.110 MPa maximum, not the erroneous 6.110 MPa caption. No environmental/fatigue certification claims are made.
- The extracted `image14.jpg` is visually an early printed interface, not the taped-tripod mockup. The public caption reflects the actual image.
- Historical PDF page 1 `X20.png` is the completed outdoor quadcopter. `X22.png` is assembly work and was not exported as the completed-aircraft card.
- Older image resolution is limited. No upscaling restores detail; no vendor imagery or full source documents are exposed.

## Scope

Only Home, Projects index, and Camera Rig case study exist. Survey Aircraft, Heven and Modular Quadcopter are overview cards; their full case studies, About, secondary pages, and deployment configuration are intentionally deferred.

## Stage-one verification

### Boreas paper and photograph update

At the user's explicit request, added the 10-page AmadorUAVs 2021–2022 SUAS technical design paper to `source-materials/project-documents/Boreas SUAS 2022/`. The added PDF is byte-identical to the file supplied from Downloads; all 945 pre-existing source files remain unchanged. Adding this document is the user-authorized exception to the earlier reference-only archive rule.

The Projects index now uses the cover-page hardware photograph, extracted at native 961 × 721 resolution and converted to WebP quality 88 without cropping, enhancement or generative changes. It replaces the distant flight photo in the public page; the older `boreas.webp` export remains as an unused historical asset. The new descriptive filename prevents reuse of the old cached image. The paper credits Justin as one of the team contributors; no additional individual responsibilities or numerical results were inferred from team content.

- Compared SHA-256 snapshots before and after implementation: all 945 source files and their paths are unchanged. The public resume copy is byte-identical to the designated source PDF.
- Reviewed all three pages in Edge at 1440 px desktop and 390 px mobile widths, plus the homepage at 320 px with JavaScript disabled. All pages have one main heading, no page-level horizontal overflow, and no missing images or browser script errors.
- Checked every local link, image, stylesheet, script, resume link, and anchor target. Mobile menu opening and Escape dismissal pass; navigation remains visible without JavaScript.
- Visually reviewed imagery, primary/secondary hierarchy, gimbal drawing framing, and mobile result/limitation presentation. Text colors exceed 4.5:1 against the implemented light surfaces. These checks are not a comprehensive accessibility audit.
- Local review server: `http://127.0.0.1:8765/`, serving only `website`. No production deployment performed.

## Reference-homepage collage — October 3, 2026

**Layout revision:** Replaced the vertical column layout with a compact CSS Grid collage at the user's request: four columns on desktop, three on tablet/mobile, varied tall and larger featured tiles, and tighter gutters. Preview tiles use presentation-only cover cropping; analysis/assembly images and the closing mobile team image use contain sizing. All full-size files remain unchanged and linked. Verified all 32 images, varied tile dimensions, and no page overflow at 1440, 800, 390 and 320 px. This supersedes the original natural-proportion preview layout described below.

**Image-viewer revision:** Clicking collage images or Camera Rig figure-enlargement links now opens a native on-page modal with the uncropped local image and descriptive caption. Close button, Escape, and backdrop dismissal return focus to the original image link and restore scrolling. Desktop/mobile browser checks confirm no download or page navigation during normal clicks. Direct-image links remain a fallback without JavaScript; original assets are unchanged.

At the user's request, all **32 image elements** from the public [Google Sites reference homepage](https://sites.google.com/view/justin-sejin-park-portfolio/home) were recovered through its public browser image responses and added to the new Home page. The 32 recovered images have 32 distinct pixel contents. All images are stored locally under `website/assets/images/home-collage/`; public HTML has no dependency on the Google image URLs.

Exports retain the delivered source dimensions (up to the reference site's 1,280-pixel image-size request), with WebP quality 86 and transparent pixels composited onto white. No crops, generative edits, added labels or altered engineering content. The collage preserves each image's natural proportions and links to its full local export. Alt text describes visible content; unverified project identity, individual authorship, and numeric results are not inferred. The frame-analysis screenshot is illustrative source material, not a new validation claim.

[Machine-readable provenance](home-collage-sources.json) records each local filename, reference image index, original public image URL, pixel dimensions, descriptive alt text, and original/export SHA-256. Source URLs may be temporary Google signed URLs; the durable reference is the public homepage plus its image index and downloaded-image hash. Existing `source-materials` files were not modified or supplemented.

## Justin with the Camera Rig — October 3, 2026

Layout update: the simplified Camera Rig page places this photograph in the prominent opening image pair. All nine existing Camera Rig images retain their original exports and provenance; no new assets were created for the simplification.

User-supplied photograph: `C:/Users/justi/AppData/Local/Temp/codex-clipboard-a3a7be60-77fd-4410-a26c-a7e7509d92be.png`. The user explicitly identified the pictured person as himself. Export: `website/assets/images/camera-rig/justin-with-camera-rig.webp`, 978 × 1304, native-resolution RGB WebP quality 88, without cropping or generative edits. Source SHA-256: `d03329291a42261589d980ee57cc9a274e5c904eb4ef01e089d3be3307779425`. Export SHA-256: `b3dd405cf37679ad73aa0cfacfbf5a1de42e171ec0078b89870e1242d238bf76`. Added to the existing Camera Rig systems-integration section with a caption identifying Justin and crediting the completed rig to the team. It uses the shared enlarged-image popup. No source-materials files were changed.

## Remaining primary pages — October 3, 2026

Added seven native-resolution image excerpts from the historical public portfolio PDF. Photographs use WebP quality 88; CAD uses lossless WebP. Transparency is composited onto white. No crops, upscaling, generative edits, or reconstructed diagrams. Existing public assets are reused for overview hardware, the Heven company logo, and the identified Justin portrait on About. No private company material or native simulation output was exported.

| Public asset | Source / locator | Pixels | Purpose |
| --- | --- | --- | --- |
| `website/assets/images/survey-aircraft/suspension-gear-cad.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 4, X18.png | 253 × 149 | First-aircraft suspension landing-gear CAD |
| `website/assets/images/survey-aircraft/tailwheel-cad.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 2, X35.png | 312 × 341 | Second-aircraft steerable tailwheel CAD |
| `website/assets/images/survey-aircraft/tailwheel-build.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 2, X36.png | 512 × 384 | Second-aircraft tailwheel and airframe fabrication |
| `website/assets/images/survey-aircraft/flying-wing-field.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 2, X15.png | 274 × 364 | Third-aircraft flying wing outdoors |
| `website/assets/images/modular-quadcopter/frame-cad.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 1, X21.png | 301 × 168 | Custom frame CAD with modular mounts and tube arms |
| `website/assets/images/modular-quadcopter/frame-assembly.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 1, X22.png | 384 × 288 | Printed frame components and tube arms during assembly |
| `website/assets/images/modular-quadcopter/arm-components.webp` | `old-portfolio/Justin Portfolio 2.pdf`, page 1, X23.png | 213 × 284 | Separate arm tubes and printed motor-mount components |

Export hashes and locators: `primary-page-image-sources.json`. The survey mission screenshot/plot was intentionally not exported because its scale/test context is insufficient for a technical interpretation. Vendor motor/propeller reference renders and unvalidated simulation plots are not used as personal project evidence. All source files remain read-only.
