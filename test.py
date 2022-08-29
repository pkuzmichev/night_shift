import unittest
from PIL import Image
import color_temperature
from parameterized import parameterized


class TestRGB(unittest.TestCase):
    
    def setUp(self):
        self.before_image = Image.open('img/test/before.jpg')
        self.after_image = Image.open('img/test/after.jpg')
    
    @parameterized.expand([
        ['1000', 1000, (53, 107, 233)],
        ['5000', 5000, (70, 25, 2)],
        ['10000', 10000, (65, 111, 186)]
    ])
    def testChangeRGBFromList(self, name, temperature, expected):
        color_temperature.convert_temp(
            self.before_image, int(temperature), path=self.after_image.filename)
        
        self.assertEqual(self.after_image.getpixel((1, 1)), expected)
        
    def testChangeRGBFromNonList(self):
            
        with self.assertRaises(KeyError):
            color_temperature.convert_temp(
                self.before_image, int(200), path=self.after_image.filename)
            
    def tearDown(self):
        self.before_image.close()
        self.after_image.close()

