def reverse_text(text: str) -> str:
    return text[::-1]

"Odwraca teks, zwraca str"

def count_words(text: str) -> int:
    return len(text.split())

"Liczy słowa w tekście, zwraca int"

def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

"Sprawdza, czy tekst nie jest palindromem, zwraca true lub false"