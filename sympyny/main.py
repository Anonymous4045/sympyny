"""What the end result should be able to do (subject to change)."""

from sympyny import Song
from instruments import Instrument
from defaults import trumpet


# Instrument definition
my_instrument = Instrument("My Instrument", "/path/to/sound/file")

# Song definition

# Define song with name and other attributes
ode_to_joy = Song(
    "Ode to Joy",
    bpm=120,
    octave=5,
    composer="Anonymous4045",
    layers={
        "Melody": (
            # F4 for 1 beat
            trumpet.f(4, 1),
            # Rest for 1 beat
            trumpet.rest(1),
        )
    },
)

# Add a layer to the song
harmony = ode_to_joy.add_layer("Harmony")

# Add notes with loops
for octave in range(3, 6):
    for note in ("C", "E", "G"):
        harmony.add_note(my_instrument.note(note, octave, 1))

# Processing

# Turns the song into a sound file
ode_to_joy.save("ode_to_joy", "wav")

# Usage

# Plays the sound file saved above with the given parameters
ode_to_joy.play(volume=0.5, speed=1)

# Fun stuff I might add

# Create an image of the sheet music for each layer of the song
ode_to_joy.generate_sheet_music("Ode to Joy Sheet Music", "pdf")

# Turn the melody of the song into a piano tiles game
ode_to_joy.play_piano_tiles()

# Play the song with animations of various things, like graphs of the frequency or pitch
ode_to_joy.visualize()
