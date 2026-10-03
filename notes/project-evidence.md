# Engineering project evidence and source conflicts

Reviewed October 2, 2026. This record supports the [content inventory](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/notes/content-inventory.md>) and proposed future project pages. It identifies **12 named projects or workstreams plus one unidentified CAD study**. The survey aircraft is one project family with three documented historical generations and a fourth claimed in the current resume. Heven integration and modeling are separate substantial workstreams within one internship. GT Supersonics was added after a historical resume appeared during review.

**Evidence language:** “reported” means stated by a supplied source, not independently reproduced. Team results do not establish sole personal ownership. Missing details stay missing. No website implementation is included.

## Principal project sources

| Key | Source |
| --- | --- |
| R | [Current Drone Resume](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/resume/Drone Resume.pdf>) |
| A | [Academic Resume](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/resume/Academic Resume.pdf>) |
| O | [Historical Resume](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/resume/old resume.pdf>) |
| C | [Cover Letter](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/cover-letter/Drone Cover Letter.pdf>) |
| P | [Historical Portfolio PDF](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/old-portfolio/Justin Portfolio 2.pdf>) |
| F | [Capstone Final Report](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Report.docx>) |
| FP | [Capstone Final Presentation](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Final Report/Atlanta Dynamics - Final Presentation.pptx>) |
| F2 | [Capstone Second Progress Report](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Report 2/Atlanta Dynamics - Second Progress Report.docx>) |
| F1 | [Capstone First Report Reference](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Report 2/Report 1 (Reference).docx>) |
| FAB | [Final Fabrication Package](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Final Report/Fab/Atlanta Dynamics - Final Fabrication Package.pdf>) |
| BOM | [Final Bill of Materials](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Final Report/Final Bill of Materials.xlsx>) |
| GUIDE | [Capstone Start Guide](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Capstone Fall 25/Final Report/Height Change Mechanism Start Guide.docx>) |
| J | [Heven Jira CSV](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Heven Aerotech Jira Tickets/Jira (1).csv>) |
| E | [Parcel End Effector Presentation](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Intern Take Home Project/Justin Park Intern Take Home Project.pptx>) |

## 1 Stabilized height adjustable camera rig for a quadruped robot

**What:** August–December 2025 interdisciplinary capstone for Aetos Imaging. Atlanta Dynamics developed a height-adjustable, actively stabilized camera payload for a teleoperated Unitree Go2 Pro to collect images for 3D reconstruction. It was a delivered prototype/MVP, not demonstrated autonomous robot navigation. Sources: R, C, P p1; F sections 7, 9–12, 16–17 and Table 6; FP slides 4–13.

- **Personal role:** R/C credit mechanical design, height adjustment, two-axis gimbal, FEA, and IMU/motor integration. F section 16 explicitly credits Justin with requirements/specifications, morphological chart, ideation, concept selection, analyses, final design, and gimbal CAD/drawings. It credits Matthew Ackerman with height-change CAD/drawings/analysis/BOM and Jeffrey Bulen with testing/integration. The charter lists Justin as finance manager. Sole ownership of the whole rig is not established.
- **Disciplines:** mechanical design, structures, mechatronics, embedded control, vibration isolation, power, robot payload integration, imaging.
- **Tools:** SolidWorks/Simulation; final report describes ESP32 Wi-Fi control and BGC 3.12 gimbal controller; IMU, brushless gimbal motors, stepper driver, and smartphone app. GUIDE references BaseCam tuning software. COLMAP/OpenSplat setup notes support the reconstruction workflow, but do not establish Justin's individual software authorship. STM32 in R conflicts with supporting documents.
- **Design decisions:** lead screw and constrained gantry selected over telescoping/cascade alternatives for rigidity and holding position; adjustable camera balance slot; two-axis stabilization; rubber isolation mounts; heavy components near the base; removable straps and silicone interface; separate power supplies; standard 1/4-inch camera interface.
- **Prototyping/manufacturing:** taped-tripod mockup, revised printed interface, then laser-cut MDF saddle, PLA gimbal/support components, aluminum extrusion, and purchased hardware. Drawings, STL/CAD revisions, fabrication package, receipts, and BOM support the build history.
- **Systems integration:** robot mounting/clearance and payload configuration; mechanical mast with motor/driver; ESP32 step/direction and PWM commands; IMU feedback to gimbal controller; camera and battery/wiring arrangement. Final design section describes these interfaces; source code is absent.
- **Testing/validation:** static FEA with a stated 1 kg camera load; mount-load checks; physical height/weight/extension measurements; IMU observation; 3-inch drop; runtime trial; teleoperated MRDC hallway capture and Gaussian-splat reconstruction. Mockup 1 failed stairs, mockup 2 improved clearance; final-rig limitations remain.
- **Results:** Table 6 reports 6.5 kg with batteries, camera height 4 ft 3 in–8 ft 1 in from the base of the dog, approximately 60 s extension normally/40 s at maximum speed, and 1.75 h gimbal runtime. Angular deviation was under 1 degree for **most** operation. A usable reconstruction was reported, with visible camera-occlusion artifacts. The <30 s speed target was missed; IP54, temperature, and 100,000-cycle fatigue targets were untested. Final report recommends further damping and a more capable robot; final rig could use ADA ramps but could not climb stairs.
- **Strongest images:** FP slide 4, completed rig on robot; slide 6, gimbal assembly drawing; slide 7, electronics diagram; slide 8, reconstruction. F Figure 26, mounted operating rig; Figures 11–12, labeled subsystem renders; Figures 14–19, FEA; Figures 20–24, prototype progression; Figure 29, electronics diagram; Figure 31, reconstruction. FAB p13, gimbal exploded assembly. Higher-quality embedded images are indexed below.
- **Missing:** precise individual ownership and assembly/testing contribution; confirmed final controller/motor/driver configuration; raw angular data, test conditions/sample counts, and fatigue/vibration evidence; original photos and verified video; camera-height datum; corrected FEA captions and print assumptions; whether mass includes the camera.

