from typing import Optional
from list_node import ListNode

'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
'''

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev