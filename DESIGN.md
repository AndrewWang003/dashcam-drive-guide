# DESIGN.md — design rules for the Dash Cam Drive Guide

**Read this whole file before you change `index.html`.** It is written for AI assistants and human editors. It records every design decision that shapes how the page looks, moves, reads and behaves, and why. Most rules exist because the owner tested an alternative and rejected it; those are marked **(rejected)**. Do not bring a rejected idea back without asking the owner.

If a rule here conflicts with a new instruction from the owner, the owner wins. Then update this file in the same commit.

---

## 1. What this page is

- A training guide for **temporary drivers** on dash cam road survey jobs. They read it once on their own phone, usually during the induction, then answer a quiz and send a screenshot of the final card to their supervisor.
- It holds **general rules only**. It must stay reusable for any future job.
- One file: `index.html`. No build step, no libraries, no backend. Fonts load from Google Fonts; nothing else is loaded and nothing is sent or stored.

### Design goals, in priority order

1. **The driver remembers the four key points** (section 9). Everything else supports them.
2. **Form and colour serve information.** Nothing is decoration. If a shape, colour or movement does not help the driver understand the rule, remove it.
3. **One unified illustration style** on every card and quiz picture.
4. **Brand feel: tasteful and caring.** The page should feel made with care by a serious company, so a temporary worker feels trusted and responsible. Calm, warm, exact. Never childish, never corporate-cold, never alarming.

---

## 2. Audience and wording

- Readers may not be native English speakers. Use **short, plain English**. No idioms, no Australian slang, no jargon.
- One idea per sentence. Prefer verbs: "Check REC before you start."
- Say **"your supervisor"**. Never a person's name.
- **Never add job-specific details**: no dates, clock times, route names, place names, phone numbers, company staff names.
- Do not restate ordinary road rules (for example "no phone while driving" as a law). The guide covers survey rules. Australian road rules are assumed; the car is **right-hand drive** and traffic keeps **left**.
- Be honest about what the page does. The completion card says the page does not send anything by itself. Keep that.
- Each card: a title, one lead sentence, and **at most 3 bullets**. Each bullet starts with a bold keyword phrase, then a short explanation.
- Check every new sentence for double meanings. Known traps: "the whole time" (say "the whole session"); "each part" (say what part).

---

## 3. Page structure

Top bar (always visible):

- **Back** button, top-left. Goes back exactly one page, also inside the quiz.
- Title and position text ("Card 3 of 15", "Question 2 of 10").
- **Theme button**, top-right (section 8).
- **Route progress bar** with five stops: `BEFORE · ROAD · BREAK · AFTER · QUIZ`. The amber fill moves forward card by card, so it is both the stage map and the progress indicator.

Flow:

1. Start page: title, "About 7 minutes", the four key points, Start button.
2. 15 cards, grouped in four stages (`STAGES` in the script): Before you drive, On the road, Between sessions, After the last session. Each card shows a stage chip.
3. The last card repeats the four key points.
4. Quiz: 10 questions.
5. Name entry, then the completion card for the screenshot.

Rules:

- One card on screen at a time. One narrow column. Must work at 320 px width with no sideways scrolling.
- Order cards in the order the driver does things during the day.
- **No second progress indicator.** A vertical trail down the left side was tried and removed **(rejected)**.
- Keep the total reading time under about 10 minutes. If you add cards, update the "About N minutes" label.

---

## 4. Illustration style

Name: **flat geometric transit poster**. Think of a modern public transport safety poster.

- Flat filled shapes. **No outlines** around objects.
- **No texture, grain, noise, or gradient lighting.** Texture looked dirty; soft light was not visible on a phone **(both rejected)**.
- Rounded corners on everything man-made.
- Each object uses **one main colour plus one darker shade** of it. No third tone.
- A soft dark ellipse under objects that stand on the ground (cars, cones) to seat them.
- Simple background: sky block, one or two hill shapes, ground. Never detailed scenery.
- **No people and no faces.** Hands and bodies are not drawn; actions are shown by the object moving.
- All pictures are inline SVG produced by helper functions in the script (`R`, `C`, `T`, `svg`, `arc`, `carSym`, `cabin`, `cams`, `wiring`, `outside`, `check`, `no`, …). **Reuse these helpers.** Do not add image files, icon fonts or libraries.
- Card pictures use `viewBox="0 0 360 220"`; quiz pictures are shorter (170, or 196 for cabin views).

### 4.1 Palette (fixed)

Illustration constants (in the script):

| Name | Hex | Use |
|---|---|---|
| `N` navy | `#141B3C` | Brand colour. Car bodies, cameras, cabin frame, structure |
| `N2` / `N3` / `NK` | `#33407A` / `#232B52` / `#0A0E22` | Navy shades, shadows |
| `CR` cream / `W` white | `#F3EBDD` / `#FFFDF8` | Light surfaces, text on navy |
| `AM` amber / `AM2` | `#F2A93B` / `#DB932A` | **Action and progress** |
| `CO` coral / `CO2` | `#E4572E` / `#C4441F` | **Attention and prohibition** |
| `SG` sage | `#5E8F88` | **Correct, done, OK** |
| `SK` / `SK2` / `MT` | `#DCE9E8` / `#C9DBD8` / `#B9CFCB` | Sky, far hills |
| `SD` / `SD2` / `SD3` | `#D8C9AE` / `#C4B393` / `#BCA988` | Sand: ground, dashboard |
| `GY` | `#B8BCC8` | Neutral grey: other cars, metal |

Page tokens (CSS variables on `:root`):

| Token | Light | Dark |
|---|---|---|
| `--bg` | `#F6F1E7` | `#0E1228` |
| `--surface` | `#FFFDF8` | `#171D3A` |
| `--ink` | `#141B3C` | `#F3EBDD` |
| `--muted` | `#5B6078` | `#A9AEC6` |
| `--line` | `#E2D9C8` | `#2B3359` |
| `--brand` / `--brand-ink` | `#141B3C` / `#FFFDF8` | `#F2A93B` / `#141B3C` |
| `--amber` | `#F2A93B` | `#F2A93B` |
| `--coral` | `#D94A22` | `#FF7A52` |
| `--sage` | `#5E8F88` | `#7DB3AB` |

Do not add colours. If something needs to stand out, use the meaning table below.

### 4.2 Colour meaning (never break this)

| Colour | Means | Examples |
|---|---|---|
| **Coral** | Stop, don't, look here | REC dot, prohibition signs, wrong answer, gauge needles |
| **Amber** | Do this, movement, progress | Lane lines, plugs and adapter, progress fill, camera view box, primary button in dark mode |
| **Sage** | Correct, done | Check badges, OK, right answer |
| **Navy** | Brand, structure, neutral objects | Survey car, cameras, cabin |

- The survey car is always navy. Other traffic is grey.
- A prohibition is always the **coral circle with a diagonal bar** (`no()` helper). A lock icon was tried and was not understood **(rejected)**.
- Never use colour alone for right/wrong in the quiz; keep the text feedback too.

### 4.3 Text inside pictures

Keep it to short labels only: `REC`, `12V`, `A`, `B`, `000`, `OK`, `TIME'S UP`, odometer digits, numbers. All explanation goes in the HTML text below the picture. Text must never overflow its shape.

---

## 5. Viewpoint and proportion

### 5.1 Which view to use

| View | Use for | Cards |
|---|---|---|
| **First-person, from the driver's seat** | Things the driver does with their hands inside the car | Camera setup, Power on, Hands off while driving, Between sessions, quiz Q1/Q2 |
| **Side view** | Route and position ideas | The job, On the road, Finish where you started, Stay on your route |
| **Top-down** | Lanes | Lanes and overtaking |
| **Object close-up** | A single item | Before you start, Odometer photos, If something goes wrong, SD card, Hand back |

First-person view was chosen for immersion: the driver sees what they will really see.

### 5.2 Cabin (`cabin()` helper)

- Right-hand drive: **steering wheel at the bottom-right**.
- Dashboard contains: glovebox (left), air vents, centre screen, instrument hood with **two gauges, each with a static coral needle**, steering wheel with spokes and hub.
- Through the windscreen: a **wide** road with edge lines and a dashed centre line, going to a vanishing point.

### 5.3 True proportions

- The **rear-view mirror (96×30) is bigger than a dash cam (40×28)**. Never draw a camera larger than the mirror.
- **Two cameras, one each side of the mirror, at the top of the windscreen, pointing straight ahead.** This follows the company method: middle of the windscreen, as high as possible, near the rear-view mirror.
- The adapter is small (48×17).
- When a camera screen is too small to read, use a **zoom bubble** (`zoomRec`) instead of enlarging the camera.
- In the side view the two cameras sit side by side at the top of the windscreen, not stepped diagonally.

### 5.4 Camera view (Camera setup card)

Each camera has **its own view region** (two cameras, two regions that overlap in the middle). A region is a translucent amber rectangle on the road ahead with four thin edge lines running back to its camera.

- Lines are thin (1.4–1.6) so the picture stays light on a small screen.
- **Any part of a line that passes over a filled view region is drawn as a clear dashed line** (darker amber `AM2`, width 2.2, dash `6 4`). Parts outside the regions are solid.
- The two regions share one solid outer border; the inner side edges, which sit inside the other camera's region, are dashed.

Earlier versions were rejected: downward triangles (looked like cameras pointing down), a flat viewfinder frame, two solid trapezoids, and **one merged region for both cameras** (it hides that each camera records its own view).

---

## 6. Hardware facts (pictures must match the real equipment)

- Each car has **two dash cams**. One is the backup. **Both must record.**
- Each camera has **its own cable ending in a cigarette-lighter plug**.
- Both camera plugs go into a **1-to-2 adapter** (two sockets).
- The adapter has **its own short lead and plug**, which goes into the car's **12V socket**.
- To **stop** recording between sessions: pull **only the adapter's plug out of the car**. The cameras stay plugged into the adapter.
- To **start** again: push the adapter's plug back in and check `REC` on both cameras.
- A plugged-in plug must look inserted: the barrel disappears inside the socket hole (clip path), it does not sit on top.
- Cables are navy with a thin white edge so they stay visible against the road.
- **SD card: the driver never removes it.** The camera is drawn from the screen side.
- **Handed back at the end:** two cameras (cables attached) and one adapter. Nothing else.

---

## 7. Motion

- Every card has a small animation that **explains the rule**. No movement just for decoration.
- **Animations always play.** The owner asked for this on purpose after animations did not play on an iPhone. Do not add a `prefers-reduced-motion` rule that stops them.
- Loops are slow and calm. Nothing flashes faster than once per second.
- A car driving to the right: **road dashes move right-to-left**. The car bobs by only 1.3 px.
- **A stopped car's wheels do not turn.** Use the non-spinning symbols `carS` / `carBS`. (CSS cannot stop an animation inside a `<use>` symbol, so separate symbols exist.)
- **SD card animation:** the card slides **out** a little, a coral arrow shows the direction, the prohibition sign pops, the card fades and resets. Never animate the card moving **in** — it reads as "insert the card".
- No rotating gear. The gear icon is static.
- No curved detour line jumping over a road barrier **(rejected)**.
- Use `transform-box` / `transform-origin` carefully for SVG parts. The adapter lead scales from a fixed end so it never shows from under the adapter.

---

## 8. Light and dark theme

- Default follows the device (`prefers-color-scheme`).
- One round button, top-right, toggles `document.documentElement.dataset.theme`.
- **The icon shows the mode you will switch to**: a moon in daylight mode, a sun in dark mode. This is the owner's choice.
- All page colours come from the tokens in 4.1. Dark tokens are defined twice: under `@media (prefers-color-scheme: dark){:root:not([data-theme="light"])}` and under `:root[data-theme="dark"]`. Change both together.
- Pictures keep the same palette in both themes; in dark mode the picture frame gets a thin border (`--scene-edge`).

---

## 9. Content rules

### 9.1 The four key points

They appear on the start page and on the last card, with the same words and the same icons, in this order:

1. **Stay safe.** Safety comes before the data.
2. **Start on time. Drive the whole session.**
3. **Keep both cameras recording.**
4. **Stay on your route.** Road closed? Report it and get OK first. Then go around only the closed part.

Do not reorder them, reword them, or add a fifth without the owner's decision.

### 9.2 Rules already agreed

