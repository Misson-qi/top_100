# 力扣 热题100 · 第16题 除了自身以外数组的乘积
# 链接: https://leetcode.cn/problems/product-of-array-except-self/
#
# ---------- 思路 ----------
# 题目在问什么：输出一个数组，第 i 个位置 = 原数组除了第 i 个以外所有数的乘积。要求不用除法、O(n)、空间尽量 O(1)（不算输出）。
#
# 做法：output[i] = （i 左边所有数乘积）×（i 右边所有数乘积）。先从左到右扫一遍，在 ans[i] 里存「左侧乘积」；再从右到左扫，用一个变量 r 累乘右边的数，每次 ans[i] *= r。这样就不需要额外开左右两个数组。
#
# ---------- 关键点 ----------
# · 不用除法时，output[i] 只能拆成「i 左边所有数的乘积」×「i 右边所有数的乘积」。第一趟从左到右：ans[i] = ans[i-1]*nums[i-1]，得到每个位置左边的乘积。第二趟从右到左：用变量 r 表示「当前下标右边」的乘积，每到一个 i 先 ans[i]*=r（把右边乘上去），再 r*=nums[i]（把当前数纳入「右边」）。这样第二趟只用一个变量，满足 O(1) 额外空间。
# · 第二趟必须从右往左：r 从 1 开始，到最右边时乘的是「右边没有数」的乘积 1；然后 r 不断乘上 nums[i]，往左走时 r 就是「当前 i 的右边所有数的乘积」。从左往右的话没法用同一个 r 表示「当前右边」。

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        r = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]
        return ans
