import sys

sys.path.append('../HelperFunctions')
from HelperFunctions.HelperFunctions import add
from HelperFunctions.HelperFunctions import subtract
from HelperFunctions.HelperFunctions import multiply
from HelperFunctions.HelperFunctions import division
from HelperFunctions.HelperFunctions import square
from HelperFunctions.HelperFunctions import square_root
import unittest
import csv

# from Calculator.Addition import addition
# from Calculator.Subtraction import subtraction
# from Calculator.Division import division
# from Calculator.Multiplication import multiplication
# from Calculator.Sqrt import root


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # self.calc = HelperFunctions
        pass

    def test_add(self):
        self.assertEqual(add(10,20), 30.0)

    def test_subtract(self):
       self.assertEqual(subtract(30,10), 20.0)

    def test_multiply(self):
       self.assertEqual(multiply(3,2), 6.0)

    def test_division(self):
        self.assertEqual(division(10,2), 5.0)

    def test_square(self):
        self.assertEqual(square(3), 9.0)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3.0)

    # def test_instantiate_calculator(self):
    #     self.assertIsInstance(self.calc, HelperFunctions)


    # def test_add(self):
    #     self.assertEqual(self.addition(10,20), 30.0)
    #
    # def test_subtract(self):
    #    self.assertEqual(self.subtraction(30,10), 20.0)
    #
    # def test_multiply(self):
    #    self.assertEqual(self.multiplication(3,2), 6.0)
    #
    # def test_division(self):
    #     self.assertEqual(self.division(10,2), 5.0)
    #
    # def test_square(self):
    #     self.assertEqual(self.square(3), 9.0)
    #
    # def test_square_root(self):
    #     self.assertEqual(self.sqrt(9), 3.0)


if __name__ == '__main__':
    unittest.main()