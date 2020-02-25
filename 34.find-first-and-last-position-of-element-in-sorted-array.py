#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexcity: O(log(n))
        # Space Complexcity: O(1)
        def upper_bound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return l - 1

        def lower_bound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        if not nums:
            return [-1,-1]
        upper_idx = upper_bound(nums, target)
        lower_idx = lower_bound(nums, target)
        if upper_idx == len(nums):
            upper_idx = -1
        if lower_idx == len(nums):
            lower_idx = -1
        if nums[upper_idx] != target:
            upper_idx = -1
        if nums[lower_idx] != target:
            lower_idx = -1
        return [lower_idx, upper_idx]
# @lc code=end

