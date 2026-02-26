# 力扣 热题100 · 第85题 零钱兑换
# 链接: https://leetcode.cn/problems/coin-change/
#
# ---------- 思路 ----------
# 题目在问什么：若干面额的硬币无限个，凑成 amount 最少要几枚；凑不出返回 -1。
#
# 做法：dp[i] = 凑成金额 i 的最少硬币数。dp[0]=0；对 i 从 1 到 amount，枚举每种面额 c，若 i>=c 则 dp[i] = min(dp[i], dp[i-c]+1)。最后 dp[amount] 若仍为初值（无穷）则 -1。
#
# ---------- 关键点 ----------
# · dp[i] 表示凑成金额 i 最少需要几枚硬币。凑 i 时，最后一枚可以是任意一种面额 c（只要 c<=i），用了 c 之后还要凑 i-c，所以 dp[i]=min{ dp[i-c]+1 }  over 所有面额 c。dp[0]=0（凑 0 元不需要硬币），其他先设为无穷大，表示暂时凑不出；若最后 dp[amount] 还是无穷，就返回 -1。按 i 从 1 到 amount 推，每种硬币可以无限用（完全背包）。

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
