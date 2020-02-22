#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # time complexcity: O(max(l1,l2))
        # space complexcity: O(max(l1,l2) + 1) 1 for dummy node
        dummy = ListNode(None)
        result = dummy
        added = 0
        while l1 or l2:
            if l1 and l2:
                if l1.val + l2.val + added > 9:
                    new_node = ListNode(l1.val + l2.val + added - 10)
                    dummy.next = new_node
                    added = 1
                else:
                    new_node = ListNode(l1.val + l2.val + added)
                    dummy.next = new_node
                    added = 0
                dummy = dummy.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if l1.val + added > 9:
                    new_node = ListNode(l1.val + added - 10)
                    dummy.next = new_node
                    added = 1
                else:
                    new_node = ListNode(l1.val + added)
                    dummy.next = new_node
                    added = 0
                dummy = dummy.next
                l1 = l1.next
            elif l2:
                if l2.val + added > 9:
                    new_node = ListNode(l2.val + added - 10)
                    dummy.next = new_node
                    added = 1
                else:
                    new_node = ListNode(l2.val + added)
                    dummy.next = new_node
                    added = 0
                dummy = dummy.next
                l2 = l2.next
        if added == 1:
            new_node = ListNode(1)
            dummy.next = new_node
        return result.next
            
# @lc code=end

