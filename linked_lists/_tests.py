import unittest
from linked_list_tools import LinkedListTools
from reverse_linked_list import Solution as ReverseList
from merge_two_sorted_lists import Solution as MergeTwoLists

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        solution = ReverseList()
        tools = LinkedListTools()

        self.assertEqual(tools.apply_function(solution.reverseList, [0,1,2,3]), [3,2,1,0])
        self.assertEqual(tools.apply_function(solution.reverseList, []), [])
    
class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        solution = MergeTwoLists()
        tools = LinkedListTools()

        self.assertEqual(tools.apply_function_two_lists(solution.mergeTwoLists, [1,3], [0,2]), [0,1,2,3])
        self.assertEqual(tools.apply_function_two_lists(solution.mergeTwoLists, [1,2,4], [1,3,5]), [1,1,2,3,4,5])
        self.assertEqual(tools.apply_function_two_lists(solution.mergeTwoLists, [], [1,2]), [1,2])
        self.assertEqual(tools.apply_function_two_lists(solution.mergeTwoLists, [], []), [])

if __name__ == "__main__":
    unittest.main()