from unittest import TestCase

from expression.expr.arithmetic import Constant, Div, Add, Mul


class TestMiddle(TestCase):
    def test_constant(self):
        term = Constant(0)
        self.assertEqual(0, term.evaluate())

    def test_div(self):
        term = Div(Constant(1), Constant(2))
        self.assertAlmostEqual(0.5, term.evaluate(), 5)

    def test_div_error(self):
        term = Div(Constant(1), Constant(0))
        self.assertRaises((ValueError, AssertionError), term.evaluate)

    def test_add(self):
        term = Add(Constant(1), Constant(3))
        self.assertEqual(4, term.evaluate())

    def test_complex(self):
        term = Mul(Add(Constant(1), Constant(3)), Constant(2))
        self.assertEqual(8, term.evaluate())
