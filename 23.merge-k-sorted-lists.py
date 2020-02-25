#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # priority queue approach
        # Time Complexcity:O(Nlogk) N:total number of node k: size of heap
        # Space complexcity:O(n)
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        dummy = ListNode(None)
        res = dummy
        while heap:
            val, node = heapq.heappop(heap)
            dummy.next = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
            dummy = dummy.next
        return res.next


# @lc code=end

