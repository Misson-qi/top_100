# 力扣 热题100 · 第89题 分割等和子集
# 链接: https://leetcode.cn/problems/partition-equal-subset-sum/
#
# ---------- 思路 ----------
# 题目在问什么：数组能否分成两堆，两堆和相等。等价于能否选出若干数使其和为总和的一半。
#
# 做法：若总和为奇数直接 False。否则 target = sum//2，用 0-1 背包：dp[j] 表示能否凑出和 j。dp[0]=True；遍历每个数 num，从 target 倒着到 num，dp[j] = dp[j] or dp[j-num]。最后看 dp[target]。
#
# ---------- 关键点 ----------
# · 分成两堆和相等，等价于能否选出若干数，使它们的和等于全部数总和的一半（target=sum/2）。总和若是奇数，不可能平分，直接 False。
# · 0-1 背包：dp[j] 表示能否凑出和 j。对每个数 num，要么不选要么选；从 target 倒着枚举 j 到 num，dp[j]=dp[j] or dp[j-num]（不选则保持，选则看 j-num 能否凑出）。为什么要倒序？因为正序的话，dp[j-num] 可能已经用过当前 num，相当于同一个数用了多次；倒序保证 dp[j-num] 是「还没考虑当前 num」时的状态。

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]
