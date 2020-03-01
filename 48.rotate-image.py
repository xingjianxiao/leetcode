#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Time Complexcity: O(n^2)
        # Space Complexcity: O(1)
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

# @lc code=end
