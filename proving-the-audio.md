# Proving the Audio

**Outcome: a method — four checks, one
small script — that tells you a spoken
file really contains the speech, at the
right length, at a healthy level, using
nothing but arithmetic.** This chapter
exists because of how the guide was
written: the lab had no speakers and no
way to listen. Everything it claims
about Piper's output, it *measured*. The
method is worth having even with ears,
because speech tools fail silently in
ways a quick listen to the first file
will not catch in the hundredth.

## The script

The lab's measuring stick is a short
Python program, kept in the repository
as `piper-lab/check-wav.py`. For each
file it reports the header facts, the
duration, the **RMS level** (the average
loudness) and the **peak level**, both
in **dBFS** — decibels below the maximum
a 16-bit sample can hold — and the
percentage of samples that are exactly
zero. Silence, to this script, is not a
metaphor: a silent file would show an
RMS of minus infinity and 100% zeros.

```bash
python3 piper-lab/check-wav.py out/hello.wav
```

```text
out/hello.wav
  sample rate 22050 Hz, 1 channel(s), 16-bit
  62010 samples, 2.81 seconds
  RMS level -17.5 dBFS, peak -0.0 dBFS
  zero samples: 9.8%
```

(Transcript `t02-audio-checks.txt`.)

## Check one: the header tells the truth

The rate, channels and bit depth in the
file must match the voice's sidecar —
22050 Hz, mono, 16-bit for every voice
the lab ran. A mismatch means something
between Piper and your disk rewrote the
file, and everything downstream (players,
converters, other programs) will assume
the header is right.

## Check two: duration against word count

People speak at a fairly steady rate.
The lab's sentence has nine words and
took 2.61 seconds of speech — 3.4 words
per second, about 207 words a minute, a
normal reading pace. A paragraph of 30
words took about 10.5 seconds. So: count
the words, divide by the seconds, and
distrust anything far outside roughly
2 to 4 words per second. This one check
catches the classic disasters — a file
that contains only the first sentence, a
file stretched to ten times its length
by a wrong sample rate, an empty file —
without listening to a second of it.

## Check three: levels, not silence

Healthy speech from Piper sits around
−20 to −14 dBFS RMS, with peaks reaching
near 0 dBFS — every file the lab made
peaked at −0.0, the loudest sample
touching full scale, which is the
model's natural output level rather than
distortion you need to fix. The
signatures of trouble are equally clear:
an RMS far below −40 dBFS means a
whisper or near-silence; 100% zero
samples means true silence wearing a
WAV costume. The zero percentage has a
legitimate use too: it is mostly the
pauses, so it *rises* when the pauses
do — chapter 8's 1.5-second
sentence-silence file reads 38.2% zeros
against the usual 10%, which is how the
lab proved the pause really was in the
file.

## Check four: the size arithmetic

A 16-bit mono file holds 2 bytes per
sample. Samples × 2, plus 44 bytes of
header, should equal the size on disk to
the byte. If it does not, the file was
truncated or is still being written.
This is the check that catches a Piper
run interrupted halfway — the header may
still parse while the speech stops
early.

## Where this method stops

Measurement proves the audio is real,
the right length, and at a healthy
level. It cannot prove the voice said
the *right words* — a mispronunciation
measures exactly like a correct reading,
and a sentence silently dropped between
two others would only show as a slightly
short duration. (The obvious closing of
that gap — feeding the file to a speech
*recognizer* and comparing texts — needs
a recognizer such as Whisper installed;
the lab did not have one, and so did not
do it. It is labelled here as an open
door, not a result.) Ears, in the end,
remain the only complete check. This
chapter's method is what you use when
ears do not scale — and it catches every
failure the lab actually met.
