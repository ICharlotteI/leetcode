#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        p = dummy = Node(0)
        # 关键点：random需要指向新节点
        # 创建新节点
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            p.next = dic[cur]
            p = p.next
            if cur.random:
                p.random = dic[cur.random]
            cur = cur.next

        return dummy.next


# @lc code=end
