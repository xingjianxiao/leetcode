#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # time complexcity: O(3^N x 4^M)
        # space complexcity: O(3^N x 4^M)

        if len(digits) == 0:
            return []
        d = {}
        s = 'abcdefghijklmnopqrstuvwxyz'
        count = 0
        for i in range(2, 10):
            if i == 7 or i == 9:
                d[str(i)] = [s[count], s[count + 1], s[count + 2], s[count + 3]]
                count = count + 4
            else:
                d[str(i)] = [s[count], s[count + 1], s[count + 2]]
                count = count + 3

        def backtrack(digits, idx, cur, res):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in d[digits[idx]]:
                cur += c
                backtrack(digits, idx + 1, cur, res)
                cur = cur[:-1]
        
        res = []
        cur = ''
        backtrack(digits, 0, cur, res)
        return res


# @lc code=end