## 2 Autonomous land survey aircraft development

**What:** independent large fixed-wing UAV design/build/flight-test family, January 2024–present per R. P p4 covers aircraft 1, p2 covers aircraft 2 and 3; the fourth design in R is not described in the archive. Sources: R, A, C, P pp2/4.

- **Personal role:** R states solo design/fabrication of airframe, suspension landing gear, and electronics mounts; avionics/powertrain integration and flight tuning.
- **Disciplines/tools:** mechanical/aerodynamic design, structures, flight controls, avionics and power; Onshape, Pixhawk, PX4, QGroundControl.
- **Design decisions:** aircraft 1 used foamboard and rubber-band suspension gear; aircraft 2 replaced the V-tail with a conventional tail, enlarged wing area, and used a servo-steered tailwheel for control authority/propeller clearance; aircraft 3 used a flying-wing configuration and carbon reinforcement to address inefficient cruise.
- **Prototyping/manufacturing:** custom low-budget foamboard construction, fabricated mounting/landing gear, and carbon reinforcement. R reports four airframes; only three have identifiable images/descriptions.
- **Systems integration:** flight controller, avionics, powertrain, mechanical mounts, autopilot configuration and tuning; historical portfolio reports survey waypoint missions and automatic landing/takeoff capabilities for particular revisions.
- **Testing/validation:** R reports extensive field testing. P contains aircraft photography, flight-path screenshot and plot; underlying logs and test protocols are absent.
- **Results:** R supports iteration and field testing without numerical endurance. A reports 45-minute capability and cruise above 40 mph. P reports improved control/stall behavior in aircraft 2, and approximately 8 m/s stall/30% cruise throttle for aircraft 3. These remain source claims with no supplied logs or controlled comparisons.
- **Strongest images:** P p2 upper, flying wing in workshop and field; p2 lower, aircraft 2 and tailwheel CAD/build photo; p4 lower, aircraft 1 outdoors, gear render, mission screenshot/plot. These are embedded, relatively low-resolution assets.
- **Missing:** current/fourth aircraft, dates and dimensions per version, weight/payload/battery/motor/airfoil, original photos, CAD, flight logs and test conditions, mission outcomes or actual mapping outputs. Resolve p2's 7.5 ft wing span versus R's 65–85 inch range before using dimensions.

## 3 Heven multirotor systems integration and documentation

**What:** June–July 2026 professional internship work on an existing Group 2 multirotor. Sources: R, C, J. Platform-specific names are recorded in J; their public use is not established by this local archive.

