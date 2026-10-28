#!/usr/bin/env python3
"""check-wav.py -- prove a WAV file really contains speech-shaped audio.

The lab cannot listen to the files Piper makes, so it measures them
instead. For each file named on the command line this prints:

  - the header facts (sample rate, channels, bits per sample)
  - the duration in seconds
  - the RMS (average) level and the peak level, in dBFS
    (decibels below full scale; silence would be -infinity)
  - the percentage of samples that are exactly zero

Usage: python3 check-wav.py one.wav [two.wav ...]
"""

import math
import sys
import wave
from array import array


def check(path):
    with wave.open(path, "rb") as w:
        rate = w.getframerate()
        channels = w.getnchannels()
        width = w.getsampwidth()
        frames = w.getnframes()
        raw = w.readframes(frames)

    samples = array("h")  # Piper writes 16-bit samples
    samples.frombytes(raw)
    if channels > 1:  # keep the first channel only
        samples = samples[::channels]

    count = len(samples)
    duration = count / rate
    if count == 0:
        print(f"{path}: EMPTY (0 samples)")
        return

    peak = max(max(samples), -min(samples))
    rms = math.sqrt(sum(s * s for s in samples) / count)
    zeros = sum(1 for s in samples if s == 0)

    def db(value):
        return "-inf" if value == 0 else f"{20 * math.log10(value / 32768):.1f}"

    print(f"{path}")
    print(f"  sample rate {rate} Hz, {channels} channel(s), {width * 8}-bit")
    print(f"  {count} samples, {duration:.2f} seconds")
    print(f"  RMS level {db(rms)} dBFS, peak {db(peak)} dBFS")
    print(f"  zero samples: {100.0 * zeros / count:.1f}%")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        check(path)
