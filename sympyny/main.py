from instruments import PATHS, Instrument

file = PATHS["brass"] / "trumpet.wav"
trumpet = Instrument(file)

trumpet.play()
