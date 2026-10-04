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


## About portrait replacement — October 3, 2026

User-supplied photograph: `C:/Users/justi/AppData/Local/Temp/codex-clipboard-127ac0e3-6b62-417e-a835-184b6ed5af0f.jpg`. The user requested this as his About portrait. Public export: `website/assets/images/about/justin-graduation.webp`, 1367 × 911, RGB WebP quality 90, preserving the full composition without cropping, upscaling, or generative changes. EXIF orientation applied; source metadata is not carried into the public export. Source SHA-256: `2dd85b33775619c5f39126ee925965f5bbbbcf90037e2001eb3a82353b5cd470`. Export SHA-256: `c46fa1ac85010c446c91b70255b79cd51fae812a69ea6abba87e1f9a1b18389e`. Replaces only the About opening image and caption; the Camera Rig photograph remains on its project page. Uses existing image enlargement and responsive image styles. No source-materials files were changed.


### About portrait framing update

At Justin’s request, the About opening photo is now displayed in a larger portrait frame using CSS object-fit: cover and object-position: 92% 50%. Desktop height is 560 px; mobile height is 440 px. The public WebP remains unchanged, and the enlargement popup shows the full uncropped photograph. No raster edits or source changes.


## Camera Rig card hardware photograph — October 3, 2026

User-supplied photograph: `C:/Users/justi/AppData/Local/Temp/codex-clipboard-83454197-e3ff-40cf-a1ed-2640f65a30c7.png`. Public export: `website/assets/images/camera-rig/hardware-overview.webp`, 683 × 910, native-resolution RGB WebP quality 90, no cropping or generative edits. Used for the Camera Rig cards on Projects and Home in place of the gimbal CAD thumbnail. Full hardware remains visible using the existing contained image treatment. Source SHA-256: `9008a22e102817aca1f9c7679937386cd7aec3020232e378a74fbc13d92d97f8`. Export SHA-256: `951def1bd25358c04aff38f766795c159061b003b59d0831d56a224e3dcfd94e`. No source-materials files changed.


## User-uploaded homepage collage additions — October 3, 2026

Added all four supplied photographs to “A closer look at the work.” Native-resolution RGB WebP quality 90; no source-image cropping, upscaling, or generative changes. Existing collage thumbnails use CSS framing; enlargement shows each complete image. Descriptions identify visible hardware without assigning undocumented projects, responsibilities, or test outcomes. No source-materials files changed.

| Public asset | Supplied source | Pixels |
| --- | --- | --- |
| `website/assets/images/home-collage/avionics-closeup.webp` | `C:/Users/justi/AppData/Local/Temp/codex-clipboard-7e04595b-3951-4199-aba0-e7236efa68bb.png` | 958 × 719 |
| `website/assets/images/home-collage/aircraft-field-setup.webp` | `C:/Users/justi/AppData/Local/Temp/codex-clipboard-8a1ea839-84a9-471b-b498-ce4f6169b595.png` | 958 × 719 |
| `website/assets/images/home-collage/multirotor-assembly.webp` | `C:/Users/justi/AppData/Local/Temp/codex-clipboard-7536d3e7-30c5-41c5-85f4-dd98077c96e9.png` | 958 × 719 |
| `website/assets/images/home-collage/printed-quadcopter.webp` | `C:/Users/justi/AppData/Local/Temp/codex-clipboard-cdd51789-5863-4af9-b091-632b51e5a529.png` | 958 × 719 |

Source/export hashes and alt text: [uploaded-collage-sources.json](uploaded-collage-sources.json). Homepage collage now contains 36 photographs.


### Camera Rig card framing

At Justin’s request, Home and Projects Camera Rig card images now fill their thumbnail areas using CSS object-fit: cover and centered framing. The public hardware-overview.webp remains unchanged; thumbnail framing can crop portions of the full rig. Other project images retain their existing treatment.

### Camera Rig card photo replacement — October 3, 2026

Replaced the Home and Projects Camera Rig card image with the user-supplied `C:/Users/justi/Downloads/20251118_204342.jpg`. Public copy: `website/assets/images/camera-rig/camera-rig-card-photo.jpg`, 3000 × 2800, byte-identical JPEG. The card uses `object-fit: cover` and a centered 55% focal position to fill the thumbnail while keeping Justin, the quadruped robot, and the raised camera payload visible. The source image remains available uncropped in the public asset. Source/public SHA-256: `6160ed3c83d38ecf6354330b338edbcbce26ca326db0bdf76c240d126fe61b9c`. No source-materials files changed.

### Camera Rig card full-aspect revision