- **Personal role:** reverse-engineering, debugging, integration documentation, flight software/network setup, and thrust testing per R/C. All 46 supplied tickets are assigned to Justin; assignment alone does not prove task completion.
- **Disciplines/tools:** UAV systems, avionics, telemetry/networking, hardware troubleshooting, test/documentation; QGroundControl, Mission Planner/ArduPilot-related configuration, Pixhawk/Cube ecosystem, radio/receiver links, companion computer, video interfaces, Jira/Confluence. J gives more detail than the resume, but linked documents are unavailable locally.
- **Design decisions:** a conventional direct RC plus telemetry path was specified for minimum viable flight while another communications path was unavailable; documentation distinguishes autopilot/GCS roles and test-versus-deployment configurations.
- **Prototyping/manufacturing:** receiver/telemetry installation and motor/ESC checks documented in tasks; new frame subassemblies were still In Progress (WE-242). This does not establish that Justin designed the original aircraft.
- **Systems integration:** flight control, companion computer, radios, Ethernet/UDP telemetry and video, and gimbal control. Completed WE-167/179 concern gimbal control and the companion-board connection guide; WE-154/155/156 concern receiver, telemetry, and flight modes.
- **Testing/validation:** resume/letter establish system integration and thrust testing. Jira supports configuration/check tasks and a completed flight-log-template task (WE-227). No thrust curves, test reports, or flight logs are supplied.
- **Results:** integration/configuration guides and operational documentation are supported by completed tickets. Minimum viable manual-flight parent WE-141 is Blocked despite a resolved date; do not claim its entire flight acceptance sequence passed from the export.
- **Strongest images:** none supplied for this workstream. Jira is evidence, not an attractive or necessarily publishable visual. Request a suitable aircraft photograph or simplified authorized system diagram.
- **Missing:** public-use boundaries and materials, actual technical guides, test data, approved images, final configuration, concrete before/after debugging outcomes, and status reconciliation. GPS-denied navigation research is In Progress, not demonstrated navigation capability.

## 4 Heven drone performance modeling tool

**What:** Python tool estimating multirotor endurance/range from vehicle, payload, mission, and environmental inputs. Sources: R/C; J WE-61, WE-115, WE-119, WE-121, WE-145/146/148.

- **Personal role:** developed the tool per R/C and completed model-related Jira tasks.
- **Disciplines/tools:** aircraft performance, power/energy modeling, environmental modeling, engineering software; Python, Tkinter, published motor thrust data, QGroundControl mission-analysis context.
- **Design decisions:** J describes a physics backend separated from a Tkinter frontend; hover calculations depend on vehicle/payload/environment, with an air-density model and manufacturer thrust data. R extends the described inputs to airspeed, altitude, battery capacity and range.
- **Prototyping/manufacturing:** software prototype; no physical manufacturing directly established for this tool.
- **Systems integration:** vehicle configuration and thrust/environment inputs feed mission/performance estimates. No direct live-aircraft data connection is established.
- **Testing/validation:** completed modeling tasks demonstrate reported development; no code, equations, unit tests, numerical example, or measured comparison is provided.
- **Results:** estimator developed; prediction accuracy, flight-test agreement, and engineering decisions it enabled are missing. Mission-analysis writeup WE-148 remains In Progress.
- **Strongest images:** none locally. A permitted interface screenshot and measured-versus-predicted plot would improve this page.
- **Missing:** source or sanitized excerpts, governing equations, assumptions/coaxial-loss treatment, input range, outputs, validation data/error, screenshots, and permitted publication scope. Keep within the internship case study initially.

## 5 FDM printed autonomous quadcopter

**What:** personal modular low-cost multirotor intended for autonomous GPS missions and repairability. Sources: P p1 lower; [3D Printed Drone Frame archive](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/3D Printed Drone Frame>).

- **Personal role:** P credits frame design, electronics integration and flight tuning; personal-project designation supports individual work, but specific CAD authorship should still be distinguished from downloaded motor/propeller models.
- **Disciplines/tools:** structures, additive manufacturing, avionics, flight control; Onshape per P, SolidWorks/native Simulation files in archive, PX4, PID tuning. No explanation of the CAD tool transition is supplied.
- **Design decisions:** modular printed chassis/interfaces, packaged flight controller/GPS/power distribution, and tuning for reported structural resonance. Images visibly show tube arms, so “fully 3D-printed airframe” needs qualification.
- **Prototyping/manufacturing:** printed plates/clamps/mounts and tube-based structure are represented by photographs and CAD. Exact polymers, print settings, tube material and manufacturing dates are unconfirmed.
- **Systems integration:** flight controller, GPS, power distribution and PX4 configuration within the custom frame.
- **Testing/validation:** P reports flight trials; native static-study artifacts exist, but constraints/results were not recomputed. Solver output identifies an August 2025 run, which does not establish full project dates.
- **Results:** P reports stable autonomous flight, waypoint navigation, automatic takeoff/Return-to-Land, and one-hour frame assembly. No logs or timed assembly record validate these claims.
- **Strongest images:** P p1 lower right, assembled aircraft outdoors; lower middle, printed plates/clamps during assembly; lower left, full-frame render. Standalone archive images mainly depict motor/propeller reference components, not Justin's finished airframe.
- **Missing:** dates, polymer/print process, dimensions/mass, motor/battery/payload, structural test results, flight logs/tuning evidence, original photographs, and distinction from the unidentified multirotor archive.

