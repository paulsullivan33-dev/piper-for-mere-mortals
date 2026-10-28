# The Moving Parts

Piper looks like one program, and at the
command line it is one program. Inside,
four parts do four different jobs, and
nearly every surprise in this guide —
including most of the troubleshooting
chapter — is one of these parts behaving
exactly as designed while the reader
expected another part's behaviour. This
chapter names them.

## The program itself

The `piper` binary is the conductor. It
reads text from standard input, splits
it into sentences, asks the phonemizer
to prepare each sentence, asks the model
to sing it, and
writes the result as a WAV file (or as a
raw stream of samples — chapter 9). It
holds the options: which model, which
speaker, how fast, how long a pause after
each sentence. It also prints the log
lines — *Loaded voice*, the real-time
factor — that this guide uses as receipts.

## The phonemizer: text into sounds

A speech model does not read letters. It
reads **phonemes**: the distinct sounds
of a language, written in a phonetic
alphabet. Between your text and the model
sits **espeak-ng**, a venerable
open-source speech synthesizer in its own
right, used here only for its front half:
it turns written words into phoneme
strings. This stage is where numbers,
abbreviations and symbols are expanded —
feed Piper `Dr. Lee paid 5 dollars` and
espeak-ng's output begins with the
phonemes for *doctor*, as the lab's
debug transcript shows:

```text
[piper] [debug] Converting 8 phoneme(s) to ids: dˈɑːktɚ.
```

That is the whole word *doctor*,
compressed into eight sound symbols. The
debug flag (`--debug`) shows this stage
working, sentence by sentence:

```text
[piper] [debug] Phonemizing text: Piper reads text out loud.
[piper] [debug] Converting 32 phoneme(s) to ids: pˈaɪpɚ ɹˈiːdz tˈɛkst ˈaʊt lˈaʊd.
```

(From the lab's transcript
`piper-lab/transcripts/t08-debug-phonemes.txt`.)

The release download carries its own
copy of espeak-ng's data files
(`espeak-ng-data/`) and its library, so
this part needs nothing installed.

## The voice: a model plus its sidecar

The voice itself is a **VITS** neural
network — the architecture behind most
modern small text-to-speech systems —
stored as an **ONNX** file: a portable
format for trained models, run here by
the ONNX Runtime library bundled in the
download. Each voice is *two* files, and
both are required:

- `en_US-lessac-medium.onnx` — the
  network itself: 63 MB of trained
  weights.
- `en_US-lessac-medium.onnx.json` — the
  **config sidecar**: a small text file
  that says what the numbers in the model
  mean.

The sidecar is not decoration. It
carries the sample rate the audio must
be written at (22050 Hz for this voice),
the espeak voice to phonemize with
(`en-us`), the default values for the
noise and length options, and the
**phoneme map** — the table that turns
each phoneme symbol into the number the
model expects (154 symbols for lessac).
Take the sidecar away and Piper refuses
to start, with a crash that names the
problem exactly:

```text
terminate called after throwing an instance of 'std::runtime_error'
  what():  Model config doesn't exist
```

(Verified in the lab; transcript
`t07-failures.txt`.) Chapter 4 takes the
sidecar apart field by field.

## The WAV writer

The model's output is a stream of
numbers — audio samples. Piper wraps
them in the WAV format: 16-bit samples,
one channel (mono), at the sample rate
the sidecar declares. That rate is a
property of the *voice*, not a setting
you choose: medium and high voices in
the library record at 22050 Hz, low-tier
voices at 16000 Hz. Play a Piper file
with the wrong rate assumed and it will
sound like the wrong-sized person —
which is why chapter 6 checks the header
before anything else, and why the raw
output mode (chapter 9) makes you state
the rate yourself when you rebuild a
file from it.

## Which part holds what

| Question | The part that answers it |
| --- | --- |
| Why did it read "Dr." as "doctor"? | The phonemizer (espeak-ng) |
| Why is this file 22050 Hz? | The voice's config sidecar |
| Why did it stop between sentences? | The program (`--sentence_silence`) |
| Why does this voice sound different from that one? | The model file — the trained network |
| Why did it crash before speaking? | Usually the program, failing to find the model or its sidecar |
| Why is the same sentence a different length twice? | The model — it samples its performance anew each run (chapter 8) |

Keep this table in mind. When Piper
surprises you, the surprise has an
address, and the address is one of these
four.
