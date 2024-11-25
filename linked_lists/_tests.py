import unittest
from linked_list_tools import LinkedListTools
from reverse_linked_list import Solution as ReverseList

class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        solution = ReverseList()
        tools = LinkedListTools()

        self.assertEqual(tools.apply_function(solution.reverseList, [0,1,2,3]), [3,2,1,0])
        self.assertEqual(tools.apply_function(solution.reverseList, []), [])
        

if __name__ == "__main__":
    unittest.main()