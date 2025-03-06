#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
from collections import defaultdict


# 前缀树节点
class TrieNode:
    def __init__(self):
        self.hashmap = defaultdict(TrieNode)
        self.isEnd = False


# 前缀树  小写字母——26个节点
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.hashmap:
                cur.hashmap[ch] = TrieNode()
            cur = cur.hashmap[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.hashmap:
                return False
            cur = cur.hashmap[ch]
        return cur is not None and cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.hashmap:
                return False
            cur = cur.hashmap[ch]
        return cur is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
