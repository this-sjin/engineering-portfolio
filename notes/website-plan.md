# Engineering portfolio website plan

Prepared October 2, 2026. Planning only: no website implementation is authorized by this document. Keep `source-materials` read-only. This plan builds on [the content inventory](content-inventory.md) and [the detailed project evidence and conflict record](project-evidence.md), which identify the underlying files and review limits.

## Current project-page direction — October 3, 2026

The user has superseded the long case-study/report layout below. Future project pages should use the simplified Camera Rig format: title and one-line context, prominent real imagery, one or two short summary paragraphs, desktop quick-details sidebar (stacked after the summary on mobile), three to five contribution bullets at most, a clean captioned image gallery, and only a compact optional technical-notes block. Aim for a 30–60-second skim. Preserve individual/team attribution and meaningful limitations; omit unsupported metrics rather than adding long qualification sections. Keep the approved typography, colors, navigation, image enlargement, and accessibility.

Applied to all four primary project pages following the user’s request to simplify the remaining pages. Heven retains a compact text-led presentation with the public company logo because suitable public hardware imagery is unavailable. Primary pages and About already exist. Secondary full pages and deployment remain deferred.

## Approved amendments and first-stage scope

The user subsequently approved this plan and authorized a limited first implementation. These amendments take precedence over the original proposal below:

- `source-materials/personal-info.txt` is authoritative for contact, location, availability, preferred public links, and display preferences. A phone number appears only with explicit permission there; the current file says **Show phone number on website: Yes**.
- Resume navigation opens the current public PDF directly. No Resume landing page is part of the initial build.
- Heven content uses public-disclosure-safe information only. No internal Jira/Confluence material, proprietary screenshots, private documents, customer information, confidential specifications, or diagrams reconstructed from confidential material are published.
- The Projects index clearly separates the four visually emphasized primary projects from smaller secondary summaries.
- Stage one consists only of the visual system, header/footer, Home, Projects index, Camera Rig case study, shared CSS, minimal navigation JavaScript, and curated assets/provenance. The other full case studies, About, secondary pages, and deployment configuration remain deferred until visual review.

See [image and document provenance](image-sources.md) for the curated assets used in stage one.

The user additionally requested all projects from `Justin Portfolio 2.pdf`. The Projects index therefore includes the RoboGrinder large-quadcopter restoration and explicitly illustrated survey UAV 1/2/3 iterations. These expand the overviews while retaining the four primary projects' greater visual emphasis. This request does not change the deferred full-page build scope.

## 1. Direction and site structure

Build a small static portfolio that makes Justin's contribution, hardware, engineering decisions, and evidence easy to assess. Recruiters should understand the fit within a short homepage scan; engineers should be able to follow a case study from requirements through integration and validation. Avoid unsupported performance headlines, skill ratings, generic imagery, and pages that contain only a title and missing content.

Use the current **Drone Resume.pdf** for formal education, employment, and dates. Use final project documents for as-built configurations and measured results, retaining unresolved discrepancies rather than silently choosing a convenient claim. The cover letter supplies the practical voice: understanding the complete system and moving between CAD, fabrication, testing, and troubleshooting.

| Page | Purpose and contents |
| --- | --- |
| Home `/` | Positioning, four selected projects, evidence-linked capabilities, compact experience/education, availability, contact |
| Projects `/projects/` | Four principal case studies, then three compact additional-project summaries; identify personal, team, professional, and concept work |
| Four individual project pages | Camera rig; survey aircraft development; Heven UAV systems integration and performance modeling; modular quadcopter |
| About `/about/` | Brief engineering biography, current education, dated experience, teaching, supporting club work, optional personal interests |
| Resume `/resume/` | Simple current-resume download/view page with update date and contact link; provide an accessible download even if an embedded viewer fails |
| Contact `/#contact` | Homepage anchor and repeated footer links; no separate page or contact form needed |

Main navigation: **Projects · About · Resume · Contact**, with Justin Park linking home. About incorporates experience and capabilities rather than adding separate Experience and Skills pages. No blog, services page, awards page, or separate page for each aircraft generation at launch. Secondary project pages can follow when evidence warrants them.

