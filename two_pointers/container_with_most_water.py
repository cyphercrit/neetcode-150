from typing import List

'''
You are given an integer array heights where heights[i] represents the height of the ithith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_area = 0
        while left < right:
            # calculates area for current indices and compares it with max_area
            max_area = max((right-left) * min(heights[left], heights[right]), max_area)

            # sticks with the taller of the two heights every time
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area