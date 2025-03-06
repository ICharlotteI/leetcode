#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        stack = []
        p = dummy = ListNode(0)
        # 遍历链表
        cur = head
        while cur and cur.next:
            stack.append(cur)
            stack.append(cur.next)
            cur = cur.next.next

            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next
        # 当链表长度是奇数时，后面仍有奇数个节点
        p.next = cur
        return dummy.next


# @lc code=end
