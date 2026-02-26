# 力扣 热题100 · 第80题 划分字母区间
# 链接: https://leetcode.cn/problems/partition-labels/
#
# ---------- 思路 ----------
# 题目在问什么：把字符串切成若干段，每段里每个字母至多出现在这一段（同一字母不能跨段）。求每段长度的列表。
#
# 做法：先扫一遍记下每个字母最后一次出现的下标。再扫一遍，用 right 表示「当前段」至少要延伸到哪（已出现过的字母的最后位置的最大值）。当 i==right 时说明当前段可以截断，记录长度，下一段从 i+1 开始。
#
# ---------- 关键点 ----------
# · 要求：同一个字母只能出现在一段里，不能前半段有一个 'a'、后半段又有一个 'a'。所以一旦某段里出现了字母 'a'，这一段至少要延伸到 'a' 最后一次出现的位置。换句话说，当前段的右边界 >= 这段里出现过的每个字母的「最后出现位置」。
# · 做法：先扫一遍字符串，记下每个字母最后一次出现的下标 last[c]。再扫一遍，用 left 表示当前段的起点，right 表示「当前段至少要延伸到的位置」。每看到一个字母 c，就把 right 更新为 max(right, last[c])。当 i==right 时，说明从 left 到 right 这一段里出现过的所有字母，都不会出现在 right 之后了，可以在这里截断；记下长度 right-left+1，下一段从 right+1 开始。

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        ans = []
        left = right = 0
        for i, c in enumerate(s):
            right = max(right, last[c])
            if i == right:
                ans.append(right - left + 1)
                left = right + 1
        return ans