## 2. Homepage hierarchy

### A. Header and hero

Use a restrained header and a text-led hero. Display **Justin Park** prominently, followed by the requested headline:

> Mechanical Engineer | UAV Systems | Robotics | Systems Integration

Suggested introduction, subject to normal editorial review:

> I design, build, and integrate mechanical and UAV systems, from airframes and mechanisms to avionics and electromechanical hardware. My work combines CAD, hands-on fabrication, and testing to understand how the complete system performs.

Below it: **M.S. Mechanical Engineering, Georgia Tech — expected May 2027**. Add a smaller availability line: **Seeking Spring 2027 internships and full-time roles starting Summer 2027**. Availability must be updated as the dates approach.

Primary CTA: **View engineering projects** → Projects. Secondary CTA: **Download resume** → current PDF. A quieter **Get in touch** link goes to Contact. Do not fill the hero with numerical claims drawn from unverified historical tests. An optional narrow completed-camera-rig photograph can accompany the text on desktop; it must retain its portrait framing and not overwhelm the introduction.

### B. Selected engineering work

Feature exactly these four entries, in this reading order:

1. **Stabilized camera rig for a quadruped robot.** Best documented end-to-end mechanical/electromechanical case study: requirements, gimbal and mast mechanisms, analysis, fabricated hardware, robot integration, and measured outcomes. Caption the system as a team capstone and state Justin's contribution separately.
2. **Autonomous survey aircraft development.** Strongest independent UAV story: successive airframes, landing gear, avionics integration, configuration changes, and flight testing. One case study shows the iteration rather than presenting each generation as a separate accomplishment.
3. **Heven UAV systems integration and performance modeling.** Recent professional evidence spanning avionics, companion computer, communications, configuration/documentation, and an engineering software tool. Combine the two workstreams so the same internship is not inflated into multiple featured projects.
4. **Modular quadcopter with 3D-printed components.** Connects mechanical frame work, assembly, electronics integration, autopilot configuration, and tuning. The qualified title avoids claiming that visibly mixed-material hardware is entirely printed.

Each card needs a title, work context, one sentence on contribution, two or three factual capability labels, and a descriptive case-study link. Three cards use real hardware imagery. Heven uses a deliberately text-led card with the same visual weight; do not insert a vendor aircraft image or invented wiring diagram. These four entries all belong in Selected Work even though their media differ.

### C. Technical capabilities

Use four short groups linked to examples, not an exhaustive keyword cloud:

- **Mechanical design and analysis:** SolidWorks, Onshape, mechanisms, mounting interfaces, structural analysis; link camera rig and quadcopter.
- **Prototyping and fabrication:** FDM printing, laser cutting, foamboard airframes, CNC-related team fabrication; distinguish personal work from team process.
- **UAV and electromechanical integration:** Pixhawk/PX4, QGroundControl, sensors, actuators, power, communications; link aircraft, quadcopter, and Heven.
- **Testing and engineering software:** hardware troubleshooting, flight testing, measured capstone validation, Python/Tkinter modeling; link the relevant case-study sections.

Do not display percentage proficiency bars. Name specific tools only where sources support their use; defer the disputed capstone controller model.

### D. Experience and education

Show a compact timeline: Heven Multirotors Engineering Intern, June–July 2026; current ME 4853 Graduate Teaching Assistant, August 2026–present; Experimental Flights VIP Airframe and Avionics Engineer, August–December 2024. Link About for the fuller record, including ME 2110 laboratory supervising grader, January 2025–May 2026.

Show M.S. Mechanical Engineering expected May 2027 and B.S. Mechanical Engineering completed May 2026, Highest Honors, Georgia Tech. GPA 3.96/4.0 may appear on About/Resume rather than dominating the homepage. Do not repeat the old site's undergraduate-student biography.

GT Supersonics does **not** need homepage placement. Keep it a brief supporting About entry focused on flight-sensor and RC integration. Do not lead with its thrust stand.

### E. Contact and footer

