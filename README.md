# Dash Cam Drive Guide

A short, mobile-friendly guide for drivers on dash cam road survey jobs.

Live page: https://andrewwang003.github.io/dashcam-drive-guide/

- 15 rule cards in four stages (before you drive, on the road, between sessions, after the last session), each with an animated picture
- 10-question quiz (tap an answer, then **Check answer**; missed questions come back at the end)
- A completion card for the driver to screenshot and send to their supervisor
- Daylight and dark theme (follows the phone; one button to switch)

The guide covers general rules only. Job details (routes, times, contacts) come from the supervisor.

## Use

Open the live page, or open `index.html` in a browser.

It is a single self-contained HTML file. It loads fonts from Google Fonts and nothing else, and it does not send or store any data.

## Update

**Read [`DESIGN.md`](DESIGN.md) first.** It holds the design rules for this page: purpose, wording, illustration style, palette and colour meanings, viewpoints and proportions, hardware facts, motion, theme, interaction, and a checklist. It is written so that an AI assistant or a new editor can keep the page consistent.

Then edit `index.html` and push to `main`. The card text is in the `CARDS` array, the quiz is in the `QUIZ` array, and the pictures are the `S` (cards) and `QS` (quiz) functions inside the script.
