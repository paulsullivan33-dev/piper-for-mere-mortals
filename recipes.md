# Recipes

Short jobs, each built only from pieces
the earlier chapters verified. Unless a
recipe says otherwise, the measurements
quoted are the lab's.

## Read a text file into one narration file

Chapter 9's mode one, aimed at a real
file:

```bash
./piper/piper --model voices/en_US-lessac-medium.onnx \
    --output_file chapter-01.wav < chapter-01.txt
```

One comfort earned by the lab (chapter
9, transcript `t09-split-lines.txt`):
in this single-file mode Piper joins
the input lines before splitting it
into sentences, so hard-wrapped text —
wrapped at 70 columns by an editor —
still speaks in whole sentences. (The
file-per-line mode does *not* join
lines; keep wrapped text away from
that one.) Check the result with the
chapter 6 method: words ÷ seconds
between 2 and 4, RMS near −17 dBFS.

## A folder of named clips from a list

For announcements, prompts and other
short lines, drive Piper once with JSON
input (chapter 9, mode three) so the
voice loads once and every clip is
named:

```bash
{ echo '{"text": "Dinner is ready.", "output_file": "clips/dinner.wav"}'
  echo '{"text": "The front door is open.", "output_file": "clips/door.wav"}'
} | ./piper/piper --model voices/en_US-lessac-medium.onnx --json-input
```

Loading once matters: chapter 7 measured
about 0.7 s to load the voice, every
time the program starts.

## A two-voice conversation

Two speakers from one multi-speaker
voice, alternating lines, each into the
same combined file — or, cleaner, into
per-line files with JSON input and a
per-line `speaker`:

```bash
{ echo '{"text": "Have you watered the garden?", "speaker": 0,   "output_file": "talk/a.wav"}'
  echo '{"text": "Twice this week already.",     "speaker": 100, "output_file": "talk/b.wav"}'
} | ./piper/piper --model voices/en_US-libritts_r-medium.onnx --json-input
```

Joining the clips in order is a job for
sox or ffmpeg (`ffmpeg` has a guide in
this series). Chapter 8's caveat
applies: the library gives the 904
speakers numbers, not names — audition
a few and keep a note of the pair you
chose; the measurements can tell them
apart but cannot pick for you.

## Slower speech for careful listening

Language practice, instructions for
someone who needs them unhurried, a
proofread at dictation speed:

```bash
echo "Turn left at the second gate." \
  | ./piper/piper --model voices/en_US-lessac-medium.onnx \
      --length_scale 1.25 --sentence_silence 0.6 \
      --output_file directions.wav
```

Chapter 8's table is the calibration:
1.5 measured about 1.23× the natural
file duration, pauses included.

## Check a whole folder of output

Chapter 6's script takes many files at
once, which makes it a batch audit:

```bash
python3 piper-lab/check-wav.py clips/*.wav
```

Read the column of durations and RMS
levels as a table: the file that sits
far from its siblings — twice the zeros,
half the level, a duration its word
count cannot explain — is the file to
listen to first. This is also the guard
against chapter 12's emptiest trap: a
run fed an empty line *succeeds* and
writes nothing, so count the files, not
the exit codes.

## Speak into a pipe, not a file

For anything that wants the sound now —
a player, a stream, another machine —
use `--output_raw` (chapter 9) and let
the receiving tool own the format. On
the lab's machine, sox can play the
stream's shape directly:

```bash
echo "The kettle has boiled." \
  | ./piper/piper --model voices/en_US-lessac-medium.onnx --output_raw \
  | sox -t raw -r 22050 -e signed -b 16 -c 1 - -d
```

(The lab had no sound device, so this
exact line is assembled from verified
parts — the raw stream measured in
chapter 9, sox's conversion of it run
for real — rather than heard. The rate,
22050, is the lessac sidecar's; a
16000 Hz voice needs its own number
there.)
