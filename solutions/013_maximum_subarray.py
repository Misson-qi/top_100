# 力扣 热题100 · 第13题 最大子数组和
# 链接: https://leetcode.cn/problems/maximum-subarray/
#
# ---------- 思路 ----------
# 题目在问什么：找一个连续子数组，使其元素和最大。
#
# 做法：想象从左往右扫。到每个位置 i，「以 i 结尾」的最大子数组和只有两种可能：要么只取 nums[i]，要么接上「以 i-1 结尾」的最大和（若前面那段和是正的，接上更划算）。所以 cur = max(nums[i], cur + nums[i])，再用 cur 更新全局答案。这样扫一遍就得到答案。
#
# ---------- 关键点 ----------
# · 以位置 i 结尾的最大子数组和只有两种可能：要么只选 nums[i] 一个数，要么接在「以 i-1 结尾的某段」后面。而以 i-1 结尾的最优就是上一轮的 cur，所以 cur = max(nums[i], cur+nums[i])。若上一轮 cur 已经 ≤0，接上它只会让和变小或不变，不如从 nums[i] 重新开始。
# · 每步用 cur 更新全局答案 ans。扫完一遍，ans 就是所有「以某位置结尾」的最大和里的最大值，也就是题目要的。

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            ans = max(ans, cur)
        return ans
