def add(a: float, b: float) -> float:
    return a + b

"Dodawanie, zwraca float"


def subtract(a: float, b: float) -> float:
    return a - b

"Odejmowanie, zwraca float"


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

"Silnia, zwraca int, wyrzuca błąd jeśli n <= 0"