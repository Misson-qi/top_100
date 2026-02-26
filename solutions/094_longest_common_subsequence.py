# 力扣 热题100 · 第94题 最长公共子序列
# 链接: https://leetcode.cn/problems/longest-common-subsequence/
#
# ---------- 思路 ----------
# 题目在问什么：两个字符串，找最长公共子序列（不要求连续）的长度。
#
# 做法：dp[i][j] = text1 前 i 个与 text2 前 j 个的 LCS 长度。若 text1[i-1]==text2[j-1]，可匹配，dp[i][j]=dp[i-1][j-1]+1；否则 dp[i][j]=max(dp[i-1][j], dp[i][j-1])（舍掉 text1 最后一个或 text2 最后一个）。
#
# ---------- 关键点 ----------
# · dp[i][j] 表示 text1 的前 i 个字符和 text2 的前 j 个字符的 LCS 长度。若 text1 的第 i 个和 text2 的第 j 个相等，可以一起匹配，长度就是 dp[i-1][j-1]+1。若不等，这两个里至少有一个不能参与匹配：要么忽略 text1 的最后一个（看 dp[i-1][j]），要么忽略 text2 的最后一个（看 dp[i][j-1]），取两者较大值。dp[0][j] 和 dp[i][0] 表示有一个串是空的，LCS 长度为 0。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
