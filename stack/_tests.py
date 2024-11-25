import unittest
from valid_parentheses import Solution as IsValid
from evaluate_reverse_polish_notation import Solution as EvalRPN

class TestValidParenthesis(unittest.TestCase):
    def test_valid_parenthesis(self):
        solution = IsValid()
        self.assertTrue(solution.isValid("[]"))
        self.assertTrue(solution.isValid("([{}])"))
        self.assertFalse(solution.isValid("[(])"))

class TestEvalRPN(unittest.TestCase):
    def test_evaluate_reverse_polish_notation(self):
        solution = EvalRPN()
        self.assertEqual(solution.evalRPN(["1","2","+","3","*","4","-"]), 5)
        self.assertEqual(solution.evalRPN(["2","1","+","3","*"]), 9)
        self.assertEqual(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)

if __name__ == "__main__":
    unittest.main()