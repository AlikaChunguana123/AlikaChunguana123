# Paris — English version

Same cuts, same fonts, same positions as the Portuguese set. Only the words change.

| # | File | Length | On-screen text |
|---|------|--------|----------------|
| 0 | `0-notluck-predestined-EN.mp4` | 9.2 s | IT WASN'T LUCK. → PREDESTINED. → ON MY SHIRT. |
| 1 | `1-notredame-EN.mp4` | 7.6 s | 8:04 PM. Notre-Dame. |
| 2 | `2-notluck-EN.jpg` | — | IT WASN'T LUCK. / It's written on my back. |
| 3 | `3-middleofdinner-EN.mp4` | 14.9 s | this happened IN THE MIDDLE OF DINNER |
| 4 | `4-wholeroom-EN.mp4` | 15.0 s | The whole room stopped. |
| 5 | `5-twometres-EN.mp4` | 15.0 s | and I was TWO METRES AWAY |
| — | `opera-1-EN.mp4` | 15.0 s | I thought opera WAS STUFFY. |
| — | `opera-2-EN.mp4` | 13.4 s | my face SAYS IT ALL. |
| — | `opera-3-EN.mp4` | 14.1 s | by the end, the whole room RAISED A GLASS. |
| — | `belcanto-invite-EN.mp4` | 11.4 s | GO TO BEL CANTO. → AT YOUR TABLE. → BEL CANTO · PARIS |
| 6 | `6-oneday-EN.jpg` | — | ONE DAY. THAT ONE. |
| 7 | `7-singers-EN.jpg` | — | I STAYED TO MEET THEM |

## How each one was made

Three groups, three methods.

**Text I had added myself** (0, 5, the three opera clips, the invitation) —
re-rendered straight from the source footage with English captions. Nothing
was removed, so there is no quality loss at all.

**Cards 2 and 6** — these started life in English. They are your own
originals, untouched.

**Text burned into the footage by you** (1, 3, 4) and **card 7** — the
Portuguese had to come off first. The captions are perfectly static while
the background moves, so each one was located by fitting the typeface to
the measured glyph widths, then removed with a stroke-shaped mask
(`removelogo`, or TELEA inpainting for the still). The English was then
drawn back at the same size, position and style:

| Clip | Typeface fit | Baselines |
|------|--------------|-----------|
| 1 | Arial Bold 52, tracking −1, left 75 | 1528 |
| 3 | Arial Bold 55 (small) and 101 (caps), tracking +1 | 357 / 473 / 577 |
| 4 | Arial Bold 86, white fill with a gold outline | 396 / 489 |
| 7 | Arial Bold 80, tracking −4 (card is 900×1600) | 318 / 397 / 475 |
