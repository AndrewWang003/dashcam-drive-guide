# Dash Cam Drive Guide

A short, mobile-friendly guide for drivers on dash cam road survey jobs.

Live page: https://andrewwang003.github.io/dashcam-drive-guide/

- 15 rule cards in four stages (before you drive, on the road, between sessions, after the last session), each with an animated picture
- A progress bar with one dot per card and the quiz as the last dot: tap a dot, or drag along the bar, to go back to any card, or back to the quiz
- 10-question quiz (tap an answer, then **Check answer**; missed questions come back at the end)
- A completion card for the driver to screenshot and send to their supervisor
- Daylight and dark theme (follows the phone; one button to switch)
- Text size button (four sizes) and the phone's Back button goes to the page before

The guide covers general rules only. Job details (routes, times, contacts) come from the supervisor.

## Use

Open the live page, or open `index.html` in a browser.

It is a single self-contained HTML file. It loads fonts from Google Fonts and nothing else, and it does not send or store any data.

## Update

**Read [`GUIDE-PRINCIPLES.md`](GUIDE-PRINCIPLES.md) and [`DESIGN.md`](DESIGN.md) first.** `GUIDE-PRINCIPLES.md` holds the rules shared by every Matrix guide (the same file is in each guide repository); `DESIGN.md` holds the rules for this page only. AI agents also read [`AGENTS.md`](AGENTS.md). It holds the design rules for this page: purpose, wording, illustration style, palette and colour meanings, viewpoints and proportions, hardware facts, motion, theme, interaction, and a checklist. It is written so that an AI assistant or a new editor can keep the page consistent.

Then edit `index.html` and push to `main`. The guide's text is at the top of the script: the `CARDS` array (each card names its picture with `pic`) and the `QUIZ` array. The pictures are the `S` (cards) and `QS` (quiz) functions below it.

Code shared with the other Matrix guides (colour tokens, fonts, theme switch, swipe hint, text size) sits between `SHARED:` markers. Change it in one guide, then run `python3 tools/shared.py copy ../other-guide` and `check` (with the other guide's repository beside this one), test both and commit both.
