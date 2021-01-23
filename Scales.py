whole_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3
tuning_input = input("Tuning: ")
key_input = input("Key: ")
scale_input = input("Scale: ")
tuning = tuning_input.upper()
key_upper = key_input.upper()
scale_lower = scale_input.lower()
strings = {i:0 for i in tuning}
def Convert(tunings):
    list=[]
    list[:0]=tunings
    return list
tuning_list = Convert(tuning)
num_strings = len(tuning_list)
num_strings_list = []

for i in range(num_strings):
    i = i+1
    num_strings_list.append(i)


# select elements with these indexes into a list
def get_notes(key, intervals):
    # a sufficiently long sequence of notes to slice from
    whole_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3
    # finding start of slice
    root = whole_notes.index(key)
    # taking 12 consecutive elements
    octave = whole_notes[root:root+12]
    # accesing indexes specified by `intervals` to retrieve notes
    return [octave[i] for i in intervals]

# intervals of the major scale as indexes:
scales = {
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2 , 3, 5, 7, 8, 10],
    "dorian" : [0, 2, 3, 5, 7, 9, 10],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10],
    "lydian" :[0, 2, 4, 6, 7, 9, 11],
}


for i in strings.keys():
    # finding the index of first note in the string
    start = whole_notes.index(i)
    # taking a slice of 20 elements
    strings[i] = whole_notes[start:start+20]




# find position of notes of a given scale in the guitar
def find_notes(scale):
    notes_strings = {i:0 for i in "EADGB"}
    # for every string
    for key in strings.keys():
        # we create an empty list of indexes
        indexes = []
        for note in scale:
            # append index where note of the scale is found in
            ind = strings[key].index(note)
            indexes.append(ind)
            # because there are 20 frets, there are duplicate notes in the string
            if ind <= 7:
                # we must also append these to indexes
                indexes.append(ind+12)
        notes_strings[key] = indexes
    return notes_strings

# finding notes in a scale:
A_minor = get_notes('A', scales['minor'])





import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def plot(key, intervals, night=True):
    scale = get_notes(key, intervals)

    # Plot Strings
    fig, ax = plt.subplots(figsize=(20,num_strings))
    background = ['white', 'black']
    for i in range(1,num_strings+1):
        ax.plot([i for a in range(22)])

    # Plotting Frets
    for i in range(1,21):
        # decorates the twelve fret with a gray and thick fret
        if i == 12:
            ax.axvline(x=i, color='gray', linewidth=3.5)
            continue
        # trace a vertical line (a fret)
        ax.axvline(x=i, color=background[night-1], linewidth=0.5)
    ax.set_axisbelow(True)

    # setting height and width of displayed guitar
    ax.set_xlim([0, 21])
    ax.set_ylim([0.4, num_strings+.5])
    # setting color of the background using argument night
    ax.set_facecolor(background[night])
    # finding note positions of the scale in the guitar
    to_plot = find_notes(scale)

    # for every note of the scale in every string make a circle
    # with the note's name as label in the corresponding fret
    for y_val, key in zip([1,2,3,4,5,6], tuning):
        for i in to_plot[key]:
            font = 12
            x = i+0.5  # shift the circles to the right
            p = mpatches.Circle((x, y_val), 0.2)
            ax.add_patch(p)
            note = strings[key][i]
            # if note is the root make it a bit bigger
            if note == scale[0]:
                font=14.5
            # add label to middle of the circle
            ax.annotate(note, (i+0.5, y_val), color='w', weight='bold',
                            fontsize=font, ha='center', va='center')

    plt.title('Scale')
    plt.yticks(np.arange(1,num_strings+1), tuning_list)
    plt.xticks(np.arange(22)+0.5, np.arange(0,22))
    plt.show()
plot(key_upper, scales[scale_lower])
