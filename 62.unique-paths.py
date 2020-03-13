#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # TimeComplexcity: O(mn)
        # SpaceComplexcity: O(mn)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = 1
                if j == 0:
                    dp[i][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# @lc code=end
