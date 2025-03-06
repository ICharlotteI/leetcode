#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# B + (A-Common) = A + (B-Common)
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        A, B = headA, headB
        while A != B:
            if A != None:
                A = A.next
            else:
                A = headB

            if B != None:
                B = B.next
            else:
                B = headA
        return A


# @lc code=end
