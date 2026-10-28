# Shaping the Voice

**Outcome: command of the five options
that change how a voice performs —
speaking rate, pauses, two kinds of
randomness, and the speaker switch —
each verified by measurement, including
the discovery that Piper never gives
quite the same performance twice.**
Every option below appears in
`piper --help`; every claim is from the
lab's transcripts `t04-length-and-silence.txt`
and `t05-speakers-and-noise.txt`.

## Length scale: the speaking rate

`--length_scale` stretches or squeezes
the phonemes: below 1 is faster, above
1 is slower. The lab spoke the pangram
three ways with the medium voice and
measured the finished files (each
includes the standard 0.2 s trailing
pause):

| `--length_scale` | File duration | Character |
| --- | --- | --- |
| 0.75 | 2.38 s | brisk |
| 1.0 | 2.95 s | the voice's natural pace |
| 1.5 | 3.62 s | deliberate |

The scaling is honest but not exact —
1.5 does not give precisely 1.5 times
the speech, because pauses and the
model's judgement do not stretch in
perfect proportion. Use it for pace, not
for hitting a target duration to the
tenth of a second.

## Sentence silence: the pauses

`--sentence_silence` sets the gap, in
seconds, that Piper leaves after each
sentence — the default is 0.2. The lab
raised it to 1.5 and the measuring
script saw the change without listening:
the file grew from about 2.8 to 4.18
seconds, and its zero samples — the
silence — rose from the usual 10% to
**38.2%**. Long pauses are how a folder
of spoken paragraphs gets breathing
room; they are also pure file size, at
44,100 bytes per second of silence for
a 22050 Hz voice.

## The noise options: the performance varies

A Piper voice does not recite; it
*performs*, and the performance is
sampled — drawn with an element of
chance — every run. The lab's proof is
blunt. The same sentence, the same
voice, twice in a row:

```bash
md5sum out/run-a.wav out/run-b.wav
```

```text
5248a49bfeac0e0978d569ac13bcc56a  out/run-a.wav
955521dba1699be1ab70212808a15233  out/run-b.wav
```

Different files: 2.86 seconds against
2.79, RMS −16.8 against −18.3 dBFS. Two
options govern the size of the chance:
`--noise_scale` (default 0.667), the
variation in the sounds themselves, and
`--noise_w` (default 0.8), the variation
in how long each sound lasts. The lab
then set `--noise_scale 0`, expecting
identical twins — and did not get them:
the two files still differed, at 2.89
and 2.88 seconds. Turning the noise down
narrows the variation; on this build it
does not abolish it. Plan accordingly:
**never build anything that depends on
two Piper runs matching**, and if a
particular reading is the one you want,
keep the file — you cannot order the
identical performance again.

## The speaker switch

For a multi-speaker voice (chapter 4),
`--speaker N` chooses who reads. The lab
took speakers 0, 5 and 100 from
libritts_r's 904, same sentence each:

| Speaker | Duration | RMS |
| --- | --- | --- |
| 0 | 2.36 s | −16.2 dBFS |
| 5 | 2.31 s | −17.1 dBFS |
| 100 | 2.19 s | −14.8 dBFS |

Measurements can prove the speakers
differ — pace and level both move — but
not *who* they are: the library does not
ship names or descriptions for the 904,
so choosing among them is listening work,
and the guide leaves it to the reader's
ears. Two warnings the lab earned.
First, on a **single-speaker** voice,
`--speaker 5` is silently accepted and
the same voice reads anyway — no error,
nothing to tell you the number was
meaningless. Second, past the end of a
multi-speaker voice, the model itself
crashes the program (speaker 904, when
903 is the last, aborts inside ONNX
Runtime with a bounds complaint —
transcript `t07-failures.txt`). Keep
speaker numbers inside the sidecar's
`num_speakers`, because nothing will
check for you until it is too late.
