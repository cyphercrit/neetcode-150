import unittest
from valid_parentheses import Solution as IsValid

class TestValidParenthesis(unittest.TestCase):
    def test_valid_parenthesis(self):
        solution = IsValid()
        self.assertTrue(solution.isValid("[]"))
        self.assertTrue(solution.isValid("([{}])"))
        self.assertFalse(solution.isValid("[(])"))

if __name__ == "__main__":
    unittest.main()