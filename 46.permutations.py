#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time Complexcity: O(N x N!)
        # Space Complexcity: O(N!)
        def helper(nums, cur, res, used):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    cur.append(nums[i])
                    used[i] = True
                    helper(nums, cur, res, used)
                    cur.pop()
                    used[i] = False
        
        used = [False for _ in range(len(nums))]
        cur = []
        res = []
        helper(nums, cur, res, used)
        return res
# @lc code=end

