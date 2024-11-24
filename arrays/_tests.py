import unittest
from contains_duplicate import Solution as ContainsDuplicate
from valid_anagram import Solution as ValidAnagram
from two_sum import Solution as TwoSum
from top_k_frequent_elements import Solution as TopKFrequent
from product_of_array_except_self import Solution as ProductExceptSelf

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

class TestTopKFrequent(unittest.TestCase):
    def test_top_k_frequent(self):
        solution = TopKFrequent()
        self.assertEqual(sorted(solution.topKFrequent([1,2,2,3,3,3], 2)), [2, 3])
        self.assertEqual(sorted(solution.topKFrequent([7,7], 1)), [7])

class TestProductExceptSelf(unittest.TestCase):
    def test_product_except_self(self):
        solution = ProductExceptSelf()
        self.assertEqual(solution.productExceptSelf([1,2,4,6]), [48,24,12,8])
        self.assertEqual(solution.productExceptSelf([-1,0,1,2,3]), [0,-6,0,0,0])
        self.assertEqual(solution.productExceptSelf([1,2,0,0,5]), [0,0,0,0,0])

if __name__ == "__main__":
    unittest.main()

