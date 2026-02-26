# 力扣 热题100 · 第88题 乘积最大子数组
# 链接: https://leetcode.cn/problems/maximum-product-subarray/
#
# ---------- 思路 ----------
# 题目在问什么：找连续子数组使乘积最大（有正负，求子数组乘积最大值）。
#
# 做法：因为有负数，负负得正，所以要同时记「以当前结尾的最大乘积」和「以当前结尾的最小乘积」。到新数时，新最大 = max(最大*当前, 最小*当前, 当前)，新最小 = min(三者)。用这两个数更新答案和下一轮。
#
# ---------- 关键点 ----------
# · 和「最大子数组和」不同，乘积有负数时「负负得正」，当前很小的负数乘下一个负数可能变成很大的正数。所以不能只记「以当前结尾的最大乘积」，还要记「以当前结尾的最小乘积」。新来一个数 x 时：新的最大 = max(x, 最大*x, 最小*x)（单独成段、接在最大后面、接在最小后面），新的最小 = min(x, 最大*x, 最小*x)。用新的最大更新全局答案。

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = max_p = min_p = nums[0]
        for x in nums[1:]:
            max_p, min_p = max(x, max_p * x, min_p * x), min(x, max_p * x, min_p * x)
            ans = max(ans, max_p)
        return ans
