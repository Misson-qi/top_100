# 力扣 热题100 · 第84题 完全平方数
# 链接: https://leetcode.cn/problems/perfect-squares/
#
# ---------- 思路 ----------
# 题目在问什么：用最少的完全平方数（1,4,9,...）凑出 n，求最少个数。
#
# 做法：dp[i] 表示凑出 i 的最少个数。dp[0]=0；对 i>=1，枚举最后一个用的平方数 j*j，dp[i] = min(dp[i - j*j] + 1)。j 从 1 到 sqrt(i)。
#
# ---------- 关键点 ----------
# · dp[i] 表示「凑出数 i 最少要用几个完全平方数」。凑 i 时，最后一步用的可以是 1、4、9、……直到不超过 i 的平方数。若最后一步用了 j*j，那前面就要凑 i-j*j，用的个数就是 dp[i-j*j]+1。所以 dp[i]=min{ dp[i-j*j]+1 }，j 从 1 到 sqrt(i)。dp[0]=0（凑 0 不需要任何数）。

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
