# 力扣 热题100 · 第12题 最小覆盖子串
# 链接: https://leetcode.cn/problems/minimum-window-substring/
#
# ---------- 思路 ----------
# 题目在问什么：在 s 里找一个最短的连续子串，使得这个子串里包含 t 中的每个字符（数量不少于 t 里的次数）。
#
# 做法：滑动窗口。用 need 记录 t 里每个字符还「差几个」才满足；cnt 表示还有几种字符没满足（当 need[c] 从正变 0 时 cnt--）。right 往右扩，遇到 t 里的字符就 need[c]--，当 cnt==0 时说明当前窗口已经包含 t；然后 left 往右缩，每缩一步看是否还包含 t（need 变正时 cnt++），不包含前记录一下窗口长度和起点。最后取记录过的最短的那段。
#
# ---------- 关键点 ----------
# · need[c] 表示：要「包含 t」的话，窗口里还差几个 c（初始等于 t 里 c 的个数）。窗口多一个 c 就 need[c]--，左边界缩掉一个 c 就 need[c]++。cnt 表示「还有几种字符没满足」：某字符从差几个变成差 0 个时 cnt--，从 0 变回正时 cnt++。这样 cnt==0 就说明窗口已经包含 t 里所有字符且数量不少于 t。
# · 对每个右端点 right，先右扩直到窗口包含 t，再左缩直到刚好不包含；缩之前的那一瞬间 [left, right] 就是以 right 结尾的最短合法子串，记下长度和起点。这样枚举了每个右端点，不会漏掉真正的最短窗。
# · 左缩时：只有 need[c] 从 0 变成正数时才 cnt++（从「满足」变「不满足」）。若 need[c] 本来是负的（窗里这个字符多了），左缩一个只是 need[c]++，不会从 0 变 1，不用 cnt++。

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        cnt = len(need)
        left = 0
        min_len, start = float("inf"), 0
        for right, c in enumerate(s):
            if c in need:
                need[c] -= 1
                if need[c] == 0:
                    cnt -= 1
            while cnt == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                c0 = s[left]
                if c0 in need:
                    need[c0] += 1
                    if need[c0] == 1:
                        cnt += 1
                left += 1
        return s[start : start + min_len] if min_len != float("inf") else ""
