import unittest
from list_node import ListNode
from typing import Optional
from reverse_linked_list import Solution as ReverseList

# a helper method for making linked lists in tests
def create_list(arr: list) -> Optional[ListNode]:
    if arr == []:
        return None
    else:
        head = ListNode(arr[0])

        current = head

        for element in arr[1:]:
            current.next = ListNode(element)
            current = current.next
        
        return head

# a helper method for converting a linked list to a list
def to_list(head: Optional[ListNode]) -> list:
    if head == None:
        return []
    
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    
    return arr


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        solution = ReverseList()

        self.assertEqual(to_list(solution.reverseList(create_list([0,1,2,3]))), [3,2,1,0])
        self.assertEqual(to_list(solution.reverseList(create_list([]))), [])
        

if __name__ == "__main__":
    unittest.main()