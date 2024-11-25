import unittest
from valid_palindrome import Solution as ValidPalindrome
from two_sum_2 import Solution as TwoSum
from three_sum import Solution as ThreeSum

class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        solution = ValidPalindrome()
        self.assertTrue(solution.isPalindrome("Was it a car or a cat I saw?"))
        self.assertFalse(solution.isPalindrome("tab a cat"))
    
class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = TwoSum()
        self.assertEqual(solution.twoSum([1,2,3,4], 3), [1, 2])

class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        solution = ThreeSum()
        self.assertEqual(sorted(solution.threeSum([-1,0,1,2,-1,-4])), [[-1,-1,2], [-1,0,1]])
        self.assertEqual(solution.threeSum([0,1,1]), [])
        self.assertEqual(solution.threeSum([0,0,0]), [[0,0,0]])
        self.assertEqual(solution.threeSum([-2,0,0,2,2]), [[-2,0,2]])
      
if __name__ == "__main__":
    unittest.main()