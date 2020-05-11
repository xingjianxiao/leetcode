#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p_0 = 0
        p_2 = len(nums) - 1
        curr = 0

        while curr <= p_2:
            if nums[curr] == 0:
                nums[p_0], nums[curr] = nums[curr], nums[p_0]
                p_0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p_2], nums[curr] = nums[curr], nums[p_2]
                p_2 -= 1
            else:
                curr += 1
# @lc code=end
