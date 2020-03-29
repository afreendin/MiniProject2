from HelperFunctions import HelperFunctions
import unittest
import csv


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = HelperFunctions

    # def test_instantiate_calculator(self):
    #     self.assertIsInstance(self.calc, HelperFunctions)

    def test_add(self):
        self.assertEqual(self.calc.add(10,20), 30.0)

    def test_subtract(self):
       self.assertEqual(self.calc.subtract(30,10), 20.0)

    def test_multiply(self):
       self.assertEqual(self.calc.multiply(3,2), 6.0)

    def test_division(self):
        self.assertEqual(self.calc.division(10,2), 5.0)

    def test_square(self):
        self.assertEqual(self.calc.square(3), 9.0)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(9), 3.0)


if __name__ == '__main__':
    unittest.main()