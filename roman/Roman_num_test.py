import unittest
from NumberToRoman import numbertoRoman
from ValidateDate import validate

class RomanTests(unittest.TestCase):

    def test_1 (self):
        self.assertEqual(numbertoRoman(1), "I")

    def test_50 (self):
        self.assertEqual(numbertoRoman(50), "L")

    def test_1234 (self):
        self.assertEqual(numbertoRoman(1234), "MCCXXXIV")
    
    def test_9999 (self):
        self.assertEqual(numbertoRoman(9999), "MMMMMMMMMCMXCIX")

if __name__ == '__main__':
    unittest.main()