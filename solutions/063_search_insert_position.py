# 力扣 热题100 · 第63题 搜索插入位置
# 链接: https://leetcode.cn/problems/search-insert-position/
#
# ---------- 思路 ----------
# 题目在问什么：有序数组里找 target，找到返回下标，找不到返回若插入应放的下标。
#
# 做法：二分找「第一个 >= target 的位置」。若 nums[mid]<target 说明答案在右边，lo=mid+1；否则 hi=mid。最后 lo 就是第一个 >= target 的下标，正好是插入位置。
#
# ---------- 关键点 ----------
# · 题目本质是：在有序数组里找「第一个大于等于 target 的位置」。如果 target 在数组里，这个位置就是 target 的下标；如果 target 不在，这个位置就是「如果插入 target 应该放的位置」（因为插入后要保持有序，就要放在第一个 >= target 的位置）。用二分：若 nums[mid]<target 说明答案在右边，lo=mid+1；否则答案在 mid 或左边，hi=mid。区间用左闭右开 [lo, hi)，初始 hi=len(nums)，这样最后 lo 可能是 len(nums)，表示插在末尾。

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