## 6 Experimental Flights VIP tiltrotor VTOL

**What:** Georgia Tech custom tri-rotor tiltrotor fixed-wing subteam effort, August–December 2024. Source: R only.

- **Personal role:** airframe/avionics engineer and technical lead of the VTOL subteam, guiding conceptualization/structural design and Pixhawk integration.
- **Disciplines/tools:** mechanical/airframe design, aerostructures, avionics and systems integration; Pixhawk explicitly named. Project-specific CAD tool, firmware and control algorithms are not supplied.
- **Design decisions:** tri-rotor tiltrotor architecture is documented; tilt mechanism, actuator choice and trade studies are missing.
- **Prototyping/manufacturing:** unspecified; do not infer fabrication or a finished aircraft from the resume.
- **Systems integration:** bridging airframe design, onboard flight control, and sensor payloads.
- **Testing/validation/results:** leadership/design/integration experience is documented; hover, transition or flight-test success is not stated.
- **Strongest images:** none supplied.
- **Missing:** team context and individual deliverables, CAD, manufacturing record, tilt mechanism, components, integration diagrams, completion status, test outcomes and photographs. Suitable for an experience entry until evidence improves.

## 7 Boreas competition UAV

**What:** AmadorUAVs aircraft for the 2022 AUVSI SUAS competition, long-distance flight and UGV deployment. Source: P p3 upper; exact individual participation dates are absent.

- **Personal role:** P credits custom frame CAD and fabrication; no formal role title or team responsibility split is supplied.
- **Disciplines/tools:** airframe structures, composite machining, additive manufacturing, payload integration; Onshape. A stress plot is pictured, but analysis software and assumptions are unspecified.
- **Design decisions:** custom frame plates/assemblies, carbon-fiber structural plates, printed landing gear/brackets; long-range and payload requirements drove the concept.
- **Prototyping/manufacturing:** CNC-machined carbon-fiber plates and printed mounting/landing components per P.
- **Systems integration:** completed UAV carried/deployed a UGV according to P; Justin's responsibility for electronics, autonomy or release control is not established.
- **Testing/validation:** flight photograph and historical narrative; no logs or competition report.
- **Results:** P reports flights over five miles, UGV deployment and second overall in SUAS 2022. Treat competition placing as a team result, with supporting record missing.
- **Strongest images:** P p3 upper right, aircraft in flight (embedded image 767 × 578); upper left, frame render and stress plot.
- **Missing:** original images, individual role, build/test dates, payload/mass/endurance, competition evidence, manufacturing files, flight and release-test data.

## 8 RoboGrinder armor plate mounting

**What:** mounts for four armor plates on an aluminum mecanum-wheel robot chassis. Source: P p3 lower; A lists broader VT RoboGrinder membership September 2022–July 2023.

- **Personal role:** design, machining and assembly of mounting plates per P; broader team manufacturing described in A.
- **Disciplines/tools:** mechanical interfaces, lightweight structures, CNC fabrication; SolidWorks, CNC routing/milling and standard fasteners.
- **Design decisions:** fiberglass plates with strategically placed lightening holes and standard metric hardware.
- **Prototyping/manufacturing:** CAD/drawing-to-CNC workflow and assembled fiberglass brackets; photos show machining and loose parts.
- **Systems integration:** armor-to-chassis mounting; no personal electrical/software work established.
- **Testing/validation:** P reports force applied to armor plates; test fixture, direction and procedure missing.
- **Results:** P claims resistance to over 50 lb of applied force. A reports the team's fourth-place RoboMaster North America University League result in 2023; it is not a result of this mounting subsystem alone.
- **Strongest images:** P p3 lower middle, machining; lower right, completed plates; lower left, assembled robot CAD.
- **Missing:** exact subsystem dates, loading conditions and failure margin, material/thickness, mass saved, CAD/drawings and original photos; confirmation of personal/team scope.

## 9 RoboGrinder large quadcopter restoration

**What:** restore a mostly disassembled quadcopter using newer hardware, motor mounts and landing-gear mounts. Source: P p4 upper. A's broader team dates do not conclusively date this particular project.

- **Personal role:** mounting design/install, flight-controller setup and flight operation reported in P; team ownership split unknown.
- **Disciplines/tools:** mechanical retrofit, avionics, UAV controls; SolidWorks, PX4 and QGroundControl.
- **Design decisions:** replace mount interfaces and modernize flight hardware; component-selection rationale is absent.
- **Prototyping/manufacturing:** new mounting brackets and plates; fabrication process/materials unspecified for this project.
- **Systems integration:** flight controller/firmware, telemetry and ground station with restored airframe.
- **Testing/validation:** P describes telemetry-controlled flights and basic GPS waypoint missions; no logs supplied.
- **Results:** aircraft returned to reported flight and waypoint operation. No endurance/payload/reliability figures.
- **Strongest images:** P p4 upper, wiring close-up, ground-station setup and assembled aircraft.
- **Missing:** dates, individual contributions, before/after configuration, CAD, mount manufacturing details, flight/test data and original photographs.

## 10 Mind inator ME 2110 competition robot

**What:** Fall 2024 robot executing competition tasks in a 40-second window under a stated $120 budget. Source: P p5. Separate from the later ME 2110 grader employment.

- **Personal role:** P credits CAD, fabrication, Arduino programming and actuator integration; team photograph makes exact individual ownership worth clarifying.
- **Disciplines/tools:** mechanisms, pneumatic/electromechanical actuation, embedded sequencing, fabrication; SolidWorks, Arduino IDE, laser cutting and 3D printing.
- **Design decisions:** telescoping retrieval/lift mechanisms, scissor lift, winch, drawer-slide/pneumatic motion, DC motors and solenoid release; design reliability and cost constraints.
- **Prototyping/manufacturing:** laser-cut scissor parts, printed mounts/mechanisms and assembled frame. Material specifications are incomplete.
- **Systems integration:** Arduino control of pneumatic pistons, DC motors and solenoids across multiple timed actions.
- **Testing/validation:** repeated trials are reported; no trial log or sample count. Hundreds of cycles appears as a goal, not documented test count.
- **Results:** P reports 18th of 66 in **design review**, 95% successful mechanism deployment in trials, and total cost below $70. Overall competition placing is not provided.
- **Strongest images:** P p5 top left, annotated system CAD; top right, completed robot; lower, retracted/extended lifts and annotated retrieval mechanism. Embedded lift renders are approximately 677–678 × 267–270.
- **Missing:** personal/team contribution split, original CAD/code, test counts and failures, timing chart, dimensions/loads, budget breakdown and competition record.

## 11 Vacuum parcel end effector concept

**What:** internship take-home design study for handling varied parcels, up to 50 lb, approximately 6-inch height variation and a proposed one-second pick/place target. No completed prototype is documented. Sources: E; [Design 1 Assembly drawing](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/Intern Take Home Project/CAD/Design 1/Design 1 Assembly.pdf>).

- **Personal role:** presentation names Justin as designer; employer/application date is not confirmed. “Minimum Cargo Robotics Package” in a slide does not establish employment there.
- **Disciplines/tools:** mechanical end-effector design, vacuum handling, sensing, manufacturability and concept selection; SolidWorks CAD, supplier data and PowerPoint.
- **Design decisions:** six compliant vacuum cups, possible automatic vacuum shut-off for unused cups, load sensing, camera/light packaging, proposed 5 mm carbon-fiber plates; considers rotation drives and a hybrid mechanical/vacuum alternative. Rotation was not implemented.
- **Prototyping/manufacturing:** CAD/drawing and proposed CNC-routed plates/OTS parts; no evidence of machining or assembly.
- **Systems integration:** proposed vacuum cups/valves, load cell, pressure transducer and Raspberry Pi camera. No functioning sensing/control loop established.
- **Testing/validation:** supplier-rating arithmetic and design review only; no physical pick tests, vacuum-leak tests or cycle-time measurement.
- **Results:** concept presentation and drawing delivered. Claimed 79.8 lb total cup capacity is an ideal sum, not verified lifting capacity or a safety-factor calculation. $527.43 preliminary BOM excludes pump/fittings/valves and other vacuum hardware.
- **Strongest images:** E slides 8–9, assembly/side views; slide 5, underside/layout; drawing page 1. Use original concept CAD renders rather than third-party gripper reference images.
- **Missing:** date/client context, physical prototype status, package trials, seal/contact-area and acceleration loads, factor of safety, vacuum supply/flow sizing, chosen sensors, rotation design, actual cycle time and complete costs. Sensor/model and drawing-unit conflicts are listed below.

## 12 Unidentified carbon tube multirotor CAD study

