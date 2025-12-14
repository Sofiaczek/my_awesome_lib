def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result