from unittest import TestCase

from expression.evaluate import evaluate
from expression.expr.arithmetic import Constant, Div, Add, Mul
from expression.expr.parse import parse


class TestEvaluate(TestCase):
    def test_eval_constant(self):
        self.assertEqual(0, evaluate("0"))

    def test_eval_div(self):
        self.assertAlmostEqual(0.5, evaluate("1 / 2"), 5)

    def test_eval_div_error(self):
        self.assertRaises((ValueError, AssertionError), evaluate("1 / 0"))

    def test_eval_add(self):
        self.assertEqual(4, evaluate("1 + 3"))

    def test_eval_complex(self):
        self.assertEqual(8, evaluate("(1 + 3) * 2"))
