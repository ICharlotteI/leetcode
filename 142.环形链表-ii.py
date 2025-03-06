#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while True:
            # 指向空节点，说明无环
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            # 第一次相遇
            if fast == slow:
                break
        # 将fast放头
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # 第二次相遇就会在入口相遇
        return slow


# @lc code=end
