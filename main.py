import color_temperature
from PIL import Image
import sys

if __name__ == '__main__':
    color_temperature.convert_temp(Image.open(str(sys.argv[1])), int(sys.argv[2]))


