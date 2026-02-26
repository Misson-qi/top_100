# 力扣 热题100 · 第93题 最长回文子串
# 链接: https://leetcode.cn/problems/longest-palindromic-substring/
#
# ---------- 思路 ----------
# 题目在问什么：找字符串里最长的回文子串（连续）。
#
# 做法：中心扩展。枚举每个「中心」（可以是单个字符或两个字符之间），向左右扩展直到两边字符不等，记录能扩到的长度和起点，更新最长的那段。
#
# ---------- 关键点 ----------
# · 回文串有两种：奇数长度（如 "aba"）和偶数长度（如 "abba"）。奇数长度的有一个正中间的字符；偶数长度的「中心」在两个字符之间。所以我们枚举两种中心：以每个下标 i 为中心（奇数），以及以 i 和 i+1 之间为中心（偶数）。对每个中心，用两个指针 l、r 向两边扩展，只要 s[l]==s[r] 就继续扩，记录能扩到的最长长度和对应的起点。最后根据「最长的是以谁为中心、长度多少」截取子串返回。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        def expand(l: int, r: int) -> int:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = max_len = 0
        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i + 1)
            cur = max(odd, even)
            if cur > max_len:
                max_len = cur
                start = i - (cur - 1) // 2
        return s[start : start + max_len]
