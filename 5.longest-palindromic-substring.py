#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # time complexcity:O(n^2)
        # space complexcity:O(n^2)

        # dp relationshiop dp[i,j] = dp[i] == dp[j] and dp[i + 1][j - 1]
        if not s:
            return ""
        max_length = 1
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res_i = 0
        res_j = 0
        for i in range(len(s) - 1):
            dp[i][i] = True
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_length = 2
                res_i = i
                res_j = i + 1
        
        for j in range(1, len(s)):
            for i in range(0, j):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        res_i = i
                        res_j = j
                        
        return s[res_i:res_j + 1]
                
# @lc code=end

