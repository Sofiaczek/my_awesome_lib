def reverse_text(text: str) -> str:
    return text[::-1]


def count_words(text: str) -> int:
    return len(text.split())


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]