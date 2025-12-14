def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

"Liczy średnią z listy, zwraca float "

def max_value(numbers: list[float]) -> float:
    return max(numbers)

"Szuka najwyższej wartości, zwraca float"