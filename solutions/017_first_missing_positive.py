# 力扣 热题100 · 第17题 缺失的第一个正数
# 链接: https://leetcode.cn/problems/first-missing-positive/
#
# ---------- 思路 ----------
# 题目在问什么：未排序的数组里，找「最小的没出现过的正整数」。要求 O(n) 时间、O(1) 空间。
#
# 做法：利用「若有 1~n 的数，它们应该在下标 0~n-1 各占一个位置」：若 1<=nums[i]<=n，就把 nums[i] 换到下标 nums[i]-1 的位置（换到「属于它的位置」）。换完再扫一遍，第一个满足 nums[i] != i+1 的位置 i，答案就是 i+1；若都满足说明 1~n 都在，答案是 n+1。
#
# ---------- 关键点 ----------
# · 想法：若 1 到 n 都出现过，我们可以让它们「各就各位」——数值 x 放在下标 x-1。放完后若有 nums[i]!=i+1，说明 i+1 没出现；若都满足说明 1~n 都在，答案就是 n+1。这样把「找缺失的正数」变成「找谁没坐在自己的座位上」。
# · 用 while 而不是 if：把 nums[i] 换到下标 nums[i]-1 后，换到 i 位置上的可能是别的 1~n 的数，它也可能不在自己的位置上，要继续换，直到 i 上放的是「不在 1~n 的」或「已经在正确位置的」为止。只换一次会漏掉「链式」的调整。
# · 条件里要写 nums[nums[i]-1] != nums[i]：若相等说明要去的那个位置已经是同一个数（重复），再换会死循环，所以跳过。答案一定在 1~n+1 之间：只有 n 个位置，最多放下 1~n，缺的最小正数要么是 1~n 里某个，要么是 n+1。

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
