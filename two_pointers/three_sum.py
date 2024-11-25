from typing import List

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''

# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        first = 0
        nums.sort()

        # loops until after first, second, third are right next to eachother
        result = []
        while first + 2 < len(nums):
            # skips duplicate first values
            if first != 0 and nums[first] == nums[first-1]:
                first += 1
                continue

            second, third = first + 1, len(nums) - 1

            while second < third:
                curr_sum = nums[first] + nums[second] + nums[third]

                if curr_sum < 0:
                    second += 1
                    continue

                if curr_sum > 0:
                    third -= 1
                    continue

                if curr_sum == 0:
                    result.append([nums[first], nums[second], nums[third]])
                    # skips duplicates
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
                    third -= 1
            
            first += 1

        return result