Invite discussion of mechanical, UAV, robotics, and systems-integration roles. Display email `justinpark0902@gmail.com`, LinkedIn `https://www.linkedin.com/in/justinpark-eng/`, phone `+1 (510) 513-5799`, and Pleasanton, CA, following the supplied preferences. Confirm location wording before launch because education is in Atlanta; do not infer relocation. Repeat resume and email links in the footer. Omit GitHub until a real profile is provided.

## 3. Project selection and editorial scope

### Primary projects

| Project | Engineering evidence and contribution to the portfolio | Scope and limits |
| --- | --- | --- |
| Camera rig | Mechanism selection, two-axis gimbal, mounting/isolation, SolidWorks analysis, printed/laser-cut hardware, controls and payload interfaces, measured validation | Separate Justin's documented gimbal/design/analysis work from teammates' mast CAD and testing ownership. Teleoperated capture is not autonomous quadruped navigation. Include missed extension-time target and final stair limitation. |
| Survey aircraft family | Independent ownership, configuration iteration, custom landing gear, low-budget airframe fabrication, autopilot integration and field testing | Organize three documented generations and explicitly identify the fourth as awaiting supporting material. Do not headline endurance/speed/span until version and evidence are reconciled. |
| Heven internship | Professional integration of existing UAV hardware, communications and flight configuration; Python/Tkinter physical-modeling work | Two sections in one page. Use publishable resume-level detail. Ticket assignment/completion alone does not prove whole-platform acceptance or deployed GPS-denied autonomy. No supplied model accuracy or code. |
| Modular quadcopter | CAD-to-hardware progression, modular components, mechanical/electrical integration, PX4 configuration and reported tuning | Clarify structural materials and Onshape/SolidWorks history. Simulation artifacts are not validated performance results. Keep separate from unidentified multirotor CAD. |

### Secondary projects

Launch the Projects index with concise illustrated summaries of **Boreas**, **Mind-inator**, and **RoboGrinder armor**, using available historical PDF imagery. State roles and evidence limitations rather than promising empty full case-study pages.

| Project | Why retain it | Recommended treatment |
| --- | --- | --- |
| Boreas SUAS aircraft | Carbon-frame fabrication, printed landing hardware, competition integration, aircraft/UGV context | Best eventual fifth case study. Clarify personal responsibilities and obtain original photos. Competition placing belongs to the team; do not imply authorship of autonomous software. |
| Mind-inator ME 2110 robot | Mechanisms, pneumatic/DC/solenoid actuation, Arduino sequencing, fabrication and constrained task execution | Strong robotics breadth. Use mechanism diagrams and completed robot; qualify historical reliability and distinguish design-review rank from overall competition results. |
| RoboGrinder armor | Fiberglass/CNC plate manufacture, weight reduction, mounting and competition hardware | Useful mechanical manufacturing evidence. Team fourth-place result does not validate the armor alone; omit precise load capacity pending clarification. |
| RoboGrinder quadcopter restoration | Replacement mount design, hardware modernization, PX4/telemetry integration | Supporting paragraph under older UAV/team work on About or Projects, not a separate launch page; it overlaps the stronger quadcopter story. |
| Vacuum parcel end-effector concept | Packaging, compliant vacuum handling, CAD, sensor placement, manufacturability and concept tradeoffs | Optional later concept-design entry, clearly labeled **CAD concept; not physically validated**. Particularly useful for mechanical/robotics applications, but not a substitute for built hardware. |
| Experimental Flights VIP tiltrotor | Structural concepts and Pixhawk integration on a team VTOL effort | Dated experience entry initially; promote only with attributable design images and project outcomes. |
| GT Supersonics avionics | Flight-sensor and RC integration/testing | Brief supporting experience only, honoring the user's emphasis. No thrust-stand case study. |

### Exclude from launch project pages

