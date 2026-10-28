# Speed — Faster Than Real Time

**Outcome: a measured answer to "how
fast is it?" for two tiers of the same
voice, and a rule for when the expensive
tier is worth its cost.** Piper's own
receipt line is the instrument: after
each run it reports the **real-time
factor** — the seconds of computing
divided by the seconds of audio
produced. Below 1 is faster than the
speech plays; 0.25 means four seconds of
speech for every second of waiting.

## The experiment

The lab spoke the same four-sentence,
30-word paragraph (the third line of
`piper-lab/sentences.txt`, extended) with
lessac at **medium** and at **high**,
three runs each, on the same small
2-CPU machine. Full transcript:
`t03-speed.txt`. The real-time factors:

| Voice | Run 1 | Run 2 | Run 3 |
| --- | --- | --- | --- |
| lessac-medium | 0.24 | 0.27 | 0.19 |
| lessac-high | 1.08 | 0.96 | 1.83 |

And the speech itself was consistent:
about 10.4 to 11.0 seconds of audio each
time, 11.3 to 11.6 seconds per finished
file once the sentence pauses were in.

## Reading the result

**Medium is comfortably fast.** A factor
around 0.2 to 0.3 on a small shared
machine means a minute of narration in
roughly 15 seconds of computing — and
this machine was busy with other work
at the time, so a quiet machine of the
same size should do no worse. For the
uses in chapter 1 — announcements,
narration, reading aloud — medium is
never the bottleneck.

**High costs about five times as much.**
Its factors hover at and above 1: on
this machine, the high voice
*sometimes* took longer to make the
speech than the speech takes to play.
The file it makes is the same 22050 Hz;
the extra money buys a bigger network's
judgement, not more samples. Whether
that judgement is audible is a question
for ears; what the numbers settle is
the price — twice the disk (chapter 4)
and roughly five times the time.

**Timings move around.** The same text,
the same voice, three runs: 0.19, 0.24,
0.27. Other tenants on a shared machine,
the voice loading afresh each run, and
the model's own variability all stir
the pot. Treat any single real-time
factor as a weather report, not a
contract — the guide's numbers are
ranges for exactly this reason.

## The practical rules

- **Default to medium.** Move to high
  for the voice you will listen to for
  hours, on a machine with time to
  spare — never as a fleet default.
- **Batch work hides the cost.** Files
  made overnight or in a queue do not
  care about a factor of 1.8; anything
  spoken *in response* — an announcement
  reacting to an event — cares very
  much, and wants medium or lower.
- **Loading is part of the bill for
  short clips.** The voice took about
  0.7 seconds to load before the first
  word was made. For a two-second clip
  that is a third of the run. Programs
  that speak often should feed Piper
  many lines in one run (chapter 9)
  rather than starting it per sentence.
