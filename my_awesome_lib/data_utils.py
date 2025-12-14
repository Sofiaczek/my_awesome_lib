def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)


def max_value(numbers: list[float]) -> float:
    return max(numbers)