# 力扣 热题100 · 第7题 接雨水
# 链接: https://leetcode.cn/problems/trapping-rain-water/
#
# ---------- 思路 ----------
# 题目在问什么：一排柱子，凹下去的地方能接雨水，求总共能接多少。每个位置能接的水 = min(左边最高, 右边最高) - 当前高度（若为负则算 0）。
#
# 做法：双指针从两端往中间走，维护 left_max（i 左边见过的最高）、right_max（j 右边见过的最高）。哪边的 max 小就说明该侧是「短板」，先结算该侧当前位置能接的水（用这一侧的 max 减当前高度），然后该侧指针往中间移并更新 max。这样不用预先把每个位置左右最大都算出来，一遍扫完 O(n) O(1)。
#
# ---------- 关键点 ----------
# · 每个位置能接的水 = min(左边最高, 右边最高) - 当前高度。我们每次只结算「left_max 和 right_max 里更小」的那一侧（比如 left_max 小就结算 i 位置）。为什么可以？因为另一边的指针还没动，那边已经有一个真实柱子的高度 ≥ right_max，所以「另一边至少有这么高」是成立的，用矮的那边当挡板来算水，不会多算也不会少算。
# · 每个位置都会被算到一次：每个位置总会在「它属于较矮那一侧」时被指针扫到并结算。所以不会漏。
# · 顺序：先用水量公式算当前格、再移动指针、再更新这一侧的 max。这样更新的是「新位置」对应的左侧/右侧最高，逻辑才对。更新时可能已经 i>j，所以用 if i<=j 再更新另一侧的 max，避免越界。

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i, j = 0, len(height) - 1
        left_max, right_max = height[i], height[j]
        ans = 0
        while i < j:
            if left_max <= right_max:
                ans += left_max - height[i]
                i += 1
                if i <= j:
                    left_max = max(left_max, height[i])
            else:
                ans += right_max - height[j]
                j -= 1
                if i <= j:
                    right_max = max(right_max, height[j])
        return ans
