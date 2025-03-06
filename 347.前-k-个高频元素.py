#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from heapq import *
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        couter = Counter(nums)
        # heapq中的函数传元组会从前往后依次比较
        # 题目可以按 任意顺序 返回答案   因此可以不用管num的顺序
        min_heap = []
        for num, freq in couter.items():
            # 如果小顶堆满了
            if len(min_heap) >= k:
                # 如果新的比堆顶（最小的）还小  那说明并不是频次前k大的
                if min_heap[0][0] < freq:
                    # 弹出堆顶并插入
                    heapreplace(min_heap, (freq, num))
            else:
                heappush(min_heap, (freq, num))
        return [each[1] for each in min_heap]


# @lc code=end
