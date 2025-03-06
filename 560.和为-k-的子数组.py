#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dic = collections.defaultdict(int)
        # 前缀和
        preSum = 0
        dic[0] = 1
        for num in nums:
            preSum += num
            # 判断当前前面是否有能够满足条件的前缀和出现
            # 如果有  有几个就代表前面有几个前缀和能够和当前前缀和组成满足条件的子数组
            if dic.get(preSum - k, 0)!=0:
                ans += dic[preSum - k]
            dic[preSum] += 1
        return ans


# @lc code=end