- Unidentified carbon-tube multirotor CAD archive: ownership, identity, relationship to other aircraft, and build status are unresolved.
- Duplicate documents, intermediate file revisions, vendor components, supplier gripper images, course templates, and prior-art references: supporting evidence, not separate accomplishments.
- Hobby PC/bicycle/audio/FPV work and Millbrae commercial-audio upgrades: optional biography or supporting employment context; insufficient case-study evidence currently.
- Teaching: valuable experience, but do not present student projects as Justin's engineering builds.

## 4. Reusable engineering case-study layout

Keep a short skim layer at the top and deeper evidence below. Aim for approximately 700–1,200 words for richer cases; a shorter honest Heven page is preferable to padded prose. Use a small in-page contents list for long pages.

1. **Title, context, and overview:** project purpose, date, personal/team/professional context, completed prototype versus ongoing development or concept. Hero hardware image when available.
2. **My role:** explicit personal responsibilities, team/sponsor credit, boundaries of ownership. Include a small facts row for verified tools and system scope.
3. **Problem and requirements:** user need and constraints. Distinguish initial targets from achieved results.
4. **Design and engineering decisions:** two to four meaningful choices, alternatives, reasoning, and consequences. Pair mechanisms or CAD with explanations.
5. **Analysis:** include calculations/FEA only when assumptions, units, boundary conditions and interpretation can be explained. Distinguish predictions from physical measurements.
6. **Prototyping and manufacturing:** materials/processes, revision sequence, assembly constraints and lessons from physical builds.
7. **Systems integration:** interfaces between structure, mounting, power, sensors, actuation, communications and control. Identify integration work versus writing an algorithm.
8. **Testing and results:** test method/conditions, observed result, requirement comparison, evidence and limitations. A compact target/result/status table is useful when supported.
9. **Lessons and next steps:** documented limitations and improvements. Ask Justin for personal reflections; do not invent a first-person lesson from the report.
10. **Selected supporting material:** only relevant public excerpts/downloads, plus next-project and contact links. Do not publish the complete archive.

Adaptations:

- **Camera rig:** use nearly all sections; combine design/analysis around gimbal and mast interfaces. Acknowledge final extension time of roughly 60 seconds normally/40 seconds maximum against the under-30-second target. Use measured height with its reference datum, and separate untested environmental/fatigue requirements. Correct erroneous FEA captions before publishing plots.
- **Survey aircraft:** use a generation timeline: problem observed → design change → build → reported flight behavior. Place shared avionics integration after the iterations. Avoid treating throttle percentage as measured efficiency or claiming delivered survey maps without outputs.
- **Heven:** split into integration/documentation and performance modeling. Describe the modeling inputs/outputs supported by the resume, not invented equations or accuracy. Testing/results remain brief until publishable evidence exists. Omit CAD/manufacturing sections that have no attributable evidence.
- **Quadcopter:** emphasize frame/component design → assembly → power/avionics → configuration/tuning. No numeric FEA, vibration, or flight-performance conclusion from file names alone.
- **Future concept page:** replace Manufacturing/Testing with proposed manufacturing and validation plan; make the unbuilt status visible near the title.

## 5. Image plan

Use source identifiers from `project-evidence.md`: **P** = historical five-page portfolio PDF; **F** = capstone final report; **FP** = final presentation; **FAB** = final fabrication package. Page/figure/slide locations below refer to those original files. Office media paths are internal ZIP members, not existing standalone image files. Extraction and site-image exports happen during a later build and must not alter originals.

### Camera rig

