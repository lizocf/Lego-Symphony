from scamp import *
import random


def build_chord(interval_options, num_notes, pitch_center, round_transposition=False):
    chord = [0]
    while len(chord) < num_notes:
        chord.append(chord[-1] + interval_options[0])
        chord.append(chord[-1] + interval_options[1])
        chord.append(chord[-1] + interval_options[2])

    transposition = pitch_center - sum(chord) / len(chord)
    return [p + transposition for p in chord]


s = Session()

guitar = s.new_part("guitar")
recorder = s.new_part("recorder")
piano = s.new_part("piano")

def play():
    piano.play_note(60,0.8,1)
    # piano.play_chord(
    #         build_chord([4, 3, 4], 4, 65.5),  # 66 -> C
    #         0.8,
    #         1,
    #         # "staccato" if random.random() < 0.5 else None
    #     )
    # piano.play_chord(
    #         build_chord([4, 3, 4], 4, 71),  # 71 -> F-ish
    #         1,
    #         1,
    #         # "staccato" if random.random() < 0.5 else None
    #     )
    # piano.play_chord(
    #         build_chord([3, 4, 3], 4, 74),  # 74 -> A-ish
    #         1,
    #         1,
    #         # "staccato" if random.random() < 0.5 else None
    #     )


def play2():
    piano.play_note(48,0.8,1)

while True:
    s.fork(play)
    s.fork(play2)
    s.wait_for_children_to_finish()
