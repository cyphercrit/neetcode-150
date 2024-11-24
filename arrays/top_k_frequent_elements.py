from typing import List

'''
Given an integer array nums and an integer k, return 
the k most frequent elements within the array.

You may assume that the answer is always unique, 
and you may return the output in any order.
'''

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        # counts the frequency of each number
        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1

        # sorts each element into list, higher index -> higher frequency
        for num, freq in num_counter.items():
            freq_list[freq].append(num)
        
        # pops values from freq list and appends to result
        result = []
        while len(result) < k:
            popped = freq_list.pop()
            while len(popped) > 0:
                result.append(popped.pop())
        
        return result


        


        

