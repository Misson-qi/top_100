# 力扣 热题100 · 第74题 数组中的第K个最大元素
# 链接: https://leetcode.cn/problems/kth-largest-element-in-an-array/
#
# ---------- 思路 ----------
# 题目在问什么：未排序数组，找第 k 大的元素（不是第 k 个下标）。
#
# 做法：用大小为 k 的小根堆。遍历数组，堆不满就入堆；满了则若当前数大于堆顶就弹出堆顶再入堆。这样堆里保留的是目前最大的 k 个，堆顶是最小的那个即第 k 大。
#
# ---------- 关键点 ----------
# · 第 k 大 = 把所有数从大到小排，排第 k 个的那个。我们不需要排整个数组，只要「维护最大的 k 个数」就行：用一个小根堆（堆顶是堆里最小的），堆里最多放 k 个。遍历每个数时，若堆还没满就直接入堆；若满了且当前数比堆顶大，说明堆顶那个肯定进不了「前 k 大」，就弹出堆顶、把当前数入堆。这样扫完后，堆里就是全局最大的 k 个数，堆顶是其中最小的，也就是第 k 大。

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k:
                heapq.heappop(h)
        return h[0]
