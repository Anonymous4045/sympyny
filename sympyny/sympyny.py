"""This file defines the Song class and its methods."""


class Song:
    """Class that represents a song."""

    def __init__(self, name, composer, bpm=120, octave=5, layers=None):
        self.name = name
        self.composer = composer
        self.bpm = bpm
        self.octave = octave

        # If the layer is a dict, convert it to a list of Layer objects
        if isinstance(layers, dict):
            layers = [Layer(name, notes) for name, notes in layers.items()]

        self.layers = layers or []

    def add_layer(self, name):
        """Adds a layer to the song."""
        self.layers.append(Layer(name))

        return self.layers[-1]

    def save(self, file_name, file_type):
        pass


class Layer:
    """Class that represents a layer of a song."""

    def __init__(self, name, notes=None):
        self.name = name
        self.notes = notes or []

    def add_note(self, note):
        """Adds a note to the layer."""
        self.notes.append(note)

        return note

    def add_notes(self, notes):
        """Adds notes to the layer."""
        self.notes.extend(notes)

        return notes
