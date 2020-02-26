#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time Complexcity: O(nk) where k is the length of each string
        # Space Complexcity: O(nk)
        d = collections.defaultdict(list)
        for i in range(len(strs)):
            count = [0 for _ in range(26)]
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            d[tuple(count)].append(strs[i])
        res = []
        for key in d:
            res.append(d[key])
        return res
            
# @lc code=end

