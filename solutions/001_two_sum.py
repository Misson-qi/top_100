# 力扣 热题100 · 第1题 两数之和
# 链接: https://leetcode.cn/problems/two-sum/
#
# ---------- 思路 ----------
# 题目在问什么：从数组里找「两个数」，使它们的和等于 target，返回这两个数的下标（不能重复用同一个数）。
#
# 暴力做法：用两层循环枚举所有数对 (i, j)，看 nums[i] + nums[j] 是否等于 target。
# 这样要试很多对，时间复杂度 O(n^2)，太慢。
#
# 更好做法：只扫一遍数组。扫到每个数 x 时，心里想「我还需要另一个数 = target - x」。
# 如果这个「需要的数」在之前已经出现过，那它和当前的 x 就是答案；
# 否则把「当前数 x 和它的下标」记下来，继续往后扫。
# 用字典（哈希表）来记「见过的数 → 当时的下标」，这样每次查「target - x 有没有见过」只要 O(1)。
#
# ---------- 关键点 ----------
# · 一定要「先查 need、再把当前数放进字典」。因为题目要求不能重复用同一个数。若先存再查，当 target 正好是两倍当前数（比如 target=6、当前是 3）时，need 也是 3，就会查到刚存进去的自己，得到两个相同下标。先查再存，就能保证查到的 need 一定是「在当前数之前」出现过的另一个位置。
# · 为什么扫一遍就够？答案里的两个数在数组里一定一前一后。先被扫到的会先进字典；后扫到的那一个在算 need=target-自己 时，一定能从字典里查到先出现的那个，所以一次遍历就能找到这一对。
# · 字典存的是「数值 → 下标」：我们要的是「target-x 有没有出现过、在哪个位置」，所以用数值当 key、下标当 value。这样扫到 x 时，一查 need=target-x 就能知道有没有、在哪。

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []
