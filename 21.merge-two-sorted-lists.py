#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Time Complexcity:O(m + n)
        # Space Complexcity:O(1)
        dummy = ListNode(None)
        res = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
            l1 = l1.next
            dummy = dummy.next
        if l2:
            dummy.next = l2
            l2.next = l2.next
            dummy = dummy.next
        return res.next

# @lc code=end

