# Limits

What Piper cannot do, stated plainly.
Most of these the lab met directly; the
rest are labelled as documentation.

**One voice per run, one run per voice.**
A run loads exactly one model. Two
voices means two runs, or one
multi-speaker model with `--speaker`
(chapter 8). The voice costs about 0.7 s
to load on the lab's machine, every
time — shape scripts accordingly.

**WAV or raw, nothing else.** Output is
a 16-bit mono WAV in the voice's native
rate, or headerless samples. No MP3, no
OGG, no stereo, no resampling. Anything
else is a converter's job (sox and
ffmpeg both do it in one command).

**No direction.** There is no markup —
no SSML, no emphasis, no "say this word
carefully", no pronunciation dictionary
you can edit. What espeak-ng makes of
your text is what the voice sings:
abbreviations and numbers are expanded
by espeak's rules (chapter 2), and a
word it gets wrong will be wrong every
run, at scale, until the text itself is
changed to spell the sound you want.

**Never the same performance twice.**
Synthesis samples its own output; two
runs of the same sentence differ in
length and bytes even with the noise
turned to zero (chapter 8). Anything
that needs bit-identical audio —
checksum-matched builds, exact-duration
slots — must keep the file it likes and
treat regeneration as a new take, not a
reprint.

**It fails like a C++ program, because
it is one.** A missing model, a missing
sidecar, a speaker past the end of the
list: each aborts the process with a
thrown exception and exit code 134, not
a tidy error message and exit 1. Scripts
must check louder than usual — and must
check for the *file*, because of the
worst behaviour in this chapter:

**Empty input succeeds, silently.**
Feed Piper no text and it exits 0 and
writes nothing (transcript
`t07-failures.txt`). Any pipeline that
trusts exit codes will ship silence
downstream and call it success. Count
outputs; measure them (chapter 6).

**Fixed voices, in every sense.** A
voice speaks its one language, as its
one persona (or its numbered crowd),
with the polish its training gave it.
There is no style control, no emotion
dial, no reading-level adjustment. The
library's coverage is uneven — rich for
English and several European languages,
thin or absent elsewhere — and a voice
for your language may simply not exist
yet. And a voice is a dataset's
artefact: libritts_r's 904 speakers are
unnamed numbers, chosen by listening,
not a cast list you can browse.

**Not a conversation.** Piper's raw mode
streams samples as they are made, and
chapter 7 shows medium voices
synthesizing several times faster than
playback — but Piper itself has no
notion of playback, interruption, or
listening back. Real-time dialogue is
assembled from it by other programs
(Home Assistant's pipeline is the famous
example), not provided by it.

**Quality is per-voice, and this guide
cannot grade it.** A neural voice can
mispronounce, slur a rare word, or put
the stress on the wrong syllable, and
measurements will call the file perfect
— as chapter 6 confessed, the lab's
method proves the audio is real, never
that the reading is right.
