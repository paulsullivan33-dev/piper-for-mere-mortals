# Piper for Mere Mortals

Most text to speech lives in the cloud:
you send your text to someone else's
computer, and a voice comes back. **Piper**
does the same job with the cloud left out.
It is a program you run on your own
machine, it reads text you give it, and it
writes an ordinary **WAV file** — spoken
audio, made by a **neural network voice**
that lives in a file on your disk. No
account, no subscription, and no network
connection needed once the voice is
downloaded. The text never leaves the
machine, which is the whole point for
anything you would rather not read out
loud to a data centre.

This guide explains how Piper turns
writing into sound, how to install it,
how to choose and download a voice, and
how to make your first spoken file. Then
it does something most speech-tool guides
skip: it **proves** the audio is real.
The lab that wrote this guide had no
speakers and no ears — it could not
listen to a single file it made. So every
claim here is checked by measurement
instead: the file's header, its duration
against its word count, its sound levels
sample by sample. That turns out to be a
good habit for anyone, ears or not,
because a speech program that fails
quietly still writes a file — sometimes
an empty one.

The lab behind this guide ran the real
thing: **Piper 1.2.0**, the official
release binary, on a small Linux machine,
with three downloaded voices — the same
voice (**lessac**, US English) at
**medium** and **high** quality, and
**libritts_r**, a voice with 904 speakers
inside it. Against them the lab spoke
single sentences and a paragraph, timed
the work against the length of the audio
produced, stretched and squeezed the
speaking rate, switched speakers, fed
text a line at a time and as JSON, took
the headerless raw output and rebuilt a
WAV from it, and deliberately broke
things: a missing voice file, a voice
whose config file had been taken away, a
speaker number the voice does not have,
and an empty input — which, it turns
out, succeeds silently and writes
nothing at all.

What the lab could not do, it did not
fake. It could not listen, so it never
claims one voice *sounds* better than
another; it reports sizes, sample rates
and timings, and leaves the listening to
you. Voices for languages other than
English, the Python package form of
Piper, and Piper's life inside other
programs (such as Home Assistant) are
taught from the documentation and
labelled as such wherever they appear.
`criteria.md` keeps the full ledger of
what was run and what was only read.

## What this guide covers

- [**What Piper is**](what-piper-is.md) —
  the mental model: text in, spoken WAV
  out, everything on your own machine,
  and why that privacy is the feature
- [**The moving parts**](the-moving-parts.md) —
  the program, the phonemizer that turns
  text into sounds, the voice model, its
  config sidecar, and the WAV writer —
  and which part holds what
- [**Installing Piper**](installing-piper.md) —
  the release download, what is inside
  it, and the version check that proves
  it runs
- [**Voices — finding and choosing one**](voices.md) —
  the voice library's layout, the four
  quality tiers and what they cost in
  size and sample rate, and the two
  files every voice needs
- [**Your first synthesis**](your-first-synthesis.md) —
  one sentence in, one WAV out, and a
  first look at the file with three
  independent tools
- [**Proving the audio**](proving-the-audio.md) —
  how to know a speech file really
  contains speech: headers, duration
  against word count, and sound levels
  measured sample by sample
- [**Speed — faster than real time**](speed.md) —
  the real-time factor, measured for a
  medium and a high quality voice, and
  what the expensive tier costs
- [**Shaping the voice**](shaping-the-voice.md) —
  speaking rate, the silence after
  sentences, the noise options, and the
  speaker switch in multi-speaker voices
- [**Paragraphs, lines and JSON input**](paragraphs-lines-and-json.md) —
  how Piper splits sentences, the three
  ways to feed it text, one file per line
  or one file for everything, and the
  headerless raw output for piping
- [**Recipes**](recipes.md) — read a file
  aloud into a folder of clips, make a
  narration track for a paragraph at a
  time, build a two-voice conversation,
  and check a whole folder of output in
  one pass
- [**The neighbours**](the-neighbours.md) —
  espeak-ng the robot, Festival, the
  cloud voices, and Whisper coming the
  other way: what each does that Piper
  doesn't, and vice versa
- [**Limits**](limits.md) — one voice at
  a time, WAV or raw samples and nothing
  else, no emphasis or pronunciation
  controls, output that is never quite
  the same twice, and crashes that are
  not polite errors
- [**Troubleshooting**](troubleshooting.md) —
  the abort with no usage message, the
  missing config sidecar, the file that
  was never written, the speaker number
  that crashes the model, and the traps
  this guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Training or fine-tuning a voice of your
own — that is a project with its own
tooling and its own guide's worth of
material; this one uses voices other
people trained. Cloning a real person's
voice is likewise out, in every sense:
Piper's library voices are recordings of
volunteers and datasets, not a way to
imitate your neighbour. Real-time
conversation, telephone systems and
screen readers are pointed at, not
taught — Piper makes files (and one raw
stream) here, and chapter 12 is honest
about where its edges are.

## How to use this guide

Read chapter 1 for the model, and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapters 3 and 4 get you a program and a
voice; chapter 5 speaks in the same
sitting. Chapter 6 is the one to read
slowly even if you have speakers: its
checks are how you catch the silent
failures — including the empty input
that reports success and writes nothing —
before they reach anything that depends
on the audio. The lab's transcripts live
in `piper-lab/transcripts/`; its sample
sentences are `piper-lab/sentences.txt`
and its measuring script is
`piper-lab/check-wav.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Whisper for Mere Mortals](https://paulsullivan33-dev.github.io/whisper-for-mere-mortals/)
- [ffmpeg for Mere Mortals](https://paulsullivan33-dev.github.io/ffmpeg-for-mere-mortals/)
- [Local AI at Home for Mere Mortals](https://paulsullivan33-dev.github.io/local-ai-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/piper-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/piper-for-mere-mortals/blob/main/LICENSE-CODE).
