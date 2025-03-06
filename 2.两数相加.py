#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = ans = ListNode(0)
        # 进位
        c = 0
        while l1 or l2 or c != 0:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            cur_sum = a + b + c
            if cur_sum >= 10:
                c = 1
                cur_sum %= 10
            else:
                c = 0
            cur.next = ListNode(cur_sum)
            cur = cur.next
        return ans.next


# @lc code=end
