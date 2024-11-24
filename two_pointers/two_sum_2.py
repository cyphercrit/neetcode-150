from typing import List

'''
Given an array of 1-indexed integers nums and an integer target, return the 
indices i and j such that nums[i] + nums[j] == target and i != j

You may assume that every input has exactly one pair of indices
i and j that satisfy the condition

Your solution must use O(1) additional space
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        # runs until the two numbers are found
        while nums[left] + nums[right] != target:
            curr_sum = nums[left] + nums[right]
            
            # makes curr_sum closer to target, depending on if it is > or <
            if curr_sum > target:
                right -= 1
                continue

            if curr_sum < target:
                left += 1
                continue
        
        # adds 1 for one-indexing
        return [left + 1, right + 1]