The user supplied a revised version at the same Downloads path and requested that its aspect ratio be preserved. The public `camera-rig-card-photo.jpg` is now a byte-identical 3000 × 2434 JPEG with SHA-256 `506d5a056a41413c32c6b81e3504f64e1b210f440a063e8cac536957a81cc00b`. Home and Projects display the complete photograph at its native 3000:2434 aspect ratio using `object-fit: contain`, with no crop or distortion.

The Camera Rig card media was subsequently returned to the shared 300 px desktop height so it aligns with the other three primary cards. `object-fit: contain` still preserves the complete photograph and its aspect ratio; the surrounding card-media background fills any unused horizontal space.

## Camera Rig displacement FEA — October 3, 2026

Replaced the Camera Rig gallery's roll-axis stress plot with the roll-axis displacement plot from Figure 18 of `source-materials/project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Report.docx`. The public copy is `website/assets/images/camera-rig/roll-displacement.png`, extracted byte-for-byte from the report's embedded `word/media/image19.png` at 1212 × 682. SHA-256: `4948f87fe5e129f1c75e1505067e6e4a9aaedf8a93812339c59f74d6cdcd6f12`.

The report identifies Figures 17–19 as static displacement analyses under the same assumed 1 kg payload used for the gimbal static simulations. The figure legend reports a maximum resultant displacement of 1.123 mm. The website caption uses those supported terms and units; it does not repeat the report caption's mistaken use of “stress” for a displacement plot. The prior `roll-stress.webp` remains in the public asset archive but is no longer referenced. No source-materials files changed.

### Base-fork displacement revision

At Justin’s request, the gallery now uses the base-fork displacement result from Figure 19 of the same final report instead. Public copy: `website/assets/images/camera-rig/base-fork-displacement.png`, extracted byte-for-byte from embedded `word/media/image4.png`, 1215 × 668, SHA-256 `34cf1ed84719dfd79e23f48c162440453cdc6ec827a8d0fbd66e7bc135fe2a87`. Its legend reports a maximum resultant displacement of 0.3567 mm under the report’s modeled 1 kg payload. The caption uses displacement terminology and millimeters rather than the report caption’s incorrect “stress” wording. The prior roll-axis displacement export remains unreferenced.

## Georgia Tech affiliation wordmark — October 3, 2026

User-supplied GT/Georgia Institute of Technology wordmark, copied byte-for-byte from `C:/Users/justi/AppData/Local/Temp/codex-clipboard-10227334-923b-4fe4-832b-6b9ff094c6d9.png` to `website/assets/images/education/georgia-tech-wordmark.png`. Dimensions: 1500 × 338, RGBA PNG with original transparency. SHA-256: `6b2625a43825f3d2f6261e938c1131cec747fe5123abf0e10a986d27e53abb4c`.

Used beside the homepage introduction's degree/availability information and the About page's Education heading. Native aspect ratio and original colors are preserved. The alternate seal wordmark was not needed. No source-materials files were changed.

### Homepage Camera Rig photo swap — October 3, 2026

At Justin's request, the homepage hero now uses `camera-rig/camera-rig-card-photo.jpg` (Justin beside the completed robot payload), and the selected-project Camera Rig card uses `camera-rig/completed-rig.webp` (hardware photograph). These are existing curated public assets; neither image file was modified. The Projects index and case-study image selections remain unchanged. Camera Rig cards now inherit the shared image heights at all breakpoints: 300 px desktop, 260 px laptop/tablet, and 280 px mobile. Images retain their native proportions with `object-fit: contain`.

## Final release image refinements — October 3, 2026

Replaced six small PDF-derived project photos with higher-resolution copies of the same hardware photographs already curated from the reference homepage. The underlying sources remain in `home-collage-sources.json`. No new engineering claims or invented visuals were added. Updated public HTML intrinsic dimensions to match.

