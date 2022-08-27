import color_temperature
from PIL import Image
import sys

if __name__ == '__main__':
    print(str(sys.argv[1]), sys.argv[2])
    color_temperature.convert_temp(Image.open(str(sys.argv[1])), int(sys.argv[2]))
    # str(sys.argv[1]), sys.argv[2]
    # color_temperature.convert_temp(Image.open('img/before/bliss.jpg'), 2500)
    
    
# TODO: write readme.md
# TODO: test (read rgb from image: min 3 tests)
