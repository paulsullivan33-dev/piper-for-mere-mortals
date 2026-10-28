# What Piper Is

You have text — a paragraph, a reminder,
a chapter of a book — and you want it
*spoken*: sound you can play, save, or
hand to another program. The familiar way
to get that is a cloud service: the text
travels to a company's servers, a large
model reads it, and audio travels back.
It works well. It also means your text —
a medical letter, a private note, an
unpublished draft — took a trip.

**Piper is text to speech with the trip
removed.** It is a program that runs
entirely on your own computer. You give
it text on its standard input; it writes
a **WAV file**: uncompressed spoken
audio, the most ordinary sound file
there is. The voice it speaks with is a
**neural network** — a trained model,
downloaded once as a file, kept on your
disk, and loaded each time the program
runs. After that one download, Piper
needs no network at all. The lab that
wrote this guide ran it on a machine
where the text, the voice and the audio
never left the disk they started on.

This is worth pausing on, because it is
the reason the tool exists. Piper began
in the world of home automation — the
Rhasspy voice-assistant project — where
people wanted a house that answers
without phoning home. It is now the
built-in voice of Home Assistant's local
voice pipeline, and it runs happily on
small machines, including a Raspberry Pi.
"Fast and local" is not a slogan here; it
is the design. Chapter 7 measures the
fast part: on the lab's small shared
machine, a medium-quality voice produced
speech four to five times faster than
the speech itself plays.

## A first taste

After installing (chapter 3) and
downloading a voice (chapter 4), speaking
is one line:

```bash
echo "The quick brown fox jumps over the lazy dog." \
  | ./piper --model en_US-lessac-medium.onnx \
      --output_file hello.wav
```

The text goes in on standard input; the
file `hello.wav` comes out. Piper prints
its receipt as it works, including the
number this guide will keep coming back
to — how long the audio is, and how long
it took to make:

```text
[piper] [info] Real-time factor: 0.24 (infer=0.63 sec, audio=2.61 sec)
```

A **real-time factor** under 1 means
faster than real time: 0.63 seconds of
computing bought 2.61 seconds of speech.
Chapter 7 is about that number.

## What it is not

Piper is not a voice *cloner*: it speaks
with the voices in its library — trained
from recordings made by volunteers and
from public datasets — and it cannot
imitate a person it has never heard.
It is not a screen reader or a telephone
system: its natural output is a file,
made as fast as the machine allows, not
a live conversation (chapter 9 shows the
one streaming-shaped output it has, and
chapter 12 is plain about the rest).
It is not a general audio tool: it makes
WAV files and raw samples, and turning
those into MP3s or videos is another
tool's job — the ffmpeg guide in this
series is the natural next step. And it
is not a listener: speech *recognition* —
sound in, text out — is the opposite
journey, and it belongs to Whisper and
its kin (chapter 11).

## Who it is for

The home-automation builder who wants
spoken announcements that stay in the
house. The maker who wants a gadget to
talk without a cloud account. The writer
who proofreads by ear and would rather
their draft stayed on their own disk.
The accessibility tinkerer building
something that reads text aloud on cheap
hardware. The common thread is one
person, their own machine, and text they
would like spoken — privately, quickly,
and for free after the download.

## The honest catch, up front

A cloud voice is usually the polished
product of an enormous training run.
Piper's voices are good — genuinely,
surprisingly good for files this small —
but the library is a shelf of individual
efforts, quality varies by voice, and
each voice speaks one language, in one
persona, at one level of polish. Chapter
4 lays out the quality tiers and what
they cost. And there is a second catch
this guide treats as a feature of the
telling rather than a footnote: the lab
could not listen to its own output, so
everything here is *measured*, not
*reviewed*. Where a claim would need
ears, the guide says so.
