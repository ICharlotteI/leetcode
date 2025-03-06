#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start


class ListNode:
    def __init__(self, key=0, value=0, preNode=None, nextNode=None):
        self.key = key
        self.val = value
        self.preNode = preNode
        self.nextNode = nextNode


class LRUCache:

    def __init__(self, capacity: int) -> int:
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nextNode = self.tail
        self.tail.preNode = self.head

    """
    用于将最近访问的放至链表末尾，链表头是最近最少使用的
    """

    def move_to_tail(self, key: int):
        cur_node = self.dic[key]
        cur_node.nextNode.preNode = cur_node.preNode
        cur_node.preNode.nextNode = cur_node.nextNode
        cur_node.nextNode = self.tail
        cur_node.preNode = self.tail.preNode
        self.tail.preNode.nextNode = cur_node
        self.tail.preNode = cur_node
        return cur_node.val

    def get(self, key: int) -> int:
        res = self.dic.get(key, -1)
        if res != -1:
            return self.move_to_tail(key=key)
        else:
            return res

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            self.move_to_tail(key=key)
            return
        length = len(self.dic)
        if length >= self.capacity:
            self.dic.pop(self.head.nextNode.key)
            self.head.nextNode = self.head.nextNode.nextNode
            self.head.nextNode.preNode = self.head
        new_node = ListNode(key, value)
        new_node.nextNode = self.tail
        new_node.preNode = self.tail.preNode
        self.tail.preNode.nextNode = new_node
        self.tail.preNode = new_node
        self.dic[key] = new_node
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
