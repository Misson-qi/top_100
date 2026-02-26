# 力扣 热题100 · 第97题 多数元素
# 链接: https://leetcode.cn/problems/majority-element/
#
# ---------- 思路 ----------
# 题目在问什么：数组里有一个数出现次数超过一半，找这个数。保证存在。
#
# 做法：Boyer-Moore 投票。维护「当前候选」和「计数」。遍历时若和候选相同则计数+1，否则-1；计数变 0 时换当前数为候选、计数置 1。因为多数超过一半，最后剩下的候选一定是多数。
#
# ---------- 关键点 ----------
# · 投票法：想象多数派和其他人两两抵消。维护一个「候选」和「计数」：遇到和候选相同的数，计数+1（同伙）；遇到不同的，计数-1（抵消）。当计数变成 0，说明前面这一段「势均力敌」，可以丢掉不管，从当前数重新开始选候选、计数置 1。因为多数元素超过一半，怎么抵消最后都会剩下多数那一方，所以遍历结束时的候选就是多数元素。

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        cnt = 0
        for x in nums:
            if cnt == 0:
                cand = x
            cnt += 1 if x == cand else -1
        return cand