| Project asset | Existing curated source | Native dimensions | SHA-256 |
| --- | --- | --- | --- |
| `survey-aircraft/flying-wing.webp` | `home-collage/reference-23.webp` | 1280 × 968 | `84214ff4232037b619df1ec7a5eeda3ee3fe037d10057e0e2952e47cee0111a8` |
| `survey-aircraft/aircraft-one.webp` | `home-collage/reference-06.webp` | 1278 × 798 | `7d9473a9944a61596fef260a12ca0c8ed167963763b128775a02fbfa18c6844e` |
| `survey-aircraft/aircraft-two.webp` | `home-collage/reference-09.webp` | 1280 × 960 | `0f27e1b02607fbac9948df07d6da3803e12b8701f4e3555a542282745878c7ef` |
| `survey-aircraft/flying-wing-field.webp` | `home-collage/reference-05.webp` | 953 × 1270 | `0684e1336b2c69bd9ee166cc04d3cc9833ce9680f142c0d7743a84f9f1d2c1cf` |
| `modular-quadcopter/completed-quad.webp` | `home-collage/reference-20.webp` | 1280 × 960 | `67941e9c297b61cf46c7de3ee96068f9c8fa2a654488aa256e95b2c0aa9db1fd` |
| `modular-quadcopter/frame-assembly.webp` | `home-collage/reference-21.webp` | 1280 × 960 | `e9286678be08cb53a39631f5618f4ef93f903bff077edebccfbcbfc9e6f38242` |
| `camera-rig/camera-rig-hero.webp` | `camera-rig/camera-rig-card-photo.jpg` | 3000 × 2434 | `d7d17a561015c4776ef152328b5437f05e6a876240407d1c875f9ddc34cb4467` |

The full-resolution 3000 × 2434 Camera Rig hero is now WebP quality 90: 846,196 bytes instead of the original JPEG’s 1,801,147 bytes (53% smaller). No crop, image generation, or geometry change was applied. The curated JPEG remains available; source materials were untouched. Technical drawings and FEA legends remain uncropped.

During the final privacy check, GPS metadata was found in that retained public JPEG. Removed its EXIF/XMP metadata segments without recompressing the JPEG image data and verified identical decoded RGB pixels. It is now 1,793,088 bytes, SHA-256 `73a5db0407f71a702a85d9d00c1010e80afaad07e320bfae81ad98098e2a52f9`. The earlier byte-identical-copy entries describe its pre-sanitization state. Original source/Downloads files were unchanged, and the WebP hero already contains no GPS metadata.

## Mind-inator report and presentation assets — October 3, 2026

All source files remain unchanged. Native image dimensions preserved; WebP quality 93; no cropping or generated imagery.

| Public asset | Read-only source and embedded image | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `mind-inator/competition-robot.webp` | `project-documents/ME 2110 final report/EMO - Final Presentation.pptx` → `image27.png` | 933 × 708 | `57e267f0980d6c0d39420ea458289f1ff2db1cf3be9fe4782a8d26b14ac5c6d2` |
| `mind-inator/retrieval-cad.webp` | `project-documents/ME 2110 final report/EMO - Final Presentation.pptx` → `image15.png` | 892 × 683 | `e33a7fcd6ffb5f49008571e8ebd946c0a840e50f7ea41f2005ca29d68e822f9e` |
| `mind-inator/scissor-lift.webp` | `project-documents/ME 2110 final report/EMO - Final Presentation.pptx` → `image26.png` | 1548 × 612 | `54aee3cc3fb022a389819fc435e982c658ad0e4ffc923701a3b5b85c5d865027` |
| `mind-inator/telescoping-lift.webp` | `project-documents/ME 2110 final report/EMO - Final Presentation.pptx` → `image24.png` | 1546 × 606 | `52a5eec57608cb63b14c30caa42a01f9db6ce8e6bf3c2769bbd849795859598f` |
| `mind-inator/assembled-robot.webp` | `project-documents/ME 2110 final report/Team EMO - Final Report.docx` → `image69.png` | 953 × 1270 | `c1eaf7cbce89f4db288ac990ad2f95d728b5ac4a0bf4e80d75cbe60e51d7ac6d` |
| `mind-inator/lift-test.webp` | `project-documents/ME 2110 final report/Team EMO - Final Report.docx` → `image65.png` | 1191 × 1073 | `7b6b7bc867383dae37d57371e57898835d763b0d73a62f0659f3da488c774f87` |

### Mind-inator gallery revision — October 3, 2026

Selected the final-report Figure 17 for the lead photograph and the slide 26 preferred-design render for the second highlight. Moved the previous highlights into the lower gallery. Slide 18 and 22 figures include their original labels; crops exclude slide titles and unrelated text, without cropping mechanism labels. WebP quality 93; no generated imagery or source-file changes.

