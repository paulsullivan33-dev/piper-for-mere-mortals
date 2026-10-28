# Paragraphs, Lines and JSON Input

**Outcome: the three ways to feed Piper
text, control over whether you get one
file or many, and the headerless raw
stream for piping into other tools.**
Everything here is verified in the lab's
transcript `t06-input-modes.txt`, using
the lab's four stock lines,
`piper-lab/sentences.txt`.

## First, how text is divided

**Sentences are the units of speech.**
Piper splits text into sentences — on
the full stops and their kin — speaks
them in order, and leaves
`--sentence_silence` (default 0.2 s)
after each. The four-sentence paragraph
of chapter 7 was *one line*; its pauses
are sentence pauses, and there is no
paragraph pause distinct from them.

**Lines matter differently in different
modes** — a distinction the lab verified
the hard way, with one sentence cut in
half by a line ending (transcript
`t09-split-lines.txt`). Writing a single
file (mode one), Piper treats the whole
input as one text: lines are joined, and
a sentence split across two lines is
phonemized and spoken whole — the debug
log shows the rejoined sentence. In
file-per-line mode (mode two), each line
is its own unit of work, and the same
split sentence became two fragments in
two files — 1.22 s of "The quick brown",
then 2.10 s of the rest. Wrapped text is
safe in mode one and a trap in mode two.

## Mode one: one file, everything in it

Give `--output_file` and every line you
feed goes into that one file, in order:

```bash
./piper/piper --model voices/en_US-lessac-medium.onnx \
    --output_file out/combined.wav \
    < piper-lab/sentences.txt
```

The lab's four lines — 77 words, eleven
sentences — became a single WAV of
25.87 seconds, measured and healthy.
This is the narration mode: whole
chapters in, one audio file out.

## Mode two: a file per line

Omit `--output_file` and give
`--output_dir`, and each line gets its
own file:

```bash
./piper/piper --model voices/en_US-lessac-medium.onnx \
    --output_dir out/lines \
    < piper-lab/sentences.txt
```

```text
out/lines/1793213043970925994.wav
out/lines/1793213044611410707.wav
out/lines/1793213045583346373.wav
out/lines/1793213047520028000.wav
```

Four lines, four files — and look at the
names. They are numbers (a timestamp
count), guaranteed unique and guaranteed
meaningless: nothing in them says which
line a file speaks. This mode is for
programs, not people — a caller that
asked for the files can keep its own
ledger. A person who wants named clips
should use mode three.

## Mode three: JSON input, named outputs

With `--json-input`, each input line is
a small JSON object, and the object can
name its own output:

```bash
echo '{"text": "A short line spoken by name.", "output_file": "out/by-name.wav"}' \
  | ./piper/piper --model voices/en_US-lessac-medium.onnx --json-input
```

```text
out/by-name.wav
```

The object takes `text`, `output_file`,
and per-line overrides such as
`speaker` — this is the interface a
program driving Piper should use: one
long-lived run, requests in, named files
out, no guessing. It also makes the
two-voice trick of chapter 10 (recipes)
easy: alternate the speaker per line and
each line still lands in its own file.

## The raw stream

`--output_raw` sends neither WAV nor
file: it writes the model's samples to
standard output *as they are made*,
with no header — 16-bit signed samples,
mono, at the voice's rate:

```bash
echo "Raw output has no header at all." \
  | ./piper/piper --model voices/en_US-lessac-medium.onnx \
      --output_raw > out/raw.bin
```

```text
out/raw.bin: data
```

`file` sees only "data" — 102,516 bytes
of it, which is 51,258 samples, which is
2.32 seconds at 22050 Hz. The lab proved
the format by rebuilding a WAV with sox,
telling sox the numbers Piper would
have put in a header:

```bash
sox -t raw -r 22050 -e signed -b 16 -c 1 out/raw.bin out/raw-as-wav.wav
```

The rebuilt file measured exactly those
2.32 seconds at healthy levels. Raw mode
is the streaming shape: a player or a
network tool can start with the first
samples while the rest are still being
made — but the contract is strict. The
rate lives in the voice's sidecar, not
in the stream; get it wrong and the
voice plays at the wrong speed, and
nothing anywhere will warn you.
