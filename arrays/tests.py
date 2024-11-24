import unittest
from contains_duplicate import Solution as ContainsDuplicate

class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = ContainsDuplicate()
        self.assertTrue(solution.containsDuplicate([1,2,3,3]))
        self.assertFalse(solution.containsDuplicate([1,2,3,4,4]))

if __name__ == "__main__":
    unittest.main()

