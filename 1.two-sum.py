#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # time complexcity:O(n)
        # space complexcity O(n)
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict:
                if dict[complement] != i:
                    return [i, dict[complement]]
        return []
# @lc code=end

