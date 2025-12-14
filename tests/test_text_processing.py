import unittest
from my_awesome_lib.text_processing import reverse_text, count_words, is_palindrome

"Testy dla modułu text_procesing"

class TestTextProcessing(unittest.TestCase):

    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))