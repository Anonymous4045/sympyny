from pathlib import Path

from playsound import playsound


PATHS = {
    "root": Path(__file__).parent.parent,
    "sounds": Path(__file__).parent.parent / "sounds",
    "brass": Path(__file__).parent.parent / "sounds" / "brass"
}


class Instrument:
    def __init__(self, path: Path):
        self._path = path

    def play(self):
        playsound(self._path)
