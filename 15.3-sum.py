#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time complexity: O(n^2)
        # Space complexity: O(p) where p is the number of accepted solutions
        nums.sort()
        res = []
        d = {}
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j], nums[k]) not in d:
                        d[(nums[i], nums[j], nums[k])] = 1
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res

# @lc code=end

