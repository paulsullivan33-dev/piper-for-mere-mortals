# Voices — Finding and Choosing One

**Outcome: at least one voice downloaded
— two files, model and sidecar — and the
knowledge to read its label before you
ever hear it.** A Piper voice is a
trained network plus a small config
file. The library lives in the
`rhasspy/piper-voices` repository on
Hugging Face, and its organisation is a
filing system worth understanding,
because the path *is* the description:

```text
en/en_US/lessac/medium/en_US-lessac-medium.onnx
│   │      │       │
│   │      │       └─ quality tier
│   │      └─ the voice's name
│   └─ language and region
└─ language family
```

## The quality tiers

Each voice is trained at one or more of
four tiers. The tier decides two things
you can verify without ears — the file
size and the **sample rate**, the number
of audio samples per second, which caps
how much fine detail the sound can hold:

| Tier | Sample rate | The lab's evidence |
| --- | --- | --- |
| x_low | 16000 Hz | listed in the library; not downloaded |
| low | 16000 Hz | amy-low's sidecar, fetched and read |
| medium | 22050 Hz | lessac-medium, downloaded and run |
| high | 22050 Hz | lessac-high, downloaded and run |

Sizes from the lab's downloads
(transcript `t00-version-and-voices.txt`):

```text
en_US-lessac-medium.onnx      63 MB
en_US-lessac-high.onnx       114 MB
en_US-libritts_r-medium.onnx  79 MB
```

Whether *high* sounds better than
*medium* is a judgement for ears, and
this guide does not make it. What it can
say by measurement: high costs roughly
twice the disk and — chapter 7's real
finding — around five times the
computing time for the same paragraph.
On a small machine that trade is the
decision, and it is a decision the
numbers can make for you.

## One voice, or nine hundred

Most voices are one person. Some are
**multi-speaker**: trained on a dataset
of many readers, with each reader kept
as a numbered speaker inside the one
model. The sidecar says how many —
`num_speakers`. The lab's third voice,
**libritts_r**, is trained on the
LibriTTS audiobook dataset and carries
**904 speakers**, numbered 0 to 903,
chosen with `--speaker` (chapter 8 puts
three of them through the measuring
script). The sidecar of a big voice is
bigger too — 20 KB against lessac's
5 KB — because it carries the speaker
table.

## Reading a sidecar

Everything a reader needs to know about
a voice before running it is in the
`.onnx.json`:

```json
{
  "audio":    { "sample_rate": 22050, "quality": "medium" },
  "espeak":   { "voice": "en-us" },
  "inference": { "noise_scale": 0.667,
                 "length_scale": 1,
                 "noise_w": 0.8 },
  "phoneme_type": "espeak",
  "phoneme_id_map": { "...": "154 symbols" },
  "num_speakers": 1
}
```

- **audio.sample_rate** — the rate your
  WAV will be written at; players and
  converters need to agree with it.
- **espeak.voice** — the language
  espeak-ng will phonemize with. Text in
  another language fed to this voice
  will be pronounced as if it were
  English, because the phonemizer was
  told it is.
- **inference** — the voice's own
  preferred defaults for the shaping
  options of chapter 8.
- **phoneme_id_map** — the dictionary
  between sound symbols and model
  numbers: the largest part of the file,
  and the reason the sidecar is
  indispensable (chapter 2).

## Downloading

Each voice is two downloads — the
`.onnx` and the `.onnx.json` beside it
with the longer name. Take both, keep
the names exactly as they are, and keep
them together: Piper finds the sidecar
by adding `.json` to the model path,
unless you point `--config` elsewhere.
The library holds well over a hundred
voices across dozens of languages; this
guide verified three US-English ones
and read a fourth's sidecar, and the
rest of the shelf is documented-only
here. A voice trained for another
language works the same way — download,
point, speak — but its sidecar will name
a different espeak voice, and your text
should be in its language.
