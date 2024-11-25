from typing import Optional, Callable
from list_node import ListNode

class LinkedListTools():
    # converts a list to a linked list
    def create_list(self, arr: list) -> Optional[ListNode]:
        if arr == []:
            return None
        else:
            head = ListNode(arr[0])

            current = head

            for element in arr[1:]:
                current.next = ListNode(element)
                current = current.next
            
            return head

    # converts a linked list to a list
    def to_list(self, head: Optional[ListNode]) -> list:
        if head == None:
            return []
        
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        
        return arr
    
    # applies a function to a linked list created from a list and returns the result as a list
    def apply_function(self, func: Callable[[Optional[ListNode]], Optional[ListNode]], arr: list) -> list:
        linked_list = self.create_list(arr)
        result_linked_list = func(linked_list)
        return self.to_list(result_linked_list)