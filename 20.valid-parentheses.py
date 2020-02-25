#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time Complecity:O(n)
        # Space Complecity:O(n) 
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ')':
                    if stack.pop() != '(':
                        return False
                elif c == '}':
                    if stack.pop() != '{':
                        return False
                elif c == ']':
                    if stack.pop() != '[':
                        return False
        if len(stack) == 0:
            return True
        return False
# @lc code=end

