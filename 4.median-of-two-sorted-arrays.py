#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        l1 = 0
        r1 = len(nums1)
        while l1 <= r1:
            m1 = l1 + (r1 - l1) // 2
            m2 = (len(nums1) + len(nums2) + 1) // 2 - m1
            maxLeft1 = float('-inf') if (m1 == 0) else nums1[m1 - 1]
            minRight1 = float('inf') if (m1 == len(nums1)) else nums1[m1]
            maxLeft2 = float('-inf') if (m2 == 0) else nums2[m2 - 1]
            minRight2 = float('inf') if (m2 == len(nums2)) else nums2[m2]
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2))/2.0
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
        
# @lc code=end

