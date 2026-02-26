# 力扣 热题100 · 第86题 单词拆分
# 链接: https://leetcode.cn/problems/word-break/
#
# ---------- 思路 ----------
# 题目在问什么：字符串 s 能否由字典里的单词拼接而成（可重复用）。
#
# 做法：dp[i] 表示 s 的前 i 个字符能否被拼出。dp[0]=True；对每个 i，枚举 j<i，若 dp[j] 为真且 s[j:i] 在字典里则 dp[i]=True。最后看 dp[n]。
#
# ---------- 关键点 ----------
# · dp[i] 表示「s 的前 i 个字符（s[0:i]）能否由字典里的单词拼成」。考虑最后一段单词：若最后一段是 s[j:i]（即从位置 j 到 i），那么只要「前 j 个能拼成」（dp[j] 为 True）且「s[j:i] 在字典里」，前 i 个就能拼成。所以对每个 i，枚举 j 从 0 到 i-1，看有没有这样的 j。字典转成 set 可以 O(1) 判断 s[j:i] 是否在字典里。

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in w:
                    dp[i] = True
                    break
        return dp[n]
