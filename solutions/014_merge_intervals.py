# 力扣 热题100 · 第14题 合并区间
# 链接: https://leetcode.cn/problems/merge-intervals/
#
# ---------- 思路 ----------
# 题目在问什么：把重叠的区间合并成不重叠的区间，返回合并后的列表。
#
# 做法：按每个区间的左端点排序。这样能合并的区间一定挨在一起。遍历时，若当前区间的左端点 <= 上一段区间的右端点，说明有重叠，就把「上一段的右端点」更新成 max(上一段右, 当前右)；否则当前区间和前面不重叠，新开一段加入结果。
#
# ---------- 关键点 ----------
# · 按左端点排序后，能合并的区间一定会挨在一起。当前区间 [a,b] 若和前面某段有重叠，那个段一定已经和更前面的合并过了，所以只需要和结果列表里「最后一段」ans[-1] 比较：若 a <= ans[-1][1] 就重叠，把最后一段的右端点改成 max(ans[-1][1], b)；否则新开一段，把 [a,b] 加进结果。
# · 合并时右端点要取 max：例如 [1,4] 和 [2,3] 合并后应是 [1,4]，不能只取当前区间的 b。

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for a, b in intervals:
            if ans and a <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], b)
            else:
                ans.append([a, b])
        return ans
