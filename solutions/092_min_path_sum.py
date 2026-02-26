# 力扣 热题100 · 第92题 最小路径和
# 链接: https://leetcode.cn/problems/minimum-path-sum/
#
# ---------- 思路 ----------
# 题目在问什么：网格从左上到右下，只能向右或向下，经过的格子数字求和，求最小和。
#
# 做法：dp[i][j] = 到 (i,j) 的最小和 = grid[i][j] + min(dp[i-1][j], dp[i][j-1])。第一行第一列单独初始化（累加）。可压成一维按行更新。
#
# ---------- 关键点 ----------
# · 到 (i,j) 的最小路径和 = 当前格数字 + min(从上面来的最小和, 从左边来的最小和)，即 grid[i][j]+min(dp[i-1][j], dp[i][j-1])。第一行只能从左边来，第一列只能从上面来，先单独算好。然后按行递推，可以压成一维：dp[j] 在更新前表示「从上面来的最小和」，dp[j-1] 表示「从左面来的最小和」，所以 dp[j]=grid[i][j]+min(dp[j], dp[j-1])。

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [grid[0][0]] + [0] * (n - 1)
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        return dp[-1]
