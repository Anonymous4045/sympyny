from pathlib import Path
from typing import Any

import simpleaudio
import soundfile


def play_sound(path: Path | str) -> None:
    """Plays the wav file located at the given path"""
    simpleaudio.WaveObject.from_wave_file(Path(path).as_posix()).play().wait_done()


def write_sound(output_path: Path | str, data: Any, sample_rate: int) -> None:
    """Create a wav file from the given data and write it to the given path"""
    soundfile.write(Path(output_path).as_posix(), data, sample_rate, format="wav")
