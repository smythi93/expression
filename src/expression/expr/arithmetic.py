class Term:
    def evaluate(self) -> float | int:
        pass


class Binary(Term):
    def __init__(self, left: Term, right: Term):
        self.left = left
        self.right = right


class Add(Binary):
    def evaluate(self):
        l, r = self.left.evaluate(), self.right.evaluate()
        return l + r


class Sub(Binary):
    def evaluate(self):
        l, r = self.left.evaluate(), self.right.evaluate()
        return l - r


class Mul(Binary):
    def evaluate(self):
        l, r = self.left.evaluate(), self.right.evaluate()
        return l * r


class Div(Binary):
    def evaluate(self):
        l, r = self.left.evaluate(), self.right.evaluate()
        return l / r


class Neg(Term):
    def __init__(self, term: Term):
        self.term = term

    def evaluate(self) -> float | int:
        t = self.term.evaluate()
        return -t


class Constant(Term):
    def __init__(self, value: int):
        self.value = value

    def evaluate(self) -> float | int:
        return self.value
