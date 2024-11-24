import unittest
from contains_duplicate import Solution as ContainsDuplicate
from valid_anagram import Solution as ValidAnagram
from two_sum import Solution as TwoSum

class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = ContainsDuplicate()
        self.assertTrue(solution.containsDuplicate([1,2,3,3]))
        self.assertFalse(solution.containsDuplicate([1,2,3,4]))

class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram(self):
        solution = ValidAnagram()
        self.assertTrue(solution.isAnagram("racecar", "carrace"))
        self.assertFalse(solution.isAnagram("jar", "jam"))

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = TwoSum()
        self.assertEqual(solution.twoSum([3,4,5,6], 7), [0,1])
        self.assertEqual(solution.twoSum([4,5,6], 10), [0, 2])
        self.assertEqual(solution.twoSum([5,5], 10), [0, 1])

if __name__ == "__main__":
    unittest.main()
