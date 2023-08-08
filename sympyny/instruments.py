"""This file defines the Instrument class and creates an enum of the default instruments."""

from enum import Enum


class Instrument:
    """A class that represents an instrument."""

    def __init__(self, name, sound_file_path):
        self.name = name
        self.sound_file_path = sound_file_path

    def note(
        self,
        note,
        octave,
        duration,
        volume=1,
        speed=1,
        fade_in=0,
        fade_out=0,
        vibrato=0,
        vibrato_speed=1,
        vibrato_depth=0,
        vibrato_delay=0,
    ):
        """Returns a note with the given parameters."""

    def rest(self, duration):
        """Returns a rest with the given duration."""

        return self.note(
            note="R",
            octave=0,
            duration=duration,
        )

    def chord(self, notes, duration):
        """Returns a chord with the given notes and duration."""

    def a_flat(self, octave, duration):
        """Returns an Ab note with the given octave and duration."""

        return self.note(
            note="Ab",
            octave=octave,
            duration=duration,
        )

    def a(self, octave, duration):
        """Returns an A note with the given octave and duration."""

        return self.note(
            note="A",
            octave=octave,
            duration=duration,
        )

    def a_sharp(self, octave, duration):
        """Returns an A# note with the given octave and duration."""

        return self.note(
            note="A#",
            octave=octave,
            duration=duration,
        )

    def b_flat(self, octave, duration):
        """Returns a Bb note with the given octave and duration."""

        return self.note(
            note="Bb",
            octave=octave,
            duration=duration,
        )

    def b(self, octave, duration):
        """Returns a B note with the given octave and duration."""

        return self.note(
            note="B",
            octave=octave,
            duration=duration,
        )

    def b_sharp(self, octave, duration):
        """Returns a B# note with the given octave and duration."""

        return self.note(
            note="B#",
            octave=octave,
            duration=duration,
        )

    def c_flat(self, octave, duration):
        return self.note(
            note="Cb",
            octave=octave,
            duration=duration,
        )

    def c(self, octave, duration):
        """Returns a C note with the given octave and duration."""

        return self.note(
            note="C",
            octave=octave,
            duration=duration,
        )

    def c_sharp(self, octave, duration):
        """Returns a C# note with the given octave and duration."""

        return self.note(
            note="C#",
            octave=octave,
            duration=duration,
        )

    def d_flat(self, octave, duration):
        """Returns a Db note with the given octave and duration."""

        return self.note(
            note="Db",
            octave=octave,
            duration=duration,
        )

    def d(self, octave, duration):
        """Returns a D note with the given octave and duration."""

        return self.note(
            note="D",
            octave=octave,
            duration=duration,
        )

    def d_sharp(self, octave, duration):
        """Returns a D# note with the given octave and duration."""

        return self.note(
            note="D#",
            octave=octave,
            duration=duration,
        )

    def e_flat(self, octave, duration):
        """Returns an Eb note with the given octave and duration."""

        return self.note(
            note="Eb",
            octave=octave,
            duration=duration,
        )

    def e(self, octave, duration):
        """Returns an E note with the given octave and duration."""

        return self.note(
            note="E",
            octave=octave,
            duration=duration,
        )

    def e_sharp(self, octave, duration):
        """Returns an E# note with the given octave and duration."""

        return self.note(
            note="E#",
            octave=octave,
            duration=duration,
        )

    def f_flat(self, octave, duration):
        """Returns an Fb note with the given octave and duration."""

        return self.note(
            note="Fb",
            octave=octave,
            duration=duration,
        )

    def f(self, octave, duration):
        """Returns an F note with the given octave and duration."""

        return self.note(
            note="F",
            octave=octave,
            duration=duration,
        )

    def f_sharp(self, octave, duration):
        """Returns an F# note with the given octave and duration."""

        return self.note(
            note="F#",
            octave=octave,
            duration=duration,
        )

    def g_flat(self, octave, duration):
        """Returns a Gb note with the given octave and duration."""

        return self.note(
            note="Gb",
            octave=octave,
            duration=duration,
        )

    def g(self, octave, duration):
        """Returns a G note with the given octave and duration."""

        return self.note(
            note="G",
            octave=octave,
            duration=duration,
        )

    def g_sharp(self, octave, duration):
        """Returns a G# note with the given octave and duration."""

        return self.note(
            note="G#",
            octave=octave,
            duration=duration,
        )

    def __repr__(self):
        return f"Instrument({self.name!r}, {self.sound_file_path!r})"
