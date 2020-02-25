#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Complexcity: O(log(n))
        # Space Complexcity: O(1)
        def find_piviot(nums):
            l = 0
            r = len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < nums[-1]:
                    r = m
                else:
                    l = m + 1
            return l
        
        def binary_search(nums, l, r, target):
            while l < r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return -1
        if not nums:
            return -1
        piviot = find_piviot(nums)
        if piviot == 0:
            return binary_search(nums, 0, len(nums), target)
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            return binary_search(nums, 0, piviot, target)
        else:
            return binary_search(nums, piviot, len(nums), target)
        

# @lc code=end