| Public asset | Source in `project-documents/ME 2110 final report/` | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `mind-inator/scissor-push-labeled.webp` | EMO - Final Presentation.pptx.pdf, slide 18; figure crop (364, 98, 715, 383) PDF points, rendered at 300 dpi | 1462 × 1188 | `677aa98f23fd5d66b2c2ed75eff4a97577318475389a28f33eb80a0a3c26c9fe` |
| `mind-inator/sadness-lift-labeled.webp` | EMO - Final Presentation.pptx.pdf, slide 22; figure crop (196, 78, 547, 399) PDF points, rendered at 300 dpi | 1462 × 1337 | `31ecbc04446abbd79189682e75e6231b41a386877fdd8ebd5f6ce2515618b518` |
| `mind-inator/preferred-design.webp` | EMO - Final Presentation.pptx.pdf, slide 26; figure crop (390, 132, 674, 350) PDF points, rendered at 300 dpi | 1183 × 908 | `a4b1e7f9651dac52626fe16e4bc8470dae5d1aac63d1e6f1377fe4a8d756359b` |
| `mind-inator/final-competition.webp` | Team EMO - Final Report.docx, Figure 17; word/media/image8.png (rId28) | 756 × 837 | `bb94f0722867d02c6c6f8caa7bc63f8e9fc61d75512968e644ddd64e3049acc4` |

## Sway Less public figures — October 3, 2026

Read-only source folder: `project-documents/ME 4012 Final Project Sway Less/`. The 31-slide `ME 4012 Presentation - Sway Less .pptx` is the completed deck; the underscore-named deck contains draft/template material. Curated figures preserve complete labels and native proportions, WebP quality 93. No generated imagery, source edits, private documents, or video downloads.

| Public image | Source | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `sway-less/prototype.webp` | Final presentation, slide 30, ppt/media/image13.png | 1053 × 766 | `bb8287433d3f0482a568f96b9edbfbea56984a6080122f3a1ecf58d2b7948cb4` |
| `sway-less/cad.webp` | Final presentation, slide 31, ppt/media/image49.png | 925 × 836 | `fd582558aec84f69fbdefb76d759eca0ce0bdeeaedf1b6ad983b8e23c73b5f16` |
| `sway-less/electronics.webp` | Final presentation, slide 30, ppt/media/image14.png | 1056 × 770 | `66113fd6713f943de843ea067852c54917e00d8b570923bb987363747a988925` |
| `sway-less/motor-side.webp` | Final presentation embedded ppt/media/image17.png; same labeled figure as Project Update 2 Figure 3 | 1051 × 774 | `7868275e15cc8e5126f10fd103d0a121ee94a0545f999668b7ab68b910b59a44` |
| `sway-less/control-diagram.webp` | Other Files/Final Block Diagram-1.png; also final presentation slide 8 | 1700 × 608 | `0893559535f08a6e25bb7be0535c133070fbe8d5896e523fad8e34cebe6ca6ae` |
| `sway-less/bode.webp` | Final presentation, slide 9, ppt/media/image18.png | 1217 × 790 | `2ff5aa23420011c0b0a50790a6504928120751df2393f200b76d33f0dffcd18a` |
| `sway-less/root-locus.webp` | Final presentation, slide 14, ppt/media/image27.png | 1239 × 785 | `1421e8a38bb0cf3702526515a653469d637d381a9527567807c94fac9d10cbef` |
| `sway-less/simulated-recovery.webp` | Final presentation, slide 19, ppt/media/image34.png | 952 × 624 | `e8ee38969351140b3c17ae749edb229bf1e01bc845aa5e895e661e388670ade1` |

### Sway Less lead photo and electronics layout revision

Promoted the existing `sway-less/electronics.webp` photograph to the project lead, Selected Work thumbnail, and social preview. Replaced its original gallery position with `sway-less/electronics-layout.webp`: faithful PowerPoint PNG export of slide 5, Electronics Layout, from a read-only scratch copy of `ME 4012 Presentation - Sway Less .pptx`, re-encoded WebP quality 93 at 2400 × 1350. Entire original slide preserved, without redrawing or cropping. SHA-256 `e2dff856650e040d773032b4368b80f16c46f7e42cc37eb47ac34608b0d41070`. Source deck unchanged.

## Survey Aircraft flight-log screenshots — October 4, 2026

User-supplied screenshots deliberately selected for public display. Byte-identical PNG copies, complete plots/legends/map attribution preserved. No crop, image generation, measured-performance inference, or source-materials changes. Aircraft configuration and flight date are unspecified.

| Public image | User attachment | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `survey-aircraft/flight-path-log.png` | `codex-clipboard-4eba9a66-2f6e-46b0-8e12-332ffc323407.png` | 1008 × 970 | `f59d9a219ad2f04195f92940e9030507d7baa984bc72b37d73784dc64108a0ce` |
| `survey-aircraft/altitude-log.png` | `codex-clipboard-9ecf077b-7028-409c-b09d-ebf6315e1a06.png` | 848 × 407 | `ab30c200bc87b7f9da6a94139921d74ac8e09b309a7ceb18de2e3f021143b0e9` |
