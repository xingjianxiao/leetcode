#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # time complexcity: O(n)
        # space complexcity: O(m) m:number of distinct character in s
        
        # keep updating the index of each character if the index is less 
        # than the current starting index of the substring we ignore it 
        # and update its value else if it is in the substring we start 
        # the substring from the lastest seen index of that character + 1
        d = collections.defaultdict(int)
        start = 0
        end = -1
        max_length = 0
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
                end += 1
            else:
                if d[c] < start:
                    d[c] = i
                else:
                    start = d[c] + 1
                    d[c] = i
                end += 1
            max_length = max(max_length, end - start + 1)

        return max_length
# @lc code=end

