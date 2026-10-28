# Your First Synthesis

**Outcome: one sentence in, one WAV file
out — and the file examined by three
independent tools, so you know it is
what it claims to be before you ever
play it.** This is the chapter the rest
of the guide stands on.

## The command

Piper reads text from standard input and
writes the file named by `--output_file`:

```bash
echo "The quick brown fox jumps over the lazy dog." \
  | ./piper/piper --model voices/en_US-lessac-medium.onnx \
      --output_file out/hello.wav
```

Piper narrates its own work on standard
error, and prints the name of the file
it wrote:

```text
[piper] [info] Loaded voice in 0.73 second(s)
[piper] [info] Initialized piper
out/hello.wav
[piper] [info] Real-time factor: 0.24 (infer=0.63 sec, audio=2.61 sec)
[piper] [info] Terminated piper
```

Read the receipt: the voice took
three-quarters of a second to load;
making the speech took 0.63 seconds; the
speech itself lasts 2.61 seconds. (Full
transcript: `piper-lab/transcripts/t01-first-synthesis.txt`.)

## The check — three tools, one story

The file is 124,064 bytes. Three tools
that owe Piper nothing describe it, and
they agree:

```bash
file out/hello.wav
```

```text
out/hello.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 22050 Hz
```

```bash
ffprobe out/hello.wav
```

```text
Duration: 00:00:02.81, bitrate: 352 kb/s
Stream #0:0: Audio: pcm_s16le, 22050 Hz, 1 channels, s16, 352 kb/s
```

```bash
soxi out/hello.wav
```

```text
Sample Rate    : 22050
Duration       : 00:00:02.81 = 62010 samples
Sample Encoding: 16-bit Signed Integer PCM
```

Every number cross-checks. The sample
rate is the sidecar's 22050 (chapter 4).
The duration is the speech's 2.61
seconds **plus 0.2** — the default
`--sentence_silence`, a pause Piper adds
after the sentence, which chapter 8
measures precisely. And 62,010 samples
at 22050 per second is 2.81 seconds,
just as the byte count says it should
be: 62,010 samples × 2 bytes = 124,020,
plus the 44-byte WAV header, is the
124,064 on disk. When a file's numbers
agree with each other like this, the
file is healthy. Chapter 6 turns that
habit into a method.

## Play it, if you can

On a machine with speakers or a media
player, `hello.wav` simply plays: a
voice, reading the pangram. The guide's
lab had no way to play anything, and
deliberately proceeds as if it never
will — but a reader with ears should
confirm at least once that the measured
file and the heard voice are the same
thing. After that, the measurements are
a trustworthy stand-in, which is the
premise of the next chapter.

One practical note: the log lines go to
standard error and the written file's
name to standard output, so in scripts
the two can be separated — the name
captured, the chatter discarded or
kept, as you prefer. Chapter 9 puts that
to work.
