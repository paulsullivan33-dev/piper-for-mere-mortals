# The Neighbours

Piper sits in a crowded field — programs
that speak, and one famous program that
does the opposite. These are
characterisations from the projects' own
documentation, not benchmarks; the lab
ran Piper only.

## espeak-ng: the ancestor in the room

Piper already contains espeak-ng, used
as a phonemizer (chapter 2). On its own,
espeak-ng is a complete synthesizer —
formant synthesis, the classic robot
voice, tiny beyond belief, speaking over
a hundred languages with intelligibility
as its design goal and naturalness
nowhere on the list. If you need a
machine to *be understood* on hardware
from another decade, espeak-ng alone is
the answer. Piper is what happened when
the same front end was given a neural
network to sing through instead: natural
voices, at the price of a model file per
voice and far more computing.

## Festival and Flite: the old school

Festival, from the University of
Edinburgh, is the veteran academic
speech synthesizer — a large, scriptable
system with its own scheme-based
configuration, concatenative voices
built from recorded fragments, and
decades of research inside. Flite is its
small embedded sibling. They taught the
field much of what it knows, and on a
modern desk Piper's neural voices are
the easier path to a natural sound; but
Festival's depth of control — over
pronunciation, prosody, timing — is
something Piper simply does not offer
(chapter 12).

## The cloud voices

Amazon Polly, Google Cloud Text-to-
Speech, Azure Speech, OpenAI's audio
models and their kin sell the other end
of the trade: the largest, most polished
voices, in many languages and styles,
with controls for emphasis and speaking
style, billed by the character, on their
computers. For a product shipping to the
public, that polish may be worth the
price. The costs are the ones chapter 1
named — your text travels, the meter
runs, the service must be up, and the
voice can be retired by a decision in
another company. Piper's bet is the
opposite on every axis, and this guide
exists because for a reader's own
machine and own text, the opposite bet
often wins.

## Coqui, and the research frontier

Coqui's XTTS and the wider open research
world chase what Piper deliberately does
not: voice cloning from seconds of
sample audio, many languages in one
multilingual model, expressive styles.
They are heavier — GPU-shaped appetites,
larger downloads, licences that need
reading — and they move fast. A reader
who outgrows Piper's shelf of fixed
voices will likely land there; a reader
who wants a file spoken *tonight*, on a
small machine, offline, will not regret
starting here.

## Whisper: the mirror

Whisper (which has its own guide in
this series) runs the road backwards —
audio in, text out. The two meet
naturally: Piper makes speech you can
test a recognizer against, and a
recognizer can check Piper's output the
way chapter 6 wished for, by reading it
back and comparing with the input.
Piper's own project grew up in the same
open voice-assistant world (Rhasspy,
Home Assistant's Wyoming protocol),
which is why it composes so readily:
text in and out of small programs, files
and streams between them.