| Image | Source | Placement and purpose |
| --- | --- | --- |
| Completed rig on Unitree | FP slide 4, `ppt/media/image11.png`, 978 × 1304; F Figure 26 as alternate | Homepage card and project hero: establishes actual integrated hardware. Keep portrait orientation; do not crop out the robot/mast interface. |
| Team with prototype | FP `ppt/media/image14.png`, 1718 × 1289 | My role/team context; avoid using a team photo as sole evidence of personal responsibility. |
| Labeled gimbal | F Figure 11, `word/media/image11.png`, 974 × 828 | Design section: explain axes, camera balance, isolation and mounts. |
| Labeled mast/base | F Figure 12, `word/media/image20.png`, 980 × 806 | Mechanism and integration section; preserve labels. |
| Gimbal assembly drawing | FP slide 6, `ppt/media/image7.png`, 1532 × 1107; FAB p13 alternate | Manufacturing/assembly detail, readable full-width with optional enlargement. |
| Tripod/mockup and revised interfaces | F Figures 20–24; `word/media/image14.jpg`, 1536 × 2048 is a mockup candidate | Two or three images in an iteration sequence. Label earlier mockups so their stair behavior is not attributed to the final rig. |
| Roll-axis stress plot | F Figures 14–19; `word/media/image63.png`, 1250 × 674 | Analysis, only with corrected caption, modeled load and material assumptions; preserve legend/units. |
| Electronics diagram | FP slide 7 / F Figure 29 | Integration, after checking disputed controller/motor/driver labels. Omit or clearly qualify if the diagram is not as-built. |
| Reconstruction output | FP slide 8 / F Figure 31 | Results: illustrates capture outcome and visible artifacts, not a claim of distortion-free reconstruction. |

Missing: clear fabrication-in-progress photos, original measured test plots, and verified demonstration playback. The MOV is available but was not playback-verified; do not promise a working embedded video until checked. Use six to eight well-chosen figures rather than every available render.

### Survey aircraft development

| Image | Source | Placement and purpose |
| --- | --- | --- |
| Flying wing in workshop | P p2 upper, approximately 575 × 432 | Preferred project card/overview image; display moderately sized because the embedded original is small. |
| Flying wing outdoors | P p2 upper, approximately 274 × 364 | Field/build context within generation 3, not a full-width hero. |
| Conventional-tail aircraft and build detail | P p2 lower, approximately 512 × 384 images | Generation 2: show configuration and fabrication. |
| Tailwheel CAD | P p2 lower, approximately 312 × 341 | Mechanical design: steering and propeller-clearance decision. |
| First aircraft outdoors and gear render | P p4 lower, approximately 384 × 288 photos and 253 × 149 CAD | Generation 1: establish initial layout and suspension concept. |
| Mission screenshot/plot | P p4 lower, approximately 256 × 307 | Optional testing inset only if labels/meaning are readable and explained. It is not a substitute for flight logs. |

Missing: fourth-airframe image, original photographs, CAD overview, manufacturing sequence, readable flight logs and mapping outputs. Do not upscale these assets and imply additional detail; prefer contained figures with captions.

### Heven integration and modeling

**No project photography, application screenshot, validated performance plot, or public system diagram is supplied.** Use a text-led card and page initially. The best future additions are a permitted integrated-system photo, a simplified publishable interface diagram, a performance-tool screenshot, and a model-versus-test plot with conditions. Their planned placements are overview, integration, modeling, and validation respectively. These are requests for evidence, not existing assets. Do not use internal Jira screenshots, Confluence links, vendor aircraft photographs, or fabricated app UI as substitutes.

### Modular quadcopter

| Image | Source | Placement and purpose |
| --- | --- | --- |
| Completed outdoor quadcopter | P p1 lower | Preferred card and project overview: demonstrates a physical assembled system. |
| Frame CAD | P p1 lower | Design: component arrangement and modular interfaces. |
| Printed components and assembly photographs | P p1 lower | Manufacturing/build sequence and mechanical/electrical assembly. |

Native CAD is available in the **3D Printed Drone Frame** archive for later attributable renders, but no new render exists yet. Standalone commercial motor/propeller renderings are supplier references, not project hero assets. Missing: original high-resolution photographs, clear wiring/interface close-ups, flight-test images/logs, and interpretable analysis results.

Across the site: export curated copies to website assets, retain a source-to-export record in notes, write factual captions and useful alt text, and avoid generic stock imagery. Embedded PDF assets should be extracted at their native resolution; full-page screenshots add margins without restoring image detail.

## 6. Visual system

