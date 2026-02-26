# 力扣 热题100 · 第73题 柱状图中最大的矩形
# 链接: https://leetcode.cn/problems/largest-rectangle-in-histogram/
#
# ---------- 思路 ----------
# 题目在问什么：一排柱子，求能围成的最大矩形面积（矩形高为某根柱子高，宽为向左右延伸到比它矮或边界）。
#
# 做法：对每根柱子，找「左边第一个比它矮」和「右边第一个比它矮」的下标，则以该柱为高的矩形宽 = right-left-1。用单调递增栈：当前比栈顶矮时，栈顶的「右边界」就是当前下标，左边界是新的栈顶（或 -1），出栈算面积。
#
# ---------- 关键点 ----------
# · 单调栈在维护什么：栈里是「还没确定右边界」的下标，且这些下标对应的高度从栈底到栈顶单调递增。当遇到一个比栈顶矮的 h[i] 时，栈顶这根柱子「右边第一个比它矮」的就是 i，右边界确定了；左边界是「栈里它下面的那个下标」再往右一个（即新栈顶+1），因为栈内递增，新栈顶是左边第一个比它矮的。所以宽 = (i-1) - (新栈顶+1) + 1 = i - 新栈顶 - 1。
# · 为什么头尾加 0：头部加 0 可以让「原数组第一个元素」出栈时，新栈顶是哨兵 0（下标 0），宽 = i - 0 - 1 正确。尾部加 0 可以保证原数组最后一个元素也会在最后被「当前高度 0」触发出栈并算面积，否则栈里会剩一截没算。
# · 出栈时「左边界」是 st[-1]（弹出后的新栈顶），不是 mid：以 mid 为高的矩形，左边界是「左边第一个比 heights[mid] 矮」的位置，即新栈顶的下一个位置，所以左界下标 = left + 1，右界下标 = i - 1，宽 = (i-1)-(left+1)+1 = i - left - 1。

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        st = []
        ans = 0
        for i, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                mid = st.pop()
                left = st[-1]
                ans = max(ans, (i - left - 1) * heights[mid])
            st.append(i)
        return ans
