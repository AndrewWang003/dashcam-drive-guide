# DESIGN.md — design rules for the Dash Cam Drive Guide

**Read [`GUIDE-PRINCIPLES.md`](GUIDE-PRINCIPLES.md) first.** It holds the rules shared by every Matrix guide (the same file is in each guide repository). This file holds what is special about the Dash Cam Drive Guide and never contradicts it. **Guide type: training guide** (GUIDE-PRINCIPLES.md section 2).

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
- Each card: a title, a lead sentence only if it says something the title and bullets do not (shared rule: highest information density), and **at most 3 bullets** (training guide). Each bullet starts with a bold keyword phrase, then a short explanation.
- Check every new sentence for double meanings. Known traps: "the whole time" (say "the whole session"); "each part" (say what part).

---

## 3. Page structure

Top bar (always visible):

- **Back** button, top-left. Goes back exactly one page, also inside the quiz.
- Title and position text ("Card 3 of 15", "Question 2 of 10").
- **Theme button**, top-right (section 8).
- **Route progress bar** with five stages: `BEFORE · ROAD · BREAK · AFTER · QUIZ`, **one dot per card**, and **the quiz as the last dot**. It is the stage map, the progress indicator and a card picker (section 10, "Card dots").
  - **The line ends at the quiz dot.** Nothing comes after it, so a full line means the whole guide is done. The amber fill runs to the current dot; in the quiz and on the name and finish pages the line is full. The number of correct answers is in the text above the bar ("Quiz · 3 of 10 correct"), not in the line.
  - **All dots are the same distance apart**, whatever their size (owner's request): 16 dots (15 cards and the quiz) spread evenly along the line, so a stage takes space by its number of cards. At 320 px the dots are about 18 px apart.
  - **Key dots** are bigger (13 px), with a navy ring when reached: the first card of each stage, and the quiz dot. The last card ("Remember these 4") is a small dot just before the quiz dot.
  - **Stage labels** sit under their key dots. BREAK has one card, so BREAK and AFTER are only one dot apart and their labels would touch. The script (`layoutLabels`) centres each label under its key dot, keeps it inside the bar, and pushes neighbours apart to keep 6 px between labels. At 320 px BREAK moves a little to the left of its dot; at wider screens every label sits under its dot. It runs again on resize and when the fonts have loaded.
  - Other dots: the current one = 16 px amber with a navy ring and a soft amber halo; already opened = small amber; not opened yet = small hollow.

Flow:

1. Start page: title, "About 7 minutes", the four key points, Start button.
2. 15 cards, grouped in four stages (`STAGES` in the script): Before you drive, On the road, Between sessions, After the last session. Each card shows a stage chip.
3. The last card repeats the four key points.
4. Quiz: 10 questions.
5. Name entry, then the completion card for the screenshot.

Rules:

- One card on screen at a time. One narrow column. Must work at 320 px width with no sideways scrolling.
- Order cards in the order the driver does things during the day.
- **Changing page:** on the start page and the cards, the reader can tap the buttons or **swipe left / right**. The quiz, the name page and the finish page do not swipe (section 10).
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
- All pictures are inline SVG produced by helper functions in the script (`rect`, `circle`, `text`, `svg`, `arc`, `carSym`, `cabin`, `cams`, `wiring`, `outside`, `check`, `no`, …).
  Classes used inside pictures for their animations have specific names (`plug-on`, `plug-off`, `plug-lead`, `clock-hand`, `lane`, …), never generic page words like `on` or `lead`. **Reuse these helpers.** Do not add image files, icon fonts or libraries.
- Card pictures use `viewBox="0 0 360 220"`; quiz pictures are shorter (170, or 196 for cabin views).

### 4.1 Palette (fixed)

Illustration constants (in the script):

| Name | Hex | Use |
|---|---|---|
| `NAVY` | `#141B3C` | Brand colour. Cameras, cabin frame, road, structure |
| `NAVY_2` / `NAVY_3` / `NAVY_DARK` | `#33407A` / `#232B52` / `#0A0E22` | Navy shades, shadows |
| `CREAM` / `WHITE` | `#F3EBDD` / `#FFFDF8` | Light surfaces, text on navy |
| `AMBER` / `AMBER_DARK` | `#F2A93B` / `#DB932A` | **Action and progress** |
| `CORAL` / `CORAL_DARK` | `#E4572E` / `#C4441F` | **Attention and prohibition** |
| `SAGE` | `#5E8F88` | **Correct, done, OK** |
| `SKY` / `SKY_2` / `MIST` | `#DCE9E8` / `#C9DBD8` / `#B9CFCB` | Sky, far hills |
| `SAND` / `SAND_2` / `SAND_3` | `#D8C9AE` / `#C4B393` / `#BCA988` | Sand: ground, dashboard |
| `GREY` | `#B8BCC8` | Neutral grey: other cars, metal |

Page tokens (CSS variables on `:root`; the shared block `tokens`, GUIDE-PRINCIPLES.md 4.2):

| Token | Light | Dark |
|---|---|---|
| `--bg` | `#F6F1E7` | `#0E1228` |
| `--surface` | `#FFFDF8` | `#171D3A` |
| `--ink` | `#141B3C` | `#F3EBDD` |
| `--muted` | `#5B6078` | `#A9AEC6` |
| `--line` | `#E2D9C8` | `#2B3359` |
| `--brand` / `--brand-ink` | `#F2A93B` / `#141B3C` | `#F2A93B` / `#141B3C` |
| `--amber` | `#F2A93B` | `#F2A93B` |
| `--coral` | `#D94A22` | `#FF7A52` |
| `--sage` | `#5E8F88` | `#7DB3AB` |
| `--tint` | `#EFE7D7` | `#1F2647` |

This guide's own tokens, after the shared block: `--scene-bg` (picture background, cream in both modes),
`--scene-edge` (picture edge, only at night), `--amber-soft` (selected quiz answer) and `--amber-halo` (ring around
the current progress dot).

Do not add colours. If something needs to stand out, use the meaning table below.

### 4.2 Colour meaning (never break this)

| Colour | Means | Examples |
|---|---|---|
| **Coral** | Stop, don't, look here | REC dot, prohibition signs, wrong answer, gauge needles |
| **Amber** | Do this, movement, progress | Lane lines, plugs and adapter, progress fill, camera view box, all main buttons |
| **Sage** | Correct, done | Check badges, OK, right answer |
| **Navy** | Brand, structure, neutral objects | Cameras, cabin, road |

- The **survey car is always coral** (symbol `car`): it is the one thing to watch in every side-view picture. Other traffic is sage or dark blue (`carB`, `carC`).
- A prohibition is always the **coral circle with a diagonal bar** (`no()` helper). A lock icon was tried and was not understood **(rejected)**.
- Never use colour alone for right/wrong in the quiz; keep the text feedback too.

### 4.3 Text inside pictures

Keep it to short labels only: `REC`, `12V`, `A`, `B`, `000`, `OK`, `TIME'S UP`, odometer digits, numbers. All explanation goes in the HTML text below the picture. Text must never overflow its shape.
- **Main buttons are amber with navy text in both themes** (`--brand`): Next / Start / Check answer, the Power on and Between sessions step button, the selected A / B button. A navy button was tried in daylight mode and felt too heavy on a phone and out of place in a light theme **(rejected)**. Secondary buttons (Back, theme, Reset) stay outlined on the surface colour.

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

Each camera has **its own view region** (two cameras, two regions that overlap in the middle). A region is a pyramid: the camera is the tip, and a translucent amber rectangle on the road ahead is the far end.

Solid and dashed lines follow the **hidden-line convention of technical drawing**: an edge the viewer can see is solid; an edge hidden behind a surface is dashed. The viewer sits in the driver's seat, so the cameras are near and the rectangles are far.

- **Solid, thin (1.5):** the four edges from each camera to the corners of its rectangle. They are on the near side, so nothing hides them.
- **Solid (1.8):** the left, right and bottom outline of the two rectangles together.
- **Dashed (darker amber `AM2`, width 2, dash `6 4`):** the far top edge of the rectangles (behind the view volume), and the two inner side edges (each sits behind the other camera's view volume).
- Never dash a line just because it crosses a coloured area on the flat picture. Ask whether it is in front of or behind that surface.

Earlier versions were rejected: downward triangles (looked like cameras pointing down), a flat viewfinder frame, two solid trapezoids, **one merged region for both cameras** (it hides that each camera records its own view), and dashing the near edges where they cross the rectangle (wrong way round).

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
- **Page change (start page and cards only):** with Next / Back the new page slides in 30 px from the side it came from (0.22 s). With a finger swipe the page follows the finger and the neighbour page comes in beside it. **The quiz has no page-change motion**, so the reader's attention stays on the question.
- No rotating gear. The gear icon is static.
- No curved detour line jumping over a road barrier **(rejected)**.
- Use `transform-box` / `transform-origin` carefully for SVG parts. The adapter lead scales from a fixed end so it never shows from under the adapter.

---

## 8. Light and dark theme

### 8.1 Mechanics

- Default follows the device (`prefers-color-scheme`).
- One round button, top-right, toggles `document.documentElement.dataset.theme`.
- **The icon shows the mode you will switch to**: a moon in daylight mode, a sun in dark mode. This is the owner's choice.
- All page colours come from the tokens in 4.1. Never write a page colour as a hex value in a component; use a token.
- Dark tokens are defined twice: under `@media (prefers-color-scheme: dark){:root:not([data-theme="light"])}` and under `:root[data-theme="dark"]`. Change both together.

### 8.2 Character of each theme

**Daylight** — warm paper. Light, calm, open.
- Page `--bg` cream `#F6F1E7`, cards `--surface` off-white `#FFFDF8`, text `--ink` navy `#141B3C`, hairlines `--line` sand `#E2D9C8`.
- **Navy is for text, icons and the pictures only.** Do not use navy as a large filled area or a thick outline in the page UI (buttons, selected states, banners). It looks heavy on a phone and breaks the light feel **(rejected: navy main buttons, navy outline on the selected quiz answer)**.
- Highlights are amber; status is sage (right) or coral (wrong / don't).

**Dark** — night drive. Deep navy, low glare.
- Page `--bg` `#0E1228`, cards `--surface` `#171D3A`, text `--ink` cream `#F3EBDD`, hairlines `--line` `#2B3359`.
- Coral and sage are lighter here (`#FF7A52`, `#7DB3AB`) so they stay readable on navy.
- Picture frames get a thin border (`--scene-edge`) so they do not melt into the page.

### 8.3 Rules that are the same in both themes

| Element | Style |
|---|---|
| Main button (Start, Next, Check answer, step button, selected A / B) | Amber fill `--brand`, navy text `--brand-ink` |
| Main button disabled | Same, at 40% opacity |
| Secondary button (Back, theme, Reset) | `--surface` fill, 1.5 px `--line` outline, `--ink` text |
| Selected quiz answer (before Check) | Amber outline (2 px + 2 px inset) and a light amber tint `rgba(242,169,59,.16)` |
| Right answer / done | Sage outline, `--ok-bg` tint |
| Wrong answer / don't | Coral outline, `--bad-bg` tint |
| Progress fill, stage chip outline, bullet dashes | Amber |
| Pictures (SVG) | Same palette in both themes (4.1); they are not recoloured |

When adding a new component: if it is the thing to press or the current choice, make it amber; if it is a status, use sage or coral; everything else stays on `--surface` / `--line`. Then check it in **both** themes before committing.

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
- A break during a session is allowed at any time, 10 minutes at most (9.3).

### 9.3 Breaks during a session

- Confirmed by the manager (Nov 2026): **a driver may take a break at any time during a session, but only up to 10 minutes.** It is on the "Stay on your route" card.
- This **replaces** the "15-minute break after every 2 hours" line in the company method document. Do not add the 15-minute rule.
- Not decided: whether the cameras stay on during a break. The page says nothing about it; do not invent a rule.

---

## 10. Interaction

- Touch targets at least 44 px. Buttons have visible focus and pressed states.
- **Swipe to change page** (touch only): swipe left = next, swipe right = previous. It works on the start page and the 15 cards.
  - It changes page after 30% of the width, or after a quick flick. A shorter swipe springs back.
  - Up / down scrolling is never taken over: a gesture counts as a swipe only when it is clearly sideways.
  - Where there is no page that way (right on the start page, left on the last card) the page resists and springs back. **The last card does not swipe into the quiz**: starting the quiz is a deliberate tap on the button.
  - **Swipe hint (touch screens only):** the first swipeable page opened in a visit — normally the **start page**, with card 1 coming in beside it — shows a thumb that drags the page sideways with the caption "Swipe to change card", then the page springs back. Once per visit; any touch stops it; not on computers (shared rule).
  - **After a swipe the reader stays at the same scroll height** (owner's request), so reading continues where the eyes already are. The neighbour page is drawn at the same height during the swipe, so nothing jumps when it ends. If the new page is shorter than the current scroll position, the browser moves up to the end of that page; that is expected.
  - **Next / Back buttons still go to the top of the new page.** The Next button sits at the bottom of a card, so keeping the height there would open the next card at its end.
  - **No swipe in the quiz, the name page or the finish page.** A sideways swipe there must do nothing, so an answer can never be skipped by accident.
  - Code: `cardHTML(n)` / `startHTML()` build a page as a string so the neighbour can be drawn in `#peek`; `renderCard()` then binds the buttons on the real page. Keep that split when adding interactive cards.
- **Card dots** (owner's request, Nov 2026): tap a dot in the progress bar, or drag a finger (or the mouse) along it, to open any card. This is for review: after reading, the driver can go straight back to one card instead of tapping Back many times.
  - **Guide-type note:** "open any card directly" comes from the task guide type (GUIDE-PRINCIPLES.md section 2). The page stays a training guide; it borrows only this, because drivers review cards before and during the quiz.
  - The dots are small, so **the whole strip is the touch area**: the dot nearest the finger opens. A touch more than 16 px from every dot does nothing.
  - **The quiz dot** works only after the quiz has started (with the last card's button); before that it is disabled, so the quiz is still started by a deliberate tap. After that it goes back to **where the driver left the quiz**: the same question with its answer and feedback, or the name page, or the finish page. It never restarts the quiz or skips a question.
  - A tap cancels the browser's follow-up click. Without that, the click can land on the Back button (the page has just scrolled to the top) and go one page back.
  - A tap opens the card at its top, with the normal slide-in. While dragging, the card changes as the finger passes each dot, with no slide; only the card where the drag ends is marked as opened. An up / down move on the strip is left to page scrolling.
  - From the quiz, the name page or the finish page, a dot still opens a card. Quiz answers are kept; the quiz dot, or the last card's button ("Back to the quiz" / "Back to the finish"), leads back. Jumping out of the quiz skips nothing.
  - **The last card never swipes into the quiz** (owner's decision), also after the quiz has started. Starting or going back to the quiz is a tap: the last card's button, or the quiz dot.
  - **All cards can be opened, also ones not read yet.** This adds no new skip: a swipe could already reach the last card, and the quiz still checks the rules.
  - **Back** still goes one page back in card order, not to the card the driver jumped from.
  - Keyboard: each dot is a button ("Card 3: Camera setup", "Quiz: back to where you were"); Enter or Space opens it.
- **Arrow keys** (computer): right = next, left = previous, on the start page and the cards, the same as a swipe. The
  last card does not go into the quiz, and the keys do nothing in the quiz, the name page and the finish page.
- **Phone / browser Back button** (GUIDE-PRINCIPLES.md 6): goes to the page visited before, which can differ from
  the `Back` button after a jump with the card dots (`Back` = one page back in card order). Quiz questions each get an
  entry; answers and the typed name are kept. A drag along the dots adds one entry, for the card where it ends.
  After a reload the guide starts again (nothing is stored); an older entry for the quiz or the finish then opens
  the last card, because the quiz has not been started in this visit.
- **Screen readers:** the page area is not a live region. Each page change moves focus to the page title, which is
  read once (it used to read the whole card, picture descriptions too, sometimes twice). The quiz answer feedback has
  its own live region (`role="status"`), so "Correct" / "Not quite" is still read out after Check answer.
  - No hint teaches the dots (none was asked for).
- **Quiz:** tap an answer to select it, then tap **Check answer**. This two-step design prevents accidental taps. Feedback shows right/wrong with a one-line reason. Wrong questions **come back at the end** until all are right. **Reset** sits top-right of the quiz and turns coral after a wrong answer. **Back** goes to the previous question, it does not restart the quiz.
- **Quiz pictures set the scene and never show the answer.**
- **Power on** card: two taps (cameras → adapter, then adapter → car). Unplug returns to step 1.
- **Between sessions** card: one button toggles recording / stopped.
- **Finish where you started** card: A / B chooser.
- Completion card: the driver's name with date and time, inside an amber border — made for a screenshot.

---

## 11. Typography and layout

- Display: **Overpass** 600/800 (headings, buttons, labels; uppercase labels use letter-spacing).
- Body: **Atkinson Hyperlegible** 400/700, 17 px at the default text size, line-height 1.5. Chosen for legibility for non-native readers.
- **Text size control** (`Aa`, top right, left of the theme button): four sizes, 90 / 100 / 115 / 130 %, as in
  GUIDE-PRINCIPLES.md 4.8. Here the top bar and the progress bar keep their size, and so do the drawn pictures
  (SVG text is part of the picture). The top bar is not sticky in this guide, so `Aa`, like the theme button, is
  reached at the top of the page. Checked: every card, the quiz and the finish page at 130 % and 320 px, no text
  out of its box.
- Numbers and codes: **Overpass Mono** 600.
- No other fonts. In SVG, text uses Overpass or Overpass Mono.
- Cards: `--surface` background, 1 px `--line` border, 18 px radius. No drop shadows.
- Side gutters at least 16 px, and respect `env(safe-area-inset-*)`.

---

## 12. Technical rules

- Keep everything in **one self-contained `index.html`**: `<style>`, markup, one `<script>`.
- **The script, top to bottom:** content (the text of the guide), the picture palette and drawing helpers, card
  pictures `S`, quiz pictures `QS`, then the page logic. Code shared with the other guides sits between
  `SHARED:` markers (GUIDE-PRINCIPLES.md 7); change it as described there.
- Content, at the top of the script (change the guide's text here):
  - `CARDS` — `{g, t, pic, lead, pts, plug?, choose?, keys?}`: `g` is the stage index, `t` the title, `pic` the picture name in `S`, `pts` the bullets.
  - `QUIZ` — `{q, o, a, why}`: question, options, index of the right answer, one-line reason.
  - `STAGES`, `LEGS`, `KEYS` — stage names, progress labels, the four key points.
- Pictures: `S` (card pictures, by name) and `QS` (one per quiz question, same order as `QUIZ`).
- Pages are numbered: 0 = start, 1 to `NCARDS` = the cards, then `PAGE.quiz`, `PAGE.name`, `PAGE.done`.
  `isCard(n)` says whether page `n` is a card. Use these names, never `NCARDS+1` and so on.
- No `localStorage` is needed. No network calls. No analytics.
- Every `<svg>` picture has `role="img"` and an `aria-label` describing it.
- The page is served by GitHub Pages from the `main` branch root.

### How to add a card

1. Decide the stage (`g`) and the position in the day's order.
2. Write title, lead and up to 3 bullets following section 2.
3. Choose the viewpoint from 5.1. Build the picture from existing helpers and the palette. One small explaining animation (section 7).
4. Add the picture to `S` under a name, and the card to `CARDS` with `pic:'that name'`.
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
