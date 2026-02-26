# 力扣 热题100 · 第79题 跳跃游戏 II
# 链接: https://leetcode.cn/problems/jump-game-ii/
#
# ---------- 思路 ----------
# 题目在问什么：同 78 题，但保证能到达，求最少跳数。
#
# 做法：贪心。用 cur_end 表示「当前这一步」能到的右边界，cur_far 表示「下一步」能到的最远位置。遍历时用 i+nums[i] 更新 cur_far；当 i 到达 cur_end 时说明这一步走完了，步数 +1，cur_end 更新为 cur_far（下一步能到的范围）。
#
# ---------- 关键点 ----------
# · 贪心：每一步都在「当前步能到的范围」里选一个位置起跳，跳到「下一步能到的最远」的位置。用 cur_end 表示「当前这一步能到达的最右下标」，cur_far 表示「从当前步范围内起跳，下一步能到的最远下标」。遍历 i 时，用 i+nums[i] 更新 cur_far；当 i 走到 cur_end 时，说明这一步能到的都看完了，必须跳了，步数+1，并把 cur_end 更新为 cur_far（下一步能到的范围）。若更新后 cur_far>=n-1，说明再跳一步就到终点了，直接返回步数。

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        steps = cur_end = cur_far = 0
        for i in range(n):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                steps += 1
                if cur_far >= n - 1:
                    return steps
                cur_end = cur_far
        return steps
