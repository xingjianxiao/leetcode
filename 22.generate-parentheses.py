#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Time Complexcity: O(2^n)
        def helper(n, openb, closeb, cur, res):
            if openb == n and closeb == n:
                res.append(cur)
                return
            if openb < n:
                helper(n, openb + 1, closeb, cur + '(', res)
            if openb > closeb:
                helper(n, openb, closeb + 1, cur + ')', res)

        cur = ''
        res = []
        helper(n, 0, 0, cur, res)
        return res
# @lc code=end

