import sys

from expression.expr.parse import parse


def evaluate(arg):
    term = parse(arg)
    result = term.evaluate()
    return result


def main(*args: str, stdout=sys.stdout, stderr=sys.stderr):
    if stdout is not None:
        sys.stdout = stdout
    if stderr is not None:
        sys.stderr = stderr
    args = args or sys.argv[1:]
    assert len(args) == 1, "wrong number of arguments"
    print(evaluate(args[0]))


if __name__ == "__main__":
    main()
