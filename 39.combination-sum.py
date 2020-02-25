#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Time complexity is O(N^target) where N is a length of candidates array
        # Space complexity is O(target)
        def helper(candidates, target, s, cur, res):
            if target < 0:
                return
            if target == 0:
                res.append(cur[:])
                return
            for i in range(s, len(candidates)):
                cur.append(candidates[i])
                helper(candidates, target - candidates[i], i, cur, res)
                cur.pop()
        cur = []
        res = []
        helper(candidates, target, 0, cur, res)
        return res
# @lc code=end

