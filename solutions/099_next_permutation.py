# 力扣 热题100 · 第99题 下一个排列
# 链接: https://leetcode.cn/problems/next-permutation/
#
# ---------- 思路 ----------
# 题目在问什么：把数组改成「字典序下一个更大的排列」；若已是最大则改成最小（整体反转）。
#
# 做法：从右往左找第一个「升序」位置 i（即 nums[i] < nums[i+1]）。若没有说明整个是降序，已是最大，整体反转。否则从右往左找第一个大于 nums[i] 的 nums[j]，交换 nums[i] 和 nums[j]，再把 [i+1:] 反转（使这一段变成最小字典序）。
#
# ---------- 关键点 ----------
# · 「下一个排列」要比当前大、且尽可能小。从右往左找第一个满足 nums[i]<nums[i+1] 的 i，说明从 i+1 往右是降序（这一段已经是能组成的最大排列）。我们要把 nums[i] 换成「比它大的数里最小的那个」：从右往左找第一个 nums[j]>nums[i]，交换 i 和 j。交换后 [i+1:] 仍是降序，把它反转成升序，就得到这一段的最小排列，整体就是「刚好比原来大一点」的下一个排列。若找不到这样的 i，说明整个数组降序，已经是最大排列，题目要求此时改成最小排列，即整体反转。

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
