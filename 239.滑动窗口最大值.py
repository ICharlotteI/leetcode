#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List
import collections


# 单调队列模拟滑动窗口 先进先出
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        ans = []
        nums_len = len(nums)
        for i, j in zip(range(1 - k, nums_len + 1 - k), range(nums_len)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 形成窗口，取最大值
            if i >= 0:
                ans.append(deque[0])
        return ans


# @lc code=end