| Element | Recommendation |
| --- | --- |
| Layout | White/off-white background, clear left alignment, restrained section divisions, maximum content width about 1,160 px. Case-study prose approximately 65–75 characters per line; engineering figures can use the wider container. |
| Typography | System sans-serif stack such as Segoe UI/Arial; body 17–18 px with generous line height. Desktop hero 44–56 px, mobile 32–40 px. Use monospace sparingly for technical labels/values, never entire paragraphs. |
| Color | Background `#F7F8FA`, surface white, primary text `#18212B`, secondary text `#4C5967`, borders `#D6DEE6`, accent steel blue `#245B78`. Verify contrast during implementation. Use accent for links and primary actions, not decorative gradients. |
| Navigation | Short visible desktop navigation; simple keyboard-accessible mobile toggle if needed. Current-page indicator, visible focus styles, skip link. No complex dropdowns. |
| Cards | Two-column desktop selected-work grid, one column on small screens. Consistent title/context/description/link placement. Hardware photos above text; Heven text-led with deliberate typography and border treatment. No animated 3D cards or fabricated imagery. |
| Images | Hardware photos may be cropped for cards after checking key interfaces. Full case-study images retain meaningful composition. CAD/drawings/plots use contain sizing on neutral backgrounds; never crop dimensions or legends. Caption every technical figure. |
| Spacing | Consistent 8 px-based rhythm; page gutters around 24 px desktop and 16–20 px mobile; section gaps around 72–96 px desktop and 40–56 px mobile. Avoid oversized empty hero screens. |
| Mobile | Stack hero and grids, keep CTAs readable, preserve source order. Tables have a contained scrolling region if necessary; diagrams can enlarge without forcing whole-page horizontal scrolling. Aim for at least 44 px touch controls. |
| Motion | Optional subtle 150–200 ms hover/focus transitions only. Respect reduced-motion settings; no parallax, scroll-reveal dependencies, autoplay video, carousels, or decorative aircraft animation. |

The visual interest should come from real mechanisms, aircraft and annotated engineering evidence. Avoid a dark cockpit/radar theme or ornamental blueprint grids that make captions and analysis harder to read.

## 7. Content gaps and launch decisions

### Important before final copy is published

These affect truthfulness or attribution, but need not prevent layout work:

- **Capstone role:** confirm the personal/team split, especially mast CAD versus gimbal/design/analysis and test/integration contributions. Until clarified, use the final report's explicit credits and describe complete-system outcomes as team results.
- **Capstone configuration:** reconcile STM32 versus ESP32/BGC and final motor/driver combination. Either confirm the as-built system or omit disputed model names and diagrams. Correct FEA units/captions before showing plots.
- **Survey generations:** identify the fourth aircraft and resolve span/version mismatch. Without an answer, show the three documented iterations and omit conflicting dimensions and numeric endurance/speed claims.
- **Quadcopter identity/materials:** confirm mixed construction and CAD workflow; leave the unrelated unidentified archive out. Conservative wording permits a supported launch without solving every CAD revision.
- **Heven public scope:** confirm which details/images can appear publicly. Initial copy can stay at the supplied resume's level; private links, ticket identifiers and internal documentation are not website content.
- **Current location, availability and contact:** confirm for launch. Use primary-resume degree/employment dates, not the old student bio.

### Helpful but optional

- Original aircraft, quadcopter and competition photographs; highest-resolution source images improve presentation but are not prerequisites for building.
- Flight logs, aircraft specifications by generation, testing conditions/sample counts, actual survey outputs, and Heven model validation data. Add metrics only when the evidence supports them.
- Capstone mass definition, height datum explanation, vibration/angle logs, personally authored reflections and verified demonstration video.
- Individual roles, competition records, original CAD/code and test records for Boreas, Mind-inator and RoboGrinder.
- Approved app screenshots or interface diagrams for Heven; additional manufacturing and wiring close-ups for built projects.

### Can safely be added later

- Separate secondary-project case studies, parcel-effector concept page, new photographs or updated CAD renders.
- GitHub profile, public code repositories, personal-interest details, domain choice, and updated availability.
- Additional VIP/GT Supersonics evidence; retain the latter's secondary avionics emphasis.

No missing image, optional metric, or old competition result should hold up the entire build. Omit an unsupported claim/section rather than filling the gap with speculation.

