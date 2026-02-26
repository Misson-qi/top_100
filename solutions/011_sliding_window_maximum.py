# 力扣 热题100 · 第11题 滑动窗口最大值
# 链接: https://leetcode.cn/problems/sliding-window-maximum/
#
# ---------- 思路 ----------
# 题目在问什么：一个数组，一个固定长度 k 的窗口从左滑到右，求每个窗口里的最大值。
#
# 做法：单调队列。队列里存「下标」，且这些下标对应的数值从队首到队尾单调递减（队首就是当前窗口最大值）。新来一个数时，从队尾把比它小的都弹掉再入队（因为它们在后面窗口里不可能再当最大值）。若队首下标已经滑出窗口就出队。从第 k-1 个位置起，每次取队首下标对应的数就是该窗口最大值。
#
# ---------- 关键点 ----------
# · 单调队列里按下标对应的「值」从队首到队尾递减，队首就是当前窗口的最大值。新来一个数 nums[i] 时，从队尾把比它小的都弹掉再入队：因为这些被弹掉的下标要么之后会出窗，要么和 i 在同一窗里——同窗时它们不可能当最大值（nums[i] 更大），所以以后都不会再当最大值，可以删掉。
# · 队列里存的是下标，这样既知道值、又知道什么时候「滑出窗口」。队首下标若 ≤ i-k，说明已经不在当前窗口 [i-k+1, i] 里了，要 popleft。
# · 顺序：先按上面规则把当前 i 入队（维护单调性），再判队首是否出窗、出窗就 popleft，最后若窗口已经至少有 k 个数（i>=k-1）就取队首对应的值作为该窗口最大值。

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