**What:** archive named [dumbass jamal drone project](<C:/Users/justi/Documents/Projects/Engineering-Portfolio/source-materials/project-documents/dumbass jamal drone project>), containing center plates/clamps, carbon tube, motor/leg assemblies, STEP/Parasolid exports and simulation studies. Use a neutral public label only after identity is confirmed; preserve the source folder name.

- **Personal role:** unknown. Location in Justin's archive alone does not establish authorship or whether this was personal/team/commissioned work.
- **Disciplines/tools:** mechanical frame design and structural analysis suggested by CAD/solver artifacts; SolidWorks Simulation 2025 appears in readable output.
- **Design decisions:** names suggest clamped carbon-tube arms, plates and modular motor/landing interfaces. Geometry, materials and design reasoning have not been verified in native CAD.
- **Prototyping/manufacturing:** CAD models/neutral exports exist; physical manufacture is unconfirmed.
- **Systems integration:** mechanical subassemblies represented; avionics/power integration unconfirmed.
- **Testing/validation:** static and frequency-study artifacts exist, with readable output dated December 18/20, 2025. These are solver-run dates, not formal project dates. No supported stress limit, mode frequency, safety factor or physical test result extracted.
- **Results:** design-study files available; flightworthiness and prototype success unknown.
- **Strongest images:** no finished-project photographs or clearly attributable overview renders supplied. Future native-CAD renders could help once ownership/identity is confirmed.
- **Missing:** actual project name/purpose, relationship to other quadcopters, author/team/date, design requirements, loads/constraints, complete assembly, manufacturing record, images and test outcomes. Do not silently merge it with Boreas, RoboGrinder or the printed drone.

## 13 GT Supersonics UAV avionics integration

**What:** Georgia Tech club UAV avionics and powertrain work, August 2024–June 2025 in the historical resume. Source: O only; omitted from R. It is distinct from the Experimental Flights VIP tiltrotor entry unless Justin confirms otherwise.

**User preference:** Keep this work secondary in the portfolio. Highlight integration and testing of flight sensors and RC control systems in a brief experience entry. Do not make thrust-stand work a featured project or a leading accomplishment. The thrust-data details below are retained only as source evidence.

- **Personal role:** avionics team member; tested/integrated flight sensors and RC systems and processed load-sensor data for sustained powertrain thrust.
- **Disciplines/tools:** avionics, UAV systems integration, instrumentation and test-data analysis; MATLAB explicitly named. Flight-controller model, firmware and sensor types are unspecified.
- **Design decisions:** not described beyond sensor/control integration and thrust measurement.
- **Prototyping/manufacturing:** hardware integration is reported, but no airframe design or manufacturing contribution is established.
- **Systems integration:** flight sensors and RC control within the club aircraft; load sensing associated with powertrain testing.
- **Testing/validation:** load-sensor data processing to determine maximum sustained thrust; fixture, calibration and test conditions absent.
- **Results:** integration and thrust-data analysis reported; measured thrust, aircraft speed, flight success and competition results are not supplied.
- **Strongest images:** none supplied.
- **Missing:** confirm dates/status, project name and relationship to VIP, flight-sensor/RC configuration, integration responsibilities, validation outcomes and photographs. Retain as a supporting experience entry in accordance with the user's preference.

## Image selection and recoverability

Most older project photography is available only as compressed PDF-embedded assets, usually 200–600 pixels across. Native-resolution originals would materially improve future project pages. Extracting a whole PDF page does not restore photographic resolution.

The capstone has stronger Office-embedded originals. These locations are internal ZIP members of the source DOCX/PPTX, not separate files in `source-materials`:

| Candidate | Source location | Pixel size | Use |
| --- | --- | --- | --- |
| Completed rig on robot | FP `ppt/media/image11.png` | 978 × 1304 | Preferred hardware hero candidate |
| Team and prototype | FP `ppt/media/image14.png` | 1718 × 1289 | Team credit/context |
| Gimbal assembly drawing | FP `ppt/media/image7.png` | 1532 × 1107 | Mechanism/exploded detail |
| Labeled gimbal | F `word/media/image11.png` | 974 × 828 | Explain axes/isolation |
| Labeled mast base | F `word/media/image20.png` | 980 × 806 | Integration/actuation explanation |
| Roll-axis stress plot | F `word/media/image63.png` | 1250 × 674 | Analysis evidence with assumptions |
| Tripod/mockup hardware | F `word/media/image14.jpg` | 1536 × 2048 | Iteration story, label as mockup |
| End-effector CAD isometric | E `ppt/media/image9.png` | 769 × 890 | Concept-design hero |
| End-effector drawing image | E `ppt/media/image12.png` | 1130 × 697 | Geometry/layout discussion |

