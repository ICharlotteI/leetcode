#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = dummy = ListNode(0)
        while True:
            counter = k
            stack = []
            cur = head
            while counter > 0 and cur:
                stack.append(cur)
                cur = cur.next
                counter -= 1
            # 后面的不足够翻转，直接放到p后面
            if counter > 0:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            head = cur
        return dummy.next


# @lc code=end
