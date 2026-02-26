# 力扣 热题100 · 第9题 找到字符串中所有字母异位词
# 链接: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
#
# ---------- 思路 ----------
# 题目在问什么：在字符串 s 里找所有「和 p 是异位词」的连续子串的起始下标（异位词 = 字母相同、顺序可以不同）。
#
# 做法：用长度 26 的数组统计 p 里每个字母出现几次，得到目标 cnt_p。在 s 上用一个长度等于 len(p) 的滑动窗口，用数组 cnt 统计窗口内每个字母的次数。窗口每次右移一格：新进来一个字符就 +1，出去一个就 -1。每次移动后比较 cnt 和 cnt_p 是否完全一样，一样就说明窗口这一段是 p 的异位词，记录窗口起点。
#
# ---------- 关键点 ----------
# · 异位词 = 字母种类一样、每个字母出现次数也一样。窗口长度又等于 len(p)，所以只要窗口里 26 个字母的计数和 p 的计数完全一样，这段就是 p 的异位词。用两个长度 26 的数组分别存 p 的计数和当前窗口的计数，比较是否相等即可。
# · 窗口长度固定，每次右移一格：右边进来一个字符就给它对应的计数 +1，左边出去一个就 -1。这样不用每次重新数整个窗口，O(1) 就能更新。
# · 先单独建好第一个窗口 [0, m-1] 的计数，若和 p 一样就记录起点 0；然后从 i=m 开始，每次把 s[i] 加进、s[i-m] 去掉，再比较并记录起点 i-m+1。这样每个可能的起点都恰好考虑一次。

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        cnt_p = [0] * 26
        for c in p:
            cnt_p[ord(c) - 97] += 1
        cnt = [0] * 26
        for i in range(m):
            cnt[ord(s[i]) - 97] += 1
        ans = []
        if cnt == cnt_p:
            ans.append(0)
        for i in range(m, n):
            cnt[ord(s[i]) - 97] += 1
            cnt[ord(s[i - m]) - 97] -= 1
            if cnt == cnt_p:
                ans.append(i - m + 1)
        return ans
