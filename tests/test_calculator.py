import math
from unittest import TestCase

from src.calculator.calculator import Calculator


class TestCalculator(TestCase):
    def test_add(self):  # type: ignore

        calc = Calculator()

        self.assertEqual(calc.value, 0)
        self.assertEqual(calc.add(4), 4)
        self.assertEqual(calc.add(6), 10)
        self.assertEqual(calc.add(99999), 100009)

    def test_sub(self):
        calc = Calculator()

        self.assertEqual(calc.value, 0)
        self.assertEqual(calc.sub(10), -10)
        self.assertEqual(calc.sub(14), -24)
        self.assertEqual(calc.sub(489498), -489522)

    def test_div(self):
        calc = Calculator(2041)

        self.assertEqual(calc.div(16.25), 125.6)

    def test_div_by_zero(self):
        calc = Calculator(10)

        with self.assertRaises(ZeroDivisionError):
            calc.div(0)


    def test_mult(self):
        calc = Calculator(2)

        self.assertEqual(calc.mult(2), 4)
        self.assertEqual(calc.mult(2), 8)
        self.assertEqual(calc.mult(2), 16)
        self.assertEqual(calc.mult(2), 32)
        self.assertEqual(calc.mult(32), 1024)

    def test_root(self):
        n = 256
        calc = Calculator(n)

        self.assertEqual(calc.root(n), math.sqrt(256))

    def test_clear(self):
        calc = Calculator()
        self.assertEqual(calc.add(66), 66)
        self.assertEqual(calc.add(500), 566)
        self.assertEqual(calc.add(5000), 5566)
        self.assertEqual(calc.add(50000), 55566)
        self.assertEqual(calc.sub(37044), 18522)
        self.assertEqual(calc.mult(8), 74088*2)
        self.assertEqual(calc.div(2), 74088)

        self.assertEqual(calc.root(3), 42)

        calc.clear()
        self.assertEqual(calc.value, 0)

        # 18522
        # 74088
