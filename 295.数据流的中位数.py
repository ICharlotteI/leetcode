#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start

from heapq import *


# 在插入的时候保证列表有序即可
class MedianFinder:

    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半，方便找最小堆顶
        self.B = []  # 大顶堆，保存较小的一半，方便找最大堆顶

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            # 从A中出来一个最小的给B，可能是新元素num也可能是A中的别的
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return (
            self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
        )


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
