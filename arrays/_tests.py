import unittest
from contains_duplicate import Solution as ContainsDuplicate
from valid_anagram import Solution as ValidAnagram

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

if __name__ == "__main__":
    unittest.main()