The completed-rig photograph appears in both portfolio and capstone files; use the larger original. Vendor camera, motor, propeller, commercial gripper, DJI/Unitree/gimbal photographs and prior-art illustrations are references, not evidence Justin designed those products. Receipts contain personal/order details and are internal evidence rather than website downloads. The guide contains a network password and app link; these are not public portfolio content.

## Conflicting outdated duplicated and unclear information

| Issue | Evidence | Treatment for future copy |
| --- | --- | --- |
| Degree dates/status | R separately states B.S. May 2026 and expected M.S. May 2027; A combines BS/MS under expected May 2027; personal info still calls Justin a B.S. student despite graduation; old site says Class of 2026 | Use R's completed B.S. and current M.S. status |
| Historical resume GPA/employment | O lists GPA 3.95 and grader January 2025–Present; R gives GPA 3.96 and grader end May 2026, followed by the current GTA role | Use R for current academic and employment facts |
| Historical titles and additional roles | O calls capstone role Project Lead and Mechanical Designer and adds GT Supersonics and Millbrae Karaoke House work omitted from R | Retain as historical context; clarify leadership scope and whether extra roles belong on the portfolio |
| Additional RoboGrinder experience | A supplies 2022–2023 dates and manufacturing/team result omitted from R | Supplement as secondary-source experience; do not assume omission means invalidity |
| Capstone ownership | R/C general design language; P says entire electrical layout; F credits height-change CAD/analysis to Matthew and testing/integration to Jeffrey | Distinguish Justin's gimbal/analysis/design contribution from team deliverables; clarify overlap |
| Controller architecture | R/A say STM32-based microcontroller; F/GUIDE say ESP32 plus BGC 3.12; GUIDE references an 8-bit BaseCam GUI | Preserve the conflict; confirm exact gimbal-board architecture before naming STM32 |
| Gimbal axes/camera thread | F1 uses three axes/3/8-inch; F2/final configuration uses two axes/1/4-inch; old three-axis/thread references survive in later text/images | Describe final two-axis/1/4-inch design and identify earlier ideas explicitly |
| Actuation configuration | F analysis/diagram uses 23HS22 motor and DM542T driver; final discussion says NEMA 17; BOM says 17HS10/TB6600; electronics deck includes an Arduino Nano alternative | Confirm the as-built motor/driver, power and controller combination |
| Height and compliance | R says 4–8 ft; final Table 6 reports 4 ft 3 in–8 ft 1 in from dog base while requirement is written >4 ft and <8 ft | Use measured range/datum; do not claim exact 4–8 ft or blanket compliance |
| Extension speed | Early calculations target 20/30 s; final normal speed is approximately 60 s, maximum 40 s | State target missed and explain torque/safety tradeoff; planned speed is not measured performance |
| FEA stress caption | F text/plot legend show roll-axis maximum 8.110 MPa; Figure 15 caption says 6.110 MPa | Correct caption before publishing; supplied plot supports 8.110 MPa, not 6.110 |
| FEA displacement captions | Figures 17–19 label displacement as stress in MPa; actual plots show URES in mm, maxima about 0.3826, 1.123 and 0.3567 mm | Do not copy erroneous captions; these are simulated displacement, not stress or physical deformation measurements |
| Analysis assumptions/FOS | Material choices and strength assumptions vary; report gives ABS/PLA/PETG factors and a broad >6 statement | Qualify results by modeled load/material; no independently validated printed-part fatigue/anisotropy margin |
| Image quality and performance claims | R/P describe distortion-free imagery; F reports residual vibration and red/pink camera-occlusion artifacts | Say usable reconstruction demonstrated; avoid zero-distortion or full vibration isolation claims |
| Stair traversal | F2's lighter tripod mockup climbed stairs; F final summary states final rig cannot, but can use ADA ramps | Separate mockup success from final-system limitation |
| Environmental and all-specifications claims | F narrative says all critical demands satisfied; Table 6 lists IP54 demand as NOT TESTED, plus untested temperature/fatigue | Use specific achieved/unverified results; no environmental certification |
| Capstone cost | BOM component cost is $439.13; reimbursement workbook total after tax is $667.528 | Distinguish allocated assembly BOM from project purchasing/receipt total, including spares/prototyping; do not equate either with complete commercial cost |
| Capstone fabrication | FP says every part is printed/OTS; F and BOM show laser-cut MDF | Describe actual printed/OTS/laser-cut build; printed saddle is an alternative |
| Autonomy | Capstone report uses autonomous-platform language, but field capture was teleoperated; future autonomous fleet is sponsor vision | Avoid claiming Justin developed autonomous quadruped navigation |
| Survey aircraft count/span | R says four designs, 65–85 in; O says over four; P describes only three and aircraft 2 at 7.5 ft/90 in | Keep four as current resume claim; ask for remaining designs and reconcile span per generation |
| Survey performance | A adds 45 min; P adds >40 mph, ~8 m/s stall, 30% throttle | Attribute to source/version until logs and conditions are supplied; throttle percentage alone is not measured efficiency |
| Printed-frame construction/tools | P calls it fully printed/Onshape; photos show tube arms and archive uses SolidWorks | Clarify structural materials and CAD progression; use a qualified title |
| Internship task status | Some parents are Blocked with resolved timestamps; 8 of 46 tickets are not Complete | Status remains unresolved; do not count resolved timestamp, assignment, or completed subtasks as all acceptance criteria achieved |
| Jira access/data | Ticket descriptions link to private Confluence pages; code/screenshots/test data absent | Local export establishes limited evidence only; keep internal links/account identifiers out of public copy |
| Effector load cell | E specifies LC103B-100 but links a -25 variant; CAD contains a 500 kg load-cell model | Confirm intended versus placeholder model and rating |
| Effector camera | E proposes Camera Module 3; supplied camera assets include older board labeling/OV5647 names | Treat camera CAD as reference placeholder until model is confirmed |
| Effector units/capacity | Pressure slide pairs 85 psi with 51.71 mmHg; assembly drawing says inches while dimensions appear on a metric scale; cup capacities simply summed | Flag unit/model assumptions; no verified package capacity or cycle-time claim |
| Old competition claims | P reports SUAS second, mount >50 lb, robot 95% trials, design-review 18/66; logs/results records absent | Attribute historic claims and team awards; obtain evidence and test counts before highlighting numbers |
| Armor load wording | P says over 50 lb, O says up to approximately 50 lb | Confirm actual load and test method; avoid presenting either wording as a precise validated threshold |
| Duplicate/reference files | 472 extra identical files; F1 and final-folder Copy of Report 1 are byte-identical; multiple assembly drawings repeat across revisions | Link one preferred source per subject; retain all originals |
| Template/proposal content | First-Progress-Report.docx is course guidance, not a completed project report; vendor parts, drafts and prior-art figures recur | Exclude templates/vendor references as personal accomplishments; final report/fabrication package is preferred |
| Old website structure | Home/About retain older student bio; Portfolio embeds Justin Portfolio 2.pdf; Resume embeds Justin Park - Drone Resume.pdf; footer/social links include template placeholders | Reuse evidence selectively; embedded live PDFs were not byte-compared to local files; do not copy template links or old layout |
| File references/privacy | personal-info cover-letter path omits .pdf; no GitHub; receipts/charter/guide/Jira contain internal details | Fix references in future content data, omit unavailable GitHub, and publish only selected portfolio content |
| Unidentified archive | Folder wording, carbon-tube assemblies and December solver dates do not establish identity or ownership | Keep separate pending clarification; use no invented title, results or authorship |

