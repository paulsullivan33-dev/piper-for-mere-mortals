# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's sentences are stock sentences and pangrams.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: one voice per run, WAV or raw output only, no
   pronunciation or emphasis controls, output that is never
   bit-identical twice, aborts instead of tidy errors, the
   silent success of empty input, and per-voice quality this
   guide cannot grade.
8. **The ethics rule is in the text, early.** Piper raises no
   interception question of the kind other guides in this
   series carry, but chapter 1 and the README draw its own
   line plainly — Piper speaks with its library's trained
   voices and does not clone real people — and the privacy
   property the tool exists for (your text stays on your
   machine) is stated before any procedure depends on it.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran (timings are therefore
ranges, and the guide says so). Piper **1.2.0** was installed
from the official release archive `piper_amd64.tar.gz` and run
unmodified. Three voices were downloaded in full from the
official `rhasspy/piper-voices` repository on Hugging Face —
en_US-lessac-medium (63 MB), en_US-lessac-high (114 MB) and
en_US-libritts_r-medium (79 MB, 904 speakers) — and a fourth
voice's config sidecar (en_US-amy-low) was fetched and read
without the model. All transcripts live in
`piper-lab/transcripts/`; the measuring script is
`piper-lab/check-wav.py` and the stock sentences are
`piper-lab/sentences.txt`.

The lab had **no speakers and no way to listen**. Every claim
about the audio is therefore a measurement — header facts,
durations, sample-level RMS/peak/zero counts — and the guide
never grades how a voice *sounds*. There was no speech
recognizer installed in the sandbox, so the round-trip check
(feeding a WAV to a recognizer and comparing texts) was not
done and is described in chapter 6 as an open door, not a
result.

Run for real, with transcripts as evidence:

- Version, the full `--help` option list, voice file sizes and
  the lessac-medium sidecar read field by field, including its
  154-symbol phoneme map (t00).
- First synthesis of the pangram with lessac-medium, and the
  resulting WAV described independently by `file`, `ffprobe`
  and `soxi` — sample rate, format and the byte arithmetic all
  cross-checked (t01).
- Sample-level measurement of that file with the lab's own
  script: 22050 Hz, 2.81 s, RMS −17.5 dBFS, peak −0.0 dBFS,
  9.8% zero samples; the 2.61 s of speech plus the 0.2 s
  default sentence silence accounts for the file's length, and
  9 words in 2.61 s is about 207 words per minute (t02).
- Speed: the same 30-word, four-sentence paragraph spoken
  three times each by lessac-medium (real-time factors 0.19,
  0.24, 0.27) and lessac-high (1.08, 0.96, 1.83) on the shared
  machine (t03).
- Shaping: `--length_scale` 0.75 / 1.0 / 1.5 measured at 2.38 /
  2.95 / 3.62 s per file; `--sentence_silence 1.5` producing a
  4.18 s file whose zero samples rose from about 10% to 38.2%
  (t04).
- Speakers and noise: libritts_r speakers 0, 5 and 100 measured
  at different durations and levels; the same sentence run
  twice giving different hashes and durations (2.86 vs 2.79 s),
  and two runs at `--noise_scale 0` still differing (2.89 vs
  2.88 s) (t05).
- Input modes: four lines to one combined WAV (25.87 s);
  four lines to `--output_dir` giving four auto-named
  timestamp files; `--json-input` honouring a per-line
  `output_file`; `--output_raw` producing 102,516 headerless
  bytes that sox, told the format, rebuilt into a WAV of
  exactly the implied 2.32 s (t06).
- Failures: a missing model and a model with its sidecar
  removed both aborting with exit 134 and exact messages;
  empty input exiting 0 and writing no file; `--speaker 5` on
  a one-speaker voice silently accepted; `--speaker 904` on
  libritts_r crashing inside ONNX Runtime with the bounds
  message quoted in chapter 13 (t07).
- The phonemizer exposed with `--debug`: the phoneme strings
  and id streams for a sentence, and `Dr.` demonstrably
  expanded to the phonemes of *doctor* before the model ran
  (t08).
- Line handling: a sentence split across two lines spoken
  whole into a single output file (debug shows the rejoined
  sentence), but split into two fragment files under
  `--output_dir` (t09).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Voices beyond the three downloaded (and amy-low's sidecar):
  the rest of the library's languages and tiers, including the
  x_low tier's listings.
- The Python package form (`pip install piper-tts`,
  OHF-Voice/piper1-gpl) and Piper embedded in other programs,
  including Home Assistant's Wyoming pipeline.
- The neighbour tools of chapter 11 (espeak-ng standalone,
  Festival/Flite, the cloud services, Coqui) — characterised,
  not run or benchmarked.
- Actually *hearing* any of it: relative voice quality, whether
  high sounds better than medium, choosing among libritts_r's
  904 speakers by ear, and the sox play line in chapter 10,
  which is assembled from verified parts (the raw stream and
  sox's conversion of it were both run) but was not heard.
- Training or fine-tuning a voice, and playback on a machine
  with a sound device.

Fixtures are this guide's own and deliberately generic: a
pangram, three stock sentences about text to speech itself,
and one weather sentence — no names, organisations or real
events. Nothing was recorded or cloned; every voice is a
library artefact trained by its own project.
