# 力扣 热题100 · 第83题 打家劫舍
# 链接: https://leetcode.cn/problems/house-robber/
#
# ---------- 思路 ----------
# 题目在问什么：一排房子每家有金额，不能偷相邻两家，求能偷到的最大金额。
#
# 做法：到第 i 家有两种选择：不偷则等于到 i-1 的最大值；偷则等于到 i-2 的最大值 + nums[i]。所以 dp[i] = max(dp[i-1], dp[i-2]+nums[i])。用两个变量滚动即可。
#
# ---------- 关键点 ----------
# · 考虑「到第 i 家为止能偷到的最大金额」：如果第 i 家不偷，答案就等于「到第 i-1 家为止的最大金额」；如果第 i 家偷，第 i-1 家就不能偷，答案就等于「到第 i-2 家为止的最大金额」+ nums[i]。两者取大，即 dp[i]=max(dp[i-1], dp[i-2]+nums[i])。只依赖前两项，用两个变量滚动即可。

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(b, a + nums[i])
        return b