## Smaller interests and missing archive coverage

Old About page mentions PC building/upgrading, bicycle and suspension maintenance, music/guitar electronics and a pedalboard, photography, and multiple FPV miniquads including graduation filming. These are useful optional biography details, but there are insufficient build records to create additional substantial engineering case studies. O also describes Millbrae Karaoke House assistant-manager work, August 2023–December 2025: facility hardware upgrades/commercial audio installation and Excel inventory/budget/customer-volume tracking. This is supporting hands-on employment context; engineering requirements, individual design decisions, tools beyond Excel, validation, images and quantified outcomes are missing. No standalone reports, CAD, code, or original photo sets are supplied for VIP, GT Supersonics, Boreas, Mind-inator, the survey aircraft or the older RoboGrinder projects beyond resume/PDF evidence. Teaching is documented experience, not an additional personally authored engineering project.

## Review limits

All 945 source files were inventoried and hashed, including the historical resume added during review. The original 944 files were confirmed unchanged. Readable document text, tables, slides and relevant embedded/standalone images were reviewed, including historical portfolio pages and unique fabrication drawings. CAD revisions, downloaded components, neutral exports, ZIP member lists and simulation artifacts were catalogued; native assemblies, meshes and FEA were not revalidated in their authoring tools. Video playback, private linked documents, app code and external reconstruction assets remain unverified. These limits constrain claims rather than being filled with assumptions. Scratch extraction/render files were kept outside the project; only these notes were added.
