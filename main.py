import color_temperature
from PIL import Image

if __name__ == '__main__':
    color_temperature.convert_temp(Image.open('img/before/bliss.jpg'), 2500)
    
    
# TODO: add arguments
# TODO: test (read rgb from image: min 3 tests)
