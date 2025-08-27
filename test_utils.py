import unittest
from utils import palindrome_checker

class TestPalindromes(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome_checker("racecar"))

    def test_notPalindrome(self):
        self.assertFalse(palindrome_checker("palindrome"))
    
    def test_alsoPalindrome(self):
        self.assertTrue(palindrome_checker("Hannah"))

if __name__ == '__main__':
    unittest.main()