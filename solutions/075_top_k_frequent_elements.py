# 力扣 热题100 · 第75题 前 K 个高频元素
# 链接: https://leetcode.cn/problems/top-k-frequent-elements/
#
# ---------- 思路 ----------
# 题目在问什么：给数组，求出现频次最高的 k 个元素，顺序不限。
#
# 做法：先遍历一遍用哈希表统计每个数出现次数。再用大小为 k 的小根堆，堆里按频次排序，存 (频次, 数)。遍历频次表，堆不满就入堆；满了则若当前频次大于堆顶就弹出堆顶再入堆。最后堆里 k 个就是答案。
#
# ---------- 关键点 ----------
# · 先遍历一遍数组，用哈希表统计每个数出现几次。然后问题变成：在「(数, 频次)」这些对里，找频次最高的 k 个。和 74 题类似，用大小为 k 的小根堆，但比较的是频次：堆里存 (频次, 数)，堆顶是频次最小的那个。遍历每个 (数, 频次) 时，若堆未满就入堆；满了且当前频次比堆顶大，就弹出堆顶、当前入堆。最后堆里就是频次最高的 k 个数（堆里存的是 (c, num)，取出 num 即可）。

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        h = []
        for num, c in cnt.items():
            heapq.heappush(h, (c, num))
            if len(h) > k:
                heapq.heappop(h)
        return [num for _, num in h]
