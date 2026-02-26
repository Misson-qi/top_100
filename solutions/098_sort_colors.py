# 力扣 热题100 · 第98题 颜色分类
# 链接: https://leetcode.cn/problems/sort-colors/
#
# ---------- 思路 ----------
# 题目在问什么：数组只有 0、1、2，原地按 0、1、2 顺序排好（荷兰国旗）。
#
# 做法：三个指针。p0 表示 0 的右边界（下一个 0 该放的位置），p2 表示 2 的左边界，i 从左扫到 p2。遇到 0 和 p0 交换、p0++、i++；遇到 2 和 p2 交换、p2--（i 不增，因为换过来的可能是 0 或 2）；遇到 1 只 i++。最后 0 在左、2 在右、1 在中间。
#
# ---------- 关键点 ----------
# · 用三个指针：p0 表示「0 的右边界」即下一个 0 该放的位置；p2 表示「2 的左边界」即下一个 2 该放的位置；i 从左往右扫。遇到 0 就与 p0 位置交换，p0 右移，i 也右移（因为换到 i 位置的一般是 1，已经合格）。遇到 2 就与 p2 位置交换，p2 左移，但 i 不要动：因为换到 i 位置的可能是 0 或 2，需要下一轮再判断一次。遇到 1 就只 i++。循环到 i 超过 p2 为止（p2 右边已经全是 2）。

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, p2, i = 0, len(nums) - 1, 0
        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            else:
                i += 1
