from typing import List

'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer. 
'''

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        # finds product of entire list
        for num in nums:
            # if zero_count reaches > 1, the entire array will be 0s
            if num == 0:
                zero_count += 1
            else:
                product *= num

        if zero_count > 1:
            return [0] * len(nums)
        
        result = []
        for num in nums:
            if zero_count:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // num)
        
        return result