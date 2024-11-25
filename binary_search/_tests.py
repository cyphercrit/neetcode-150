import unittest
from binary_search import Solution as BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        solution = BinarySearch()

        self.assertEqual(solution.search([1], 1), 0)
        self.assertEqual(solution.search([1,2,3], 2), 1)
        self.assertEqual(solution.search([-1,0,2,4,6,8], 4), 3)
        self.assertEqual(solution.search([-1,0,2,4,6,8], 3), -1)

if __name__ == "__main__":
    unittest.main()