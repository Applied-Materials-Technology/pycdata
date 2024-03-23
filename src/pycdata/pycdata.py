# pycdata
from pathlib import Path
import time

class Timer:

    def __init__(self, run_time: float = 0.0) -> None:
        self._start_time = 0.0
        self._run_time = run_time

    def start(self,run_time: float | None = None) -> None:
        if run_time is not None:
            self._run_time = run_time

        self._start_time = time.perf_counter()

    def finished(self) -> bool:
        return (time.perf_counter() - self._start_time) >= self._run_time

    def elapsed_time(self) -> float:
        return (time.perf_counter() - self._start_time)


class CameraDataGenerator:
    def __init__(self, frequency: float = 1.0) -> None:
        self._frequency = frequency
        self._target_path = Path.cwd()

    def generate_data(self) -> None:
        pass
