#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums == [] or nums_len < 3:
            return []

        nums.sort()
        ans = []
        for i in range(nums_len):
            # 对于当此时>0 后面不可能有加和等于0的了
            if nums[i] > 0:
                return ans
            # 对于重复元素跳过 避免重复解
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = nums_len - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    # 判断左界和右界是否有相同元素  避免重复解
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return ans


# @lc code=end
