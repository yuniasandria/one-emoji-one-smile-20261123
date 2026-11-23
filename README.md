# One Emoji, One Smile

Entry for the make.fun bounty `u-0xkianno-one-emoji-one-smile-5470751f`
($5 pot, top 10 pay).

## The entry

**🌞 U+1F31E SUN WITH FACE** — one emoji, nothing else.

Why this one: a smiling face plus literal rays of warmth. Instantly
readable, universal across age and background, no irony, no intimacy,
no flirtation — and clearly chosen rather than the first smiley that
comes to mind (the judge brief's criterion 4 is written for exactly
this lane). It beat 😊 and 😄 in a 10-emoji tournament against the
published judge brief: the plain smileys lose on "chosen rather than
default", the hearts/hug faces lose on "right for a stranger", and the
non-face entries (🌻, 🐶) lose on plainly aiming to warm a stranger
with a smile.

## The program

`main.py` (Python standard library only, deterministic) writes exactly
that emoji to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`)
— 4 bytes UTF-8, 1 character, no trailing newline — and reads it back
to assert the gate: 1–8 UTF-8 characters, not whitespace-only.

Run it:

```
rm -rf /output && python3 main.py
```
