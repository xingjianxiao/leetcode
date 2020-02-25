#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time complexity: O(n)
        # Space complexity: O(1)
        start = 0
        end = len(height) - 1
        max_water = -1
        while start < end:
            max_water = max(max_water, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_water
            
# @lc code=end

