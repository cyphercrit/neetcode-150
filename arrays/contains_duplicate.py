from typing import List

'''
Given an integer array nums, return true if any value appears more than
once in the array, otherwise return false
'''

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        # checks each number in nums, if it has been seen before, return False
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        
        return False