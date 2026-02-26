# 力扣 热题100 · 第78题 跳跃游戏
# 链接: https://leetcode.cn/problems/jump-game/
#
# ---------- 思路 ----------
# 题目在问什么：站在位置 i 最多可跳 nums[i] 步，问能否从下标 0 跳到最后一个下标。
#
# 做法：贪心。维护「当前能到达的最远下标」far。从 0 开始遍历，若 i>far 说明到不了 i，直接 False；否则用 i+nums[i] 更新 far。若某时刻 far>=n-1 则 True。
#
# ---------- 关键点 ----------
# · 关键观察：如果能到达位置 i，那 0～i 之间每一个位置都能到达（因为可以从 0 一步步走到 i）。所以我们不用关心「具体站在哪」，只关心「从 0 出发，最远能到哪个下标」far。从左到右遍历，若当前 i 已经大于 far，说明 i 到不了，后面更到不了，直接返回 False；否则从 i 可以跳最多 nums[i] 步，用 i+nums[i] 更新 far。若某时刻 far>=n-1 就说明能到终点。

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i in range(len(nums)):
            if i > far:
                return False
            far = max(far, i + nums[i])
        return True
