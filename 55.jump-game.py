#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Time Complexcity: O(n)
        # Space Complexcity: O(1)
        max_step = nums[0]
        for i in range(len(nums)):
            if i <= max_step:
                max_step = max(max_step, i + nums[i])
        return max_step >= len(nums) - 1
# @lc code=end
