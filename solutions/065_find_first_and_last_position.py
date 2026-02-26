# 力扣 热题100 · 第65题 在排序数组中查找元素的第一个和最后一个位置
# 链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# ---------- 思路 ----------
# 题目在问什么：非降序数组里 target 可能出现多次，求第一次和最后一次的下标；没有则 [-1,-1]。
#
# 做法：二分两次。第一次找「第一个 >= target」的下标 left；第二次找「第一个 > target」的下标 right，则最后一个等于 target 的是 right-1。若 left 没越界且 nums[left]==target，答案为 [left, right-1]，否则 [-1,-1]。
#
# ---------- 关键点 ----------
# · 第一次二分：找「第一个 >= target」的下标，记为 left。若 nums[left]!=target 或 left 已经越界，说明数组里没有 target，直接返回 [-1,-1]。
# · 第二次二分：找「第一个 > target」的下标（可以复用同一个函数，传入 target+1）。这个下标减 1 就是「最后一个等于 target」的位置。所以答案就是 [left, 第一次 >= target+1 的下标 - 1]。这样两次二分就能精确找到 target 的起止位置。

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_ge(t: int) -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        left = first_ge(target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = first_ge(target + 1) - 1
        return [left, right]
