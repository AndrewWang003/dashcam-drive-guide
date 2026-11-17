# Matrix guide principles

Shared design rules for every Matrix induction guide (the Dash Cam Drive Guide, the Xero Timesheet Guide, and any
guide made after them). **The same file sits in every guide repository. Change it in all of them at once.**

Each repository also has:

- `DESIGN.md`: what is special about that guide. It names its guide type (section 2) and never contradicts this file.
- `AGENTS.md`: short working rules for AI agents.

If the owner (Andrew Wang) gives an instruction that conflicts with this file, the owner wins. Then update this
file, in every repository, in the same change.

Last updated: 17 November 2026.

---

## 1. Who the guides are for

- Short-term workers. Many are new to the task, the tools and the company.
- Many do not have English as a first language.
- They read on their own phone, often in a hurry.
- They are not paid to read. Every extra line costs attention.

Everything below follows from this reader.

## 2. Two guide types

Decide the type first. It sets the structure.

| | Training guide | Task guide |
|---|---|---|
| Example | Dash Cam Drive Guide | Xero Timesheet Guide |
| Used | Read once, during the induction | Used while doing the task; opened again when something goes wrong |
| Goal | The reader remembers a few key rules | The reader finishes the task correctly |
| Flow | Linear, in the order of the working day | Linear, but any step can be opened directly |
| Progress | A progress bar with stages | A step strip: scroll sideways, tap any step |
| Points per card | **At most 3.** Attention is low. | **As many as the step needs, usually 2 to 5.** The reader's own pay or account depends on it, so they read with care. |
| Pictures | Drawn illustrations | Real screenshots of the tool, redacted |
| Details | General rules only. No dates, times, places or names. | Exact names from the tool: buttons, menus, rate names. |
| Backward button | `Back`, top-left: one page back | `Previous`, beside `Next`: the step before in order |
| End | Quiz and a completion card | A Help page: each common problem opens the step that fixes it |

A new guide uses one of these two types. If it needs something from both, say so in its `DESIGN.md` and explain why.

## 3. Content

### 3.1 Highest information density

The guide is complete and clear, and says nothing twice. An impatient reader finishes it only if no line is wasted.

- A fact appears once, where the reader uses it. The Help page or a recap may point back to it.
- A card has a lead sentence only if the lead says something the title and the points do not.
- No filler ("Two clicks.", "Look at it again.").
- Before adding a sentence, search the page for the same fact.

### 3.2 Plain words

- Short sentences. Common words. One idea per sentence. Verbs first: "Check REC before you start."
- No idioms, no slang, no jargon.
- One name for each thing, used everywhere.
- Say "your supervisor", never a person's name.
- Each point starts with a bold phrase, then a short explanation.
- Read each new sentence for double meanings.

### 3.3 The content comes from the owner

Rules about pay, hours, distances, times, safety and equipment come from the company's documents and from the
owner. Do not invent, guess or "improve" them. If a rule is unclear or looks wrong, leave the text as it is, write
the question in `DESIGN.md` ("Open questions"), and ask.

### 3.4 Honest pages

A page never claims to do what it does not do: it does not "send", "save" or "submit" anything unless it really does.

## 4. Look

### 4.1 Fonts

- Headings, buttons, labels: **Overpass** 600 / 800. Uppercase labels get letter-spacing.
- Body: **Atkinson Hyperlegible** 400 / 700, 17 px, line height 1.5. Chosen for readers of a second language.
- Codes and numbers: **Overpass Mono** 600.
- No other fonts.

### 4.2 Colour tokens

Every page colour is a CSS variable. Components never contain a colour value; only the token definitions do.
(An exception: black or white used only as an alpha mask, for example a fade at the edge of a scroller.)

| Token | Day | Night |
|---|---|---|
| `--bg` | `#F6F1E7` | `#0E1228` |
| `--surface` | `#FFFDF8` | `#171D3A` |
| `--ink` | `#141B3C` | `#F3EBDD` |
| `--muted` | `#5B6078` | `#A9AEC6` |
| `--line` | `#E2D9C8` | `#2B3359` |
| `--tint` (where a guide needs a second surface) | `#EFE7D7` | `#1F2647` |
| `--brand` / `--brand-ink` | `#F2A93B` / `#141B3C` | `#F2A93B` / `#141B3C` |
| `--amber` | `#F2A93B` | `#F2A93B` |
| `--coral` | `#D94A22` | `#FF7A52` |
| `--sage` | `#5E8F88` | `#7DB3AB` |

Night tokens are written twice: under `@media (prefers-color-scheme: dark){:root:not([data-theme="light"])}` and
under `:root[data-theme="dark"]`. Change both together.

### 4.3 Colour meaning (never break this)

| Colour | Means |
|---|---|
| **Amber** | Do this. The thing to press, the current choice, progress. |
| **Coral** | Stop, do not, watch out. Wrong answer. |
| **Sage** | Correct, done, OK. |
| **Navy** | Text, structure, neutral objects. |

- Do not add an accent colour. A second orange beside amber and coral blurs the meanings.
- Never use colour alone for right and wrong. Keep the words too.

### 4.4 Day and night

- Default follows the device. One round button, top-right, switches. Its icon shows the mode it switches **to**.
- Day is warm paper: light and open. **Navy is never a large filled area in day mode** (no navy buttons, banners or
  thick outlines). It looks heavy on a phone.
- Night is a night drive: deep navy, low glare. Coral and sage are lighter so they stay readable.
- Check every change in both modes.

### 4.5 Buttons

| Button | Style |
|---|---|
| Main (Start, Next, Check answer, the first-time choice) | Amber fill `--brand`, navy text `--brand-ink`, both modes |
| Main, not available yet | The same at 40% opacity |
| Secondary (Previous, Back, theme, Play, Reset) | `--surface` fill with a `--line` outline; Play has an amber outline |
| Selected answer | Amber outline and a light amber tint |

- One main button per screen, so the eye knows where to go.
- Buttons are **at least 44 px** high. Small items inside a scrolling strip (step chips and their arrows) may be 40 px, so the strip stays compact.

### 4.6 Layout

- One column on a phone. **The page must work at 320 px wide** with no sideways scrolling.
- Side gutters at least 16 px. Respect `env(safe-area-inset-*)`.
- Cards: `--surface`, 1 px `--line` border, 18 px radius, no drop shadow.

### 4.7 Pictures never move the page

The space a picture needs is kept **before** it loads, so text never jumps when the picture arrives.

- Drawn inline (SVG in the page): nothing to wait for.
- Image files: the page knows each picture's pixel size in advance, sets it on the image, and draws a placeholder
  in that exact space until the picture has downloaded. The placeholder is a skeleton of a screen: a few rounded
  bars on the `--tint` colour that keep growing and shrinking one after another, with a light sweeping across, so
  the reader sees that something is loading. It disappears when the picture is ready. A picture that fails to load
  keeps its placeholder.
- Marks drawn on a picture appear only when the picture is ready.

## 5. Motion

- **Motion must teach.** Every animation explains a rule or an action. Nothing moves for decoration.
- **Animations always play**, also when the device asks for reduced motion. The owner chose this after animations
  did not play on an iPhone. Keep the motion small, slow and calm.
- Slow enough to follow. Nothing flashes faster than once a second.
- Moving parts stay in step with what they show (a finger and the picture it moves are driven by one value).
- An animation that depends on a picture starts only when that picture is ready.
- A demonstration stops as soon as the reader touches the screen. It never hides content.
- Page change with a button: the new page slides in 30 px from the side it came from, in 0.22 s.

## 6. Navigation

- **Swipe left or right to change page** (touch only). Swipe left = next, swipe right = previous.
  - The page follows the finger, and the neighbour page comes in beside it, so the reader sees how far they are.
  - It changes page after 30% of the width, or after a quick flick. A shorter swipe springs back.
  - Up and down scrolling is never taken over: a gesture counts only when it is clearly sideways.
  - Where there is no page that way, the page resists and springs back.
  - **After a swipe the reader stays at the same scroll height**, so reading continues where the eyes already are.
    The neighbour page is drawn at that height during the swipe.
  - **Buttons (Next, Previous, a step chip) open the new page at its top.**
  - Pages where a swipe could skip something the reader must do (a quiz question, a required choice) do not swipe
    that way.
  - **Swipe hint, touch screens only:** the first time a swipeable page (a card or a step) opens in a visit, a thumb
    drags the page sideways with the caption "Swipe to change …", the neighbour page comes in beside it, and the
    page springs back. A thumb, because most people swipe with the thumb, and so it is not mistaken for the index
    finger of a click demo. Once per visit. Any touch stops it and hides it at once; a swipe that starts during the
    hint still changes the page (it may land on the neighbour page, so swipes are caught on the wrapper of both).
    It never runs at the same time as another hint or demo.
  - **On a computer, the only hint is the strip hint** (where a guide has a step strip that scrolls). Touch screens
    never get the strip hint.
- **One backward control.** A second "back" that goes somewhere different confuses readers.
- Left and right arrow keys change page on a computer.

## 7. Technology

- **One self-contained `index.html`** per guide: style, markup and one script. No build step, no framework.
- Content is data near the top of the script (cards or steps, quiz, Help). Change content there, not in markup.
- Image files, if any, live in `img/`. Nothing else loads from outside except the Google Fonts stylesheet.
- **No browser storage** (`localStorage`, `sessionStorage`, cookies). Choices last for the current visit only.
- No network calls, no analytics, nothing sent anywhere.
- Hosted with GitHub Pages from the `main` branch root.
- Every picture has a text alternative (`alt`, or `role="img"` with `aria-label`). Controls have a visible focus state.

## 8. Privacy

The repositories are public.

- No real names of workers or staff in text. In screenshots, names are covered; at most the first two letters stay.
- Hours, pay amounts, account numbers, email addresses and avatars are covered or cut out.
- Original, unredacted screenshots are never committed. Redaction is done on the original before anything is cut.

## 9. Working on a guide

- Read `GUIDE-PRINCIPLES.md`, then the guide's `DESIGN.md`, before changing anything.
- Explain the problem, how the page works now, and what the change alters, before you change it. Stay inside the task.
- Ideas the owner rejected are marked in `DESIGN.md`. Do not bring one back without asking.
- When a decision changes, update `DESIGN.md` (and this file if it is a shared rule) in the same commit.
- Report honestly: what you tested, what you only reasoned about, what you could not test.

### Checks before every commit

- [ ] Text: plain, short, nothing said twice; no names; content not invented.
- [ ] Colours: tokens only; amber, coral and sage used with their meanings; no navy fill in day mode.
- [ ] Day **and** night mode look right.
- [ ] 320 px wide: no sideways scrolling, no text out of its box. Also check a computer width.
- [ ] Buttons at least 44 px (strip items 40 px).
- [ ] With slow pictures, nothing on the page moves when they arrive.
- [ ] Every animation still teaches, and starts only when its picture is ready.
- [ ] Swipe: long swipe changes page at the same height, short swipe springs back, vertical drag only scrolls.
- [ ] Touch screen: the swipe hint plays once, on the first swipeable page; not on a computer.
- [ ] Walk the whole flow from the start page to the end, with no console errors.
- [ ] No browser storage, no network calls besides fonts.
- [ ] `DESIGN.md`, `README.md` and this file still describe the page.