## 8. Proposed static-site file structure

Keep the implementation under the existing empty `website` directory. This is a proposed tree only; none of these website files are created by this planning task.

```text
Engineering-Portfolio/
├── README.md
├── notes/
│   ├── content-inventory.md
│   ├── project-evidence.md
│   ├── website-plan.md
│   └── image-sources.md                 # later: export provenance/captions
├── source-materials/                    # unchanged, local reference archive
└── website/
    ├── index.html
    ├── projects/
    │   ├── index.html
    │   ├── stabilized-camera-rig/index.html
    │   ├── survey-aircraft/index.html
    │   ├── heven-uav-integration/index.html
    │   └── modular-quadcopter/index.html
    ├── about/index.html
    ├── resume/index.html
    ├── assets/
    │   ├── css/styles.css
    │   ├── js/main.js                   # only if navigation/enlargement needs it
    │   ├── images/
    │   │   ├── camera-rig/
    │   │   ├── survey-aircraft/
    │   │   ├── modular-quadcopter/
    │   │   └── additional-projects/
    │   └── documents/justin-park-resume.pdf
    ├── favicon.svg
    ├── 404.html
    ├── robots.txt                      # finalized when hosting/domain chosen
    └── sitemap.xml                     # finalized when public URLs are known
```

Use semantic HTML and one shared CSS file. Essential content and links should work without JavaScript. Small JavaScript may handle mobile navigation or figure enlargement; no runtime content fetch, framework, CMS, backend or build pipeline is warranted for this scope. Repeated navigation can remain simple static markup at this size. Use descriptive directory-based URLs and consistent links.

GitHub stores the repository; Cloudflare Pages serves only `website`, not the repository root or source archive. For a future Git-integrated Pages project: choose no framework, production branch matching the repository's actual branch, build command `exit 0`, and output directory `website` relative to the repository root. Cloudflare supports plain static HTML and Git-linked deployments/previews. See [Cloudflare's static HTML deployment guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/) and [Git integration documentation](https://developers.cloudflare.com/pages/configuration/git-integration/). No deployment configuration or publishing is performed now.

During implementation, create only curated public image/document copies. Do not expose receipts, passwords, internal Jira/Confluence material, or the entire CAD archive as downloads. Use a local HTTP preview for directory URLs; review deployed preview paths before launch.

## 9. Build order and review points

1. **Prepare content and selected assets.** Draft conservative project copy from evidence, resolve consequential attribution/configuration conflicts where possible, extract selected imagery into site assets, and record provenance. Leave unsupported details out.
2. **Global styles and navigation.** Implement type, spacing, colors, page containers, buttons, header/footer and accessible navigation. Establish desktop and mobile behavior.
3. **Homepage and Projects index.** Build the hierarchy above, four selected entries, capability links, concise experience/education and contact. Add the three secondary summaries without empty case-study links.
4. **One representative case study: camera rig.** Establish role attribution, annotated CAD, design decisions, manufacturing, integration and target-versus-result presentation.
5. **Review visual direction.** Inspect homepage and camera-rig page at desktop and mobile sizes. Review image clarity, reading density, personal/team credit and engineering depth before multiplying the template.
6. **Remaining primary pages.** Implement survey aircraft, modular quadcopter, then Heven's adapted text-led page. Keep the template flexible; do not add empty standard sections.
7. **About and Resume.** Finish current education/employment, supporting VIP/GT Supersonics avionics entries, teaching, downloadable resume and contact consistency.
8. **Responsive and accessibility refinement.** Check keyboard operation, focus, headings, alt text/captions, diagrams, tables, contrast, touch controls and reduced motion. Check links and essential content with JavaScript disabled.
9. **Final content and technical cleanup.** Review claims against sources; confirm no outdated degree wording or placeholders, compress images appropriately, check missing assets/404 behavior and metadata, and update the resume/availability. Configure a Cloudflare preview only during the later authorized build/deployment work.

The launch should communicate four credible engineering stories and a clear route to contact. Additional project pages and quantitative claims can follow when their evidence becomes available.
