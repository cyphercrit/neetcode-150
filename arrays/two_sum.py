from typing import List

'''
Given an array of integers nums and an integer target, return the 
indices i and j such that nums[i] + nums[j] == target and i != j

You may assume that every input has exactly one pair of indices
i and j that satisfy the condition
'''

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            # checks to see if the number we need is in the num_map
            if diff in num_map:
                # returns the indices of the number, with the first index first
                return [num_map[diff], i]
            # adds num and index to num_map if diff isn't found
            num_map[num] = i
        
        return