import unittest
from valid_palindrome import Solution as ValidPalindrome

class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        solution = ValidPalindrome()
        self.assertTrue(solution.isPalindrome("Was it a car or a cat I saw?"))
        self.assertFalse(solution.isPalindrome("tab a cat"))
    
if __name__ == "__main__":
    unittest.main()