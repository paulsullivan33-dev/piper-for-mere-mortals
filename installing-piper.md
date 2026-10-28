# Installing Piper

**Outcome: a `piper` program that runs
on your machine and can state its
version — before any voice enters the
picture.** Piper the program and the
voices it speaks with are separate
downloads, on purpose: install the
program once, then take voices off the
shelf as you need them (chapter 4).

## The release download

The lab installed Piper **1.2.0** from
the project's GitHub releases
(`github.com/rhasspy/piper`). There is
one archive per platform —
`piper_amd64.tar.gz` for ordinary 64-bit
Linux PCs, `piper_arm64.tar.gz` and
`piper_armv7.tar.gz` for Raspberry Pi
boards and their kin, and matching
builds for other systems. Watch the
names: the Linux PC file is called
`piper_amd64`, not the
`piper_linux_x86_64` you might guess —
the lab's first download was a 9-byte
file containing the words *Not Found*,
which is its own small lesson in
checking what you actually fetched.

Unpacked, the archive is self-contained:

```text
piper/
  piper                    the program
  espeak-ng-data/          the phonemizer's data
  libespeak-ng.so          the phonemizer's library
  libonnxruntime.so        the model runner
  libpiper_phonemize.so    the bridge between them
```

Nothing is installed into the system:
no package manager, no administrator
rights, and deleting the folder removes
Piper completely. The bundled libraries
are why — the program carries its own
espeak-ng and its own ONNX Runtime
rather than asking your system for them.

## The check

```bash
./piper/piper --version
```

```text
1.2.0
```

That is the whole acceptance test for
this chapter (the lab's transcript
`t00-version-and-voices.txt` keeps it).
`--help` lists every option; the ones
this guide uses are:

```text
-m  FILE  --model       FILE  path to onnx model file
-c  FILE  --config      FILE  path to model config file (default: model path + .json)
-f  FILE  --output_file FILE  path to output WAV file ('-' for stdout)
-d  DIR   --output_dir  DIR   path to output directory (default: cwd)
    --output_raw              output raw audio to stdout as it becomes available
-s  NUM   --speaker     NUM   id of speaker (default: 0)
    --noise_scale           NUM   generator noise (default: 0.667)
    --length_scale          NUM   phoneme length (default: 1.0)
    --noise_w               NUM   phoneme width noise (default: 0.8)
    --sentence_silence      NUM   seconds of silence after each sentence (default: 0.2)
    --json-input              stdin input is lines of JSON instead of plain text
    --debug                   print DEBUG messages to the console
```

Note the defaults printed here are the
*program's* defaults, and a voice's
sidecar can carry different ones of its
own — libritts_r's sidecar, for instance,
asks for quieter noise (0.333) than the
program's 0.667. When both speak, the
command line wins where you set a value,
and the sidecar fills the rest.

## The other way in

Piper also exists as a Python package
(`pip install piper-tts`, in the
successor project `OHF-Voice/piper1-gpl`)
for people building it into Python
programs, and it is packaged inside
other tools — Home Assistant most
famously. The lab verified the release
binary only; the package form is
documented-only here, and this guide's
commands are the binary's. Everything
after this chapter assumes the unpacked
`piper/` folder and a `voices/` folder
beside your work, but the program does
not care where the model file lives —
`--model` takes any path.
