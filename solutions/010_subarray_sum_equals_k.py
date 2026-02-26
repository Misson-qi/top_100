# 力扣 热题100 · 第10题 和为 K 的子数组
# 链接: https://leetcode.cn/problems/subarray-sum-equals-k/
#
# ---------- 思路 ----------
# 题目在问什么：找有多少个连续子数组，其元素之和等于 k。
#
# 做法：前缀和。若 pre[i] 表示前 i 个数的和，则子数组 [j+1, i] 的和 = pre[i] - pre[j]。要 pre[i]-pre[j]=k 即 pre[j]=pre[i]-k。所以扫一遍，维护当前前缀和 pre，用字典记录「之前出现过的前缀和的值 → 出现次数」，每到一个位置就查 pre-k 出现过几次，累加到答案，再把当前 pre 记进字典。
#
# ---------- 关键点 ----------
# · 子数组 [j+1, i] 的和 = 前 i 个的和 - 前 j 个的和 = pre[i]-pre[j]。要这段和等于 k，就是 pre[j]=pre[i]-k。所以扫到位置 i 时，当前前缀和是 pre，只要看「在 i 之前」有多少个位置的前缀和等于 pre-k，每一个就对应一个以 i 结尾、和为 k 的子数组。用字典 d 记录「某个前缀和值出现了几次」即可。
# · 一开始要 d[0]=1：当某段前缀和正好等于 k 时，pre-k=0，表示「从开头到当前」这一段就是一个合法子数组。如果没有 d[0]=1，这种情况就统计不到。
# · 顺序是「先查 d[pre-k] 加到答案、再把当前 pre 放进 d」：这样字典里存的都是「严格在当前位置之前」的前缀和，不会把当前自己算进去，避免出错。

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        pre = ans = 0
        for x in nums:
            pre += x
            ans += d[pre - k]
            d[pre] += 1
        return ans
