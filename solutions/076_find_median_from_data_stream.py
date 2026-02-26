# 力扣 热题100 · 第76题 数据流的中位数
# 链接: https://leetcode.cn/problems/find-median-from-data-stream/
#
# ---------- 思路 ----------
# 题目在问什么：不断加入数字，随时询问当前中位数（偶数为两中间数平均）。
#
# 做法：用大根堆存「左半部分」、小根堆存「右半部分」，保持左半个数 >= 右半且最多多 1。add 时先放进左堆，再把左堆顶挪到右堆，若右堆多了再挪一个回左堆。取中位数：若左多则左堆顶，否则两堆顶平均。
#
# ---------- 关键点 ----------
# · 中位数 = 排序后中间那个（或中间两个的平均）。我们把「较小的一半」放在大根堆里、「较大的一半」放在小根堆里，并保持左半个数比右半多 0 或 1。这样左堆顶是「左半里最大的」、右堆顶是「右半里最小的」，它们正好围住中间，中位数就是左堆顶（总数为奇）或两堆顶的平均（总数为偶）。
# · 每次 add(num)：先放进左堆（大根堆），再把左堆顶挪到右堆，这样相当于把「当前最大」的左边元素挪到右边；若此时右堆比左堆多，就再挪一个从右堆回左堆，保证左>=右且最多多 1。Python 的 heapq 是小根堆，要模拟大根堆就存负数，取的时候再取负。

import heapq


class MedianFinder:
    def __init__(self):
        self.lo = []   # 大根堆，存负值
        self.hi = []   # 小根堆

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0