- Each driver has their **own** start and end time and must know it.
- Finish where you started (A→B→A or B→A→B; the card has an A/B chooser).
- If something goes wrong: **stop safely first, then contact** your supervisor. Call **000** if anyone is hurt.
- A closed road needs a report **and** approval before going around.
- Lanes: use the left lane or the second lane. Use the far right lane only to turn right. Overtake slow vehicles. Do not jump the queue at red lights.
- Clean the windscreen before starting.
- Odometer photo at the start and end.

### 9.3 Open item — do not add yet

- **"15-minute break after every 2 hours of driving"** is in the company method document, but the owner has **not confirmed** it for this guide. Leave it out until the owner says so.

---

## 10. Interaction

- Touch targets at least 44 px. Buttons have visible focus and pressed states.
- **Quiz:** tap an answer to select it, then tap **Check answer**. This two-step design prevents accidental taps. Feedback shows right/wrong with a one-line reason. Wrong questions **come back at the end** until all are right. **Reset** sits top-right of the quiz and turns coral after a wrong answer. **Back** goes to the previous question, it does not restart the quiz.
- **Quiz pictures set the scene and never show the answer.**
- **Power on** card: two taps (cameras → adapter, then adapter → car). Unplug returns to step 1.
- **Between sessions** card: one button toggles recording / stopped.
- **Finish where you started** card: A / B chooser.
- Completion card: the driver's name with date and time, inside an amber border — made for a screenshot.

---

## 11. Typography and layout

- Display: **Overpass** 600/800 (headings, buttons, labels; uppercase labels use letter-spacing).
- Body: **Atkinson Hyperlegible** 400/700, 17 px, line-height 1.5. Chosen for legibility for non-native readers.
- Numbers and codes: **Overpass Mono** 600.
- No other fonts. In SVG, text uses Overpass or Overpass Mono.
- Cards: `--surface` background, 1 px `--line` border, 18 px radius. No drop shadows.
- Side gutters at least 16 px, and respect `env(safe-area-inset-*)`.

---

## 12. Technical rules

- Keep everything in **one self-contained `index.html`**: `<style>`, markup, one `<script>` (an IIFE).
- Data lives in arrays in the script:
  - `CARDS` — `{g, t, s, lead, pts, plug?, choose?, keys?}`: `g` is the stage index, `t` the title, `s` the scene key in `S`, `pts` the bullets.
  - `QUIZ` — `{q, o, a, why}`: question, options, index of the right answer, one-line reason.
  - `QS` — one picture per quiz question, same order as `QUIZ`.
  - `S` — scene functions, one per card picture.
  - `STAGES`, `LEGS`, `KEYS` — stage names, progress labels, the four key points.
- No `localStorage` is needed. No network calls. No analytics.
- Every `<svg>` picture has `role="img"` and an `aria-label` describing it.
- The page is served by GitHub Pages from the `main` branch root.

### How to add a card

1. Decide the stage (`g`) and the position in the day's order.
2. Write title, lead and up to 3 bullets following section 2.
3. Choose the viewpoint from 5.1. Build the picture from existing helpers and the palette. One small explaining animation (section 7).
4. Add the scene function to `S` and the card to `CARDS`.
5. Update the "About N minutes" label and the card/question counts in `README.md` if they change.

### How to add a quiz question

1. Add `{q, o, a, why}` to `QUIZ`. Three options. One clearly right answer; wrong options must be plausible, not silly.
2. Add a picture to `QS` at the same index. It must not reveal the answer.

---

## 13. Checklist before you commit

- [ ] Text is plain, short, generic; no names, dates, places.
- [ ] No more than 3 bullets on the card.
- [ ] Only palette colours; coral/amber/sage used with their meanings.
- [ ] No outlines, textures, gradients, people.
- [ ] Viewpoint matches 5.1; mirror bigger than cameras; right-hand drive.
- [ ] Hardware matches section 6.
- [ ] Animation explains the rule; stopped cars have still wheels.
- [ ] Looks right in **both** themes and at 320–400 px width; no text overflow.
- [ ] Walk the whole flow: start → all cards → all quiz questions → name → completion card, with no console errors.
- [ ] Wrong-answer path works: wrong questions return, Reset turns coral, Back goes one step.
- [ ] `README.md` counts and this file are updated if anything changed.
- [ ] The commit message says what changed for the driver, not only what changed in the code.
