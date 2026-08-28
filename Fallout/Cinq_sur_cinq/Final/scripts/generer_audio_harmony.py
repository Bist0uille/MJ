from array import array
from pathlib import Path
import math
import random
import wave


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audio"
RATE = 44100


def piano_note(freq, duration=3.0, strength=1.0):
    total = int(duration * RATE)
    samples = [0.0] * total
    detunes = (-0.0017, 0.0, 0.0013)
    for i in range(total):
        t = i / RATE
        attack = min(1.0, t / 0.006)
        body = 0.0
        for harmonic in range(1, 9):
            harmonic_freq = freq * harmonic * (1.0 + 0.00022 * harmonic * harmonic)
            harmonic_amp = 1.0 / (harmonic ** 1.45)
            harmonic_decay = math.exp(-t * (0.72 + 0.20 * harmonic))
            strings = sum(
                math.sin(2.0 * math.pi * harmonic_freq * (1.0 + detune) * t)
                for detune in detunes
            ) / len(detunes)
            body += harmonic_amp * harmonic_decay * strings
        hammer = random.uniform(-1.0, 1.0) * math.exp(-t * 70.0) * 0.05
        samples[i] = strength * attack * (body * 0.34 + hammer)
    return samples


def mix_sequence(notes, spacing=0.82, tail=3.2, final_boost=1.0):
    length = int(((len(notes) - 1) * spacing + tail) * RATE)
    result = [0.0] * length
    for index, freq in enumerate(notes):
        note = piano_note(freq, tail, final_boost if index == len(notes) - 1 else 1.0)
        start = int(index * spacing * RATE)
        for offset, value in enumerate(note):
            if start + offset < length:
                result[start + offset] += value
    return add_room(result)


def add_room(samples):
    result = list(samples)
    for delay_seconds, gain in ((0.095, 0.16), (0.211, 0.10), (0.367, 0.06)):
        delay = int(delay_seconds * RATE)
        for i in range(delay, len(result)):
            result[i] += samples[i - delay] * gain
    return result


def silence(duration):
    return [0.0] * int(duration * RATE)


def repeated_motif(notes, repetitions=4):
    result = []
    for index in range(repetitions):
        motif = mix_sequence(notes)
        result.extend(motif)
        if index < repetitions - 1:
            result.extend(silence(2.4))
    return result


def write_wav(filename, samples):
    peak = max(max(abs(value) for value in samples), 0.001)
    scale = 0.86 * 32767 / peak
    pcm = array("h", (int(max(-32767, min(32767, value * scale))) for value in samples))
    with wave.open(str(OUT / filename), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(pcm.tobytes())


def main():
    random.seed(505)
    OUT.mkdir(parents=True, exist_ok=True)
    # D4, F4, A4, F#4: une phrase presque familière qui reste en suspens.
    four_notes = [293.66, 349.23, 440.00, 369.99]
    # D5 ferme la signature et autorise HARMONY à prendre les robots.
    five_notes = four_notes + [587.33]
    write_wav("01_HARMONY_QUATRE_NOTES.wav", mix_sequence(four_notes))
    write_wav("02_HARMONY_CINQ_NOTES_CONTROLE.wav", mix_sequence(five_notes, final_boost=1.18))
    write_wav("03_CINQUIEME_NOTE_SEULE.wav", mix_sequence([587.33], final_boost=1.18))
    write_wav("04_HARMONY_QUATRE_NOTES_BOUCLE.wav", repeated_motif(four_notes))
    print(f"Fichiers HARMONY créés dans {OUT}")


if __name__ == "__main__":
    main()
