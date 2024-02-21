from scamp import *
import random


def build_chord(interval_options,
                num_notes,
                pitch_center,
                round_transposition=False):
    chord = [0]
    while len(chord) < num_notes:
        chord.append(chord[-1] + interval_options[0])
        chord.append(chord[-1] + interval_options[1])
        chord.append(chord[-1] + interval_options[2])

    transposition = pitch_center - sum(chord) / len(chord)
    if round_transposition:
        transposition = round(transposition)
    return [p + transposition for p in chord]


s = Session()

guitar = s.new_part("guitar")
recorder = s.new_part("recorder")
piano = s.new_part("piano")

while True:
    piano.play_chord(
        build_chord([4, 3, 4], 4, 65.5),  # 66 -> C
        1,
        0.4,
        # "staccato" if random.random() < 0.5 else None
    )
    piano.play_chord(
        build_chord([4, 3, 4], 4, 71),  # 71 -> F-ish
        1,
        0.4,
        # "staccato" if random.random() < 0.5 else None
    )
    piano.play_chord(
        build_chord([3, 4, 3], 4, 74),  # 74 -> A-ish
        1,
        0.4,
        # "staccato" if random.random() < 0.5 else None
    )
    # recorder.play_chord(
    #     build_chord(3, 4, 63),
    #     1,
    #     0.5,
    #     # "staccato" if random.random() < 0.5 else None
    # )
    # piano.play_chord(
    #     build_chord(3, 4, 61),
    #     1,
    #     0.3,
    #     # "staccato" if random.random() < 0.5 else None
    # )
