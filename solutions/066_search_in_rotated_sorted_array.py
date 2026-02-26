# 力扣 热题100 · 第66题 搜索旋转排序数组
# 链接: https://leetcode.cn/problems/search-in-rotated-sorted-array/
#
# ---------- 思路 ----------
# 题目在问什么：数组是「升序旋转变形」（如 [4,5,6,0,1,2]），无重复，找 target 的下标。
#
# 做法：二分时，mid 两侧必有一侧是严格有序的。若 nums[lo]<=nums[mid]，左半有序，看 target 是否在 [lo,mid] 内，在则 hi=mid-1 否则 lo=mid+1；否则右半有序，看 target 是否在 [mid,hi] 内。每次都能缩小一半。
#
# ---------- 关键点 ----------
# · 旋转数组长这样：前面一段是较大的数且升序，后面一段是较小的数且升序，比如 [4,5,6,0,1,2]。二分时取 mid，mid 要么在「前半段大数」里，要么在「后半段小数」里。关键性质：mid 的左边和右边，一定有一边是「连续升序」的。若 nums[lo]<=nums[mid]，说明左半段 [lo,mid] 是升序的；否则右半段 [mid,hi] 是升序的。我们看 target 是否落在有序的那一段里（比左端大且比右端小），在的话就在这一段里继续二分，不在的话就去另一段找。这样每次都能排除一半。

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
