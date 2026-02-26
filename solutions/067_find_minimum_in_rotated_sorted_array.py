# 力扣 热题100 · 第67题 寻找旋转排序数组中的最小值
# 链接: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
#
# ---------- 思路 ----------
# 题目在问什么：旋转过的升序数组（无重复），求最小元素。
#
# 做法：二分。和右端点比：若 nums[mid] > nums[hi]，说明最小值在右半段（mid 在左半段大数里），lo=mid+1；否则最小值在左半段含 mid，hi=mid。最后 lo 或 hi 指向最小值。
#
# ---------- 关键点 ----------
# · 旋转后最小值在「后半段」的开头。我们和右端点 nums[hi] 比较：若 nums[mid] > nums[hi]，说明 mid 还在「前半段大数」里，最小值一定在 mid 右边，所以 lo=mid+1；若 nums[mid] <= nums[hi]，说明 mid 已经在「后半段」里了，最小值在 mid 左边或就是 mid，所以 hi=mid（不能 hi=mid-1，因为 mid 可能是最小）。循环用 lo<hi，退出时 lo==hi，指向的就是最小元素的下标。

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
