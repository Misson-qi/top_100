# 力扣 热题100 · 第87题 最长递增子序列
# 链接: https://leetcode.cn/problems/longest-increasing-subsequence/
#
# ---------- 思路 ----------
# 题目在问什么：找最长严格递增子序列的长度（不要求连续）。
#
# 做法：dp[i] 表示以 nums[i] 结尾的 LIS 长度。对每个 i，枚举 j<i，若 nums[j]<nums[i] 则可以把 nums[i] 接在 j 后面，dp[i] = max(dp[i], dp[j]+1)。答案 = max(dp)。
#
# ---------- 关键点 ----------
# · dp[i] 表示「以 nums[i] 结尾」的最长递增子序列的长度。因为子序列不要求连续，以 i 结尾的序列可以是「某个以 j 结尾的递增序列」后面接上 nums[i]，前提是 nums[j]<nums[i]。所以对每个 i，枚举所有 j<i，若 nums[j]<nums[i]，则 dp[i] 可以是 dp[j]+1；取最大值，即 dp[i]=max(dp[j]+1)。每个位置至少长度为 1（只含自己），所以 dp 初值为 1。答案在所有 dp[i] 里取最大。（进阶：用二分可做到 O(n log n)。）

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
