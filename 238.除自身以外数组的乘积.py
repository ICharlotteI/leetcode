#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        # 计算前缀积
        pre_product = [1]
        for i in range(n):
            pre_product.append(pre_product[-1] * nums[i])
        # 计算后缀积
        post_prodcut = [1]
        for i in range(n):
            post_prodcut.append(post_prodcut[-1] * nums[n - 1 - i])
        # 计算结果
        for i in range(n):
            ans.append(pre_product[i] * post_prodcut[n - 1 - i])
        return ans

    def productExceptSelfByDiv(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        # 如果数组中有超过一个0，所有位置的结果都是0
        result = []
        if zero_count > 1:
            result = [0] * len(nums)
        elif zero_count == 1:
            for num in nums:
                if num == 0:
                    # 其他值都非零
                    result.append(total_product)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(total_product // num)

        return result


# @lc code=end
