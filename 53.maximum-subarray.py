#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexcity: O(n)
        # Space Complexcity: O(1)
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum
# @lc code=end
