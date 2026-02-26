# 力扣 热题100 · 第95题 编辑距离
# 链接: https://leetcode.cn/problems/edit-distance/
#
# ---------- 思路 ----------
# 题目在问什么：把 word1 通过最少次「插入、删除、替换」变成 word2，求最少次数。
#
# 做法：dp[i][j] = word1 前 i 个变成 word2 前 j 个的最少操作。若 word1[i-1]==word2[j-1]，dp[i][j]=dp[i-1][j-1]；否则三种选择：替换 dp[i-1][j-1]+1、删 word1 最后一个 dp[i-1][j]+1、插一个 dp[i][j-1]+1，取最小。边界 dp[i][0]=i，dp[0][j]=j。
#
# ---------- 关键点 ----------
# · dp[i][j] 表示把 word1 的前 i 个字符变成 word2 的前 j 个字符，最少需要几次操作。若 word1 的第 i 个和 word2 的第 j 个相同，不用动，dp[i][j]=dp[i-1][j-1]。若不同，有三种选择：① 把 word1 的最后一个替换成 word2 的最后一个，dp[i-1][j-1]+1；② 删掉 word1 的最后一个，dp[i-1][j]+1；③ 在 word1 末尾插入 word2 的最后一个（等价于 word2 少看一个），dp[i][j-1]+1。取三者最小。边界：word1 前 i 个变空串要删 i 次，空串变 word2 前 j 个要插 j 次。

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
