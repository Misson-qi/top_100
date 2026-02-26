# 力扣 热题100 · 第6题 三数之和
# 链接: https://leetcode.cn/problems/3sum/
#
# ---------- 思路 ----------
# 题目在问什么：在数组里找所有「三个数之和为 0」的不重复三元组。
#
# 做法：先排序。枚举第一个数 nums[i]，问题变成在 i 右边找两个数，使两数之和 = -nums[i]（即两数之和的经典双指针）。对每个 i，用左右指针 l、r 在 [i+1, n-1] 上向中间夹，和大了就 r--，和小了就 l++。去重：枚举 i 时若 nums[i]==nums[i-1] 就跳过；找到一组 (i,l,r) 后，把 l、r 移到和当前值不同的位置再继续。
#
# ---------- 关键点 ----------
# · 先排序有两个好处：一是后面区间 [i+1, n-1] 有序，才能用双指针在 O(n) 里找「两数之和」；二是相同的数会挨在一起，去重时只要和「前一个」比较就行，避免重复的三元组。
# · 去重要做在三处：① 枚举第一个数时，如果 nums[i]==nums[i-1] 就跳过，否则会多组「第一个数相同、后两个也相同」的解。② 找到一组 (l,r) 之后，要把 l 和 r 分别移到「和当前值不一样」的位置再继续，否则下一轮还会得到同样的 (nums[l], nums[r])，产生重复。③ 双指针的 l 从 i+1、r 从 n-1 开始，保证三个下标严格 i<l<r，不会用到同一个位置。

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                continue
            t = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < t:
                    l += 1
                elif s > t:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans
