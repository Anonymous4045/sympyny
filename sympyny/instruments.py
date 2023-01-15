from pathlib import Path

from audio_io import play_sound


class Instrument:
    def __init__(self, path: Path):
        self._path = path

    def play(self, thread=False) -> None:
        play_sound(self._path, thread)
