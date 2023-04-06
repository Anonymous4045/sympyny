"""What the end result should be able to do (subject to change)."""

from sympyny import Song
from sympyny.instruments import trumpet


# Song definition

# Define song with name and other necessary stuff
ode_to_joy = Song("Ode to Joy", bpm=120, octive=5, composer="Anonymous4045")

# Add a musical layer comprised of one instrument. Can be as many layers as needed.
ode_to_joy.add_layer("Melody", trumpet, (("C5", 1 / 2), ("F5", 1 / 4), ("Rest", 1)))


# Processing

# Runs through all the processing to add the sounds defined in the layers above into the given format
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
