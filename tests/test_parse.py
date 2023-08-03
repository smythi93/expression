from unittest import TestCase

from expression.expr.arithmetic import Constant, Div, Add, Mul
from expression.expr.parse import parse


class TestParse(TestCase):
    def test_parse_constant(self):
        term = parse("0")
        self.assertIsInstance(term, Constant)
        self.assertEqual(0, term.value)

    def test_parse_div(self):
        term = parse("1 / 0")
        self.assertIsInstance(term, Div)
        self.assertIsInstance(term.left, Constant)
        self.assertIsInstance(term.right, Constant)
        self.assertEqual(1, term.left.value)
        self.assertEqual(0, term.right.value)

    def test_parse_add(self):
        term = parse("1 + 0")
        self.assertIsInstance(term, Add)
        self.assertIsInstance(term.left, Constant)
        self.assertIsInstance(term.right, Constant)
        self.assertEqual(1, term.left.value)
        self.assertEqual(0, term.right.value)

    def test_parse_complex(self):
        term = parse("(1 + 0) * 2")
        self.assertIsInstance(term, Mul)
        self.assertIsInstance(term.left, Add)
        self.assertIsInstance(term.right, Constant)
        self.assertIsInstance(term.left.left, Constant)
        self.assertIsInstance(term.left.right, Constant)
        self.assertEqual(1, term.left.left.value)
        self.assertEqual(0, term.left.right.value)
        self.assertEqual(2, term.right.value)
