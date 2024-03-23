'''
================================================================================
pycdata: mono-repo
================================================================================
'''
from pathlib import Path
import time
import shutil
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



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


class DataGeneratorError(Exception):
    pass


class CameraDataGenerator:
    def __init__(self, frequency: float = 1.0) -> None:

        self._frequency = frequency
        self._target_path = Path.cwd()

        self._image_count = 0

        self._trace_file = None
        self._image_files = list([])

        self._trace_file_tag = 'Image'
        self._image_file_tag = 'Image'


    def set_target_path(self, targ_path: Path) -> None:

        if not targ_path.is_dir():
            raise FileNotFoundError("Target path does not exist.")

        self._target_path = targ_path


    def load_image_files(self, in_files: list[Path]) -> None:

        for ff in in_files:
            if not ff.is_file():
                raise FileNotFoundError("Specified image file: {ff}, does not exist")

        self._image_files = list([])
        for ff in in_files:
            image = Image.open(ff)
            self._image_files.append(np.array(image))


    def reset(self) -> None:
        self._image_count = 0


    def generate_data(self, duration: float) -> None:

        if duration < 0.0:
            raise DataGeneratorError("Data generation duration must be greater than 0")

        duration_timer = Timer(duration)
        output_timer = Timer(1.0/self._frequency)

        duration_timer.start()
        output_timer.start()

        while not duration_timer.finished():
            if output_timer.finished():
                output_timer.start()
                print(f'Duration = {duration_timer.elapsed_time()}s')

                self.write_traces()
                self.write_images()


    def write_traces(self) -> None:
        pass


    def write_images(self) -> None:

        for nn,ii in enumerate(self._image_files):
            image_num_str = str(self._image_count).zfill(4)
            save_file = f'{self._image_file_tag}_{image_num_str }_{nn}.tiff'
            save_path = self._target_path / save_file

            im = Image.fromarray(ii)
            im.save(save_path)

        self._image_count += 1








