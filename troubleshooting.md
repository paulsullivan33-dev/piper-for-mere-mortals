# Troubleshooting

The failures the lab met for real, in
roughly the order a new user meets them.
Transcripts: `piper-lab/transcripts/t07-failures.txt`
unless another is named.

## The program aborts: "Model file doesn't exist"

```text
terminate called after throwing an instance of 'std::runtime_error'
  what():  Model file doesn't exist
```

Piper aborts — exit code 134, no usage
text, no apology — when `--model`
points at a file that is not there. The
message is exact even if the manner is
abrupt: check the path. The common cause
is downloading the archive and expecting
the model inside it; voices are a
separate download (chapter 4). A subtler
cause is the archive-name trap from
chapter 3: an error page saved under a
plausible filename. `ls -la` the model:
a real lessac-medium is 63 MB, not 9
bytes.

## "Model config doesn't exist"

The voice's second file — the
`.onnx.json` sidecar — is missing, or
not where Piper looks. Piper finds it by
adding `.json` to the model path, so
`voices/en_US-lessac-medium.onnx` wants
`voices/en_US-lessac-medium.onnx.json`
*in the same folder, with exactly that
name*. Renaming the model without
renaming the sidecar breaks the pair;
copying the `.onnx` alone (the lab did)
breaks it too. Either restore the
sidecar beside the model or pass
`--config` explicitly.

## It exited 0 — and there is no file

The emptiest trap in the guide. Empty
input is not an error: no text, exit 0,
no file, no complaint. In a script this
usually means the *input* never arrived
— an empty variable, a previous command
in the pipe producing nothing, a file
that was not there. Debug the pipe, not
Piper: put an `echo` of the actual text
in front of the run, and afterwards
always test that the output file exists
and measures (chapter 6) before anything
consumes it.

## The crash inside ONNX Runtime, about a Gather node

```text
indices element out of data bounds, idx=904 must be
within the inclusive range [-904,903]
```

You asked for a speaker the voice does
not have. The range in the message is
the truth: speakers are numbered from 0
to `num_speakers − 1` in the sidecar —
903 for libritts_r. The mirror-image
trap is quieter: on a *single-speaker*
voice, an out-of-range `--speaker` is
silently ignored and the one voice reads
anyway, so "the speaker option does
nothing" on such a voice is expected,
not a bug.

## The voice plays too fast, too slow, or like a giant

The sample rate was assumed wrongly
somewhere. Piper writes at the voice's
rate (22050 or 16000 Hz); only the raw
stream carries no rate at all, so this
is almost always a raw-mode consumer
using the wrong `-r` value — chapter
9's contract. Check the sidecar's
`audio.sample_rate` and make the
consumer agree. A WAV file that plays
at the wrong speed was most likely
*rewritten* by something that guessed.

## Speech that stops mid-sentence

Usually not Piper: a consumer that read
a partially written file, or a run that
was killed. Check four of chapter 6 —
samples × 2 + 44 against the size on
disk — separates a finished file from a
cut one. In file-per-line mode, also
check the sentence itself was not cut
by a line ending (chapter 9's verified
trap): fragments in, fragments out.

## Numbers and names read strangely

The phonemizer's rules, not the voice's
fault (chapter 2). `Dr.` became *doctor*
in the lab because espeak-ng said so.
Run with `--debug` and read the phoneme
line to see what the model was actually
handed (transcript `t08-debug-phonemes.txt`).
The fix, such as it is, lives in the
text: spell the sound you want —
"twenty twenty-four" for the year,
a respelled name — because Piper offers
no pronunciation dictionary (chapter
12).

## Two runs, two different files

Not a fault. Synthesis is sampled;
chapter 8 measured different durations
and hashes from identical commands, even
at `--noise_scale 0`. Keep the take you
like. If a build or a test demands
identical bytes, Piper is the wrong
place to look for them — archive the
WAV as the artefact.
