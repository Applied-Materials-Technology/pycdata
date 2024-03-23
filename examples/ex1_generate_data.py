'''
================================================================================
pycdata: generate camera data example
================================================================================
'''
from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pycdata


def main() -> None:
    data_gen = pycdata.CameraDataGenerator()

    data_gen.set_target_path(Path('examples/gen_data'))

    image_files = [Path('data/OptSpeckle_5Mpx_2464_2056_width5_8bit_GBlur1.tiff'),
                   Path('data/OptSpeckle_5Mpx_2464_2056_width5_8bit_GBlur1.tiff')]
    data_gen.load_image_files(image_files)
    image = np.array(Image.open(image_files[0]))
    print(image.dtype == np.uint8)

    print("="*80)
    print("START.")
    print("="*80)

    data_gen.generate_data(duration=3.1)

    print("="*80)
    print("END.")
    print("="*80)


if __name__ == '__main__':
    main()
