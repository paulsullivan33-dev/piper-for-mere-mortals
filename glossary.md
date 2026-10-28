# Glossary

**Config sidecar** — the `.onnx.json`
file that travels with every voice
model. It declares the sample rate,
the espeak voice, the default shaping
values and the phoneme map. Required:
without it Piper will not start.

**dBFS** — decibels below full scale: a
loudness measure for digital audio,
where 0 is the loudest sample a file
can hold and real speech in this guide
measures around −20 to −14 RMS.

**espeak-ng** — the open-source formant
synthesizer whose front half lives
inside Piper: it turns written text
into phonemes (and expands numbers and
abbreviations) for the neural model.

**Length scale** — Piper's speaking-rate
option. Below 1 stretches less and
speaks faster; above 1 slows down.

**Multi-speaker voice** — a model
trained on many readers, each kept as a
numbered speaker chosen with
`--speaker`. libritts_r has 904.

**Noise scale / noise width** — the
options governing how much chance is in
a performance: variation in the sounds,
and in how long each sound lasts.

**ONNX** — a portable file format for
trained neural networks. A Piper voice's
`.onnx` file is the network itself.

**ONNX Runtime** — the library that runs
ONNX models; bundled in Piper's release
download.

**Phoneme** — one distinct sound of a
language, written as a symbol in a
phonetic alphabet. Models read phonemes,
not letters.

**Phonemizer** — the stage that converts
text into phonemes. In Piper, that is
espeak-ng.

**Real-time factor** — seconds of
computing divided by seconds of audio
produced. Below 1 is faster than
playback; Piper prints it after every
run.

**RMS level** — root mean square: the
average loudness of a sound file,
computed from all its samples. The
chapter 6 script's main witness that a
file is not silent.

**Sample rate** — audio samples per
second. Piper voices write 22050 Hz
(medium and high tiers) or 16000 Hz
(low tiers); the rate belongs to the
voice, not to a setting.

**Sentence silence** — the pause, in
seconds, Piper leaves after each
sentence; 0.2 by default.

**Text to speech (TTS)** — turning
written text into spoken audio. The
reverse journey is speech to text.

**VITS** — the neural network
architecture behind Piper's voices: it
learns to go from phonemes to a
performance, variation included.

**Voice** — in Piper, one downloadable
model (plus its sidecar): one persona,
one language, one quality tier — or, in
a multi-speaker model, one numbered
crowd of them.

**WAV** — the uncompressed audio file
format Piper writes: a 44-byte header
and 16-bit samples, understood by
practically everything.
