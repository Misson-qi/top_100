# 力扣 热题100 · 第77题 买卖股票的最佳时机
# 链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
#
# ---------- 思路 ----------
# 题目在问什么：每天一个股价，只能买一次卖一次，求最大利润；不能赚则 0。
#
# 做法：从左到右扫，维护「到目前为止的最低买入价」min_p。每到一天，若今天卖则利润为 今天价 - min_p，用这个更新最大利润；并更新 min_p = min(min_p, 今天价)。这样相当于枚举「在哪天卖」，买入价一定是那天之前的最低价。
#
# ---------- 关键点 ----------
# · 假设我们在「第 i 天」卖出，那买入一定是在第 0～i-1 天里选一天，且选其中价格最低的那天买利润最大。所以我们从左到右扫，一边扫一边记录「到目前为止出现过的最低价格」min_p。每到一天，如果今天卖、在之前最低价买，利润就是 今天价格 - min_p；用这个值更新答案。然后更新 min_p（把今天也考虑进去）。这样相当于枚举了「每一天作为卖出日」的最优情况。

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_p = prices[0]
        ans = 0
        for p in prices[1:]:
            ans = max(ans, p - min_p)
            min_p = min(min_p, p)
        return ans
