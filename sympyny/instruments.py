from pathlib import Path
from tempfile import NamedTemporaryFile

import librosa.effects

import audio_io


class Instrument:
    def __init__(self, path: Path):
        self._path = Path(path)

        # Extract sound data from the given file
        self._y, self._sr = librosa.load(path)

        with path.open("rb") as file:
            data = file.read()
        self._raw_data = data

    def play(self, freq=440) -> None:
        """Play the instrument at a given frequency"""

        sound = NamedTemporaryFile()

        sound.write(self._raw_data)
        sound.seek(0)

        y = self._shift_pitch(sound.name, freq)
        audio_io.write_sound(sound, y, self._sr)

        audio_io.play_sound(sound.name)

    def _shift_pitch(self, pitch):
        """Change the pitch of the sound"""

        change = pitch - 440
        return librosa.effects.pitch_shift(self._y, sr=self._sr, n_steps=change)
