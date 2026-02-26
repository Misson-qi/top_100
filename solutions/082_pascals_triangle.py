# 力扣 热题100 · 第82题 杨辉三角
# 链接: https://leetcode.cn/problems/pascals-triangle/
#
# ---------- 思路 ----------
# 题目在问什么：生成杨辉三角的前 numRows 行，每行是上一行相邻两数之和，首尾为 1。
#
# 做法：按行生成。第 0 行 [1]；第 i 行有 i+1 个数，第 0 个和最后一个为 1，中间 row[j] = 上一行[j-1] + 上一行[j]。用上一行算下一行即可。
#
# ---------- 关键点 ----------
# · 杨辉三角的规则：每行首尾是 1，中间每个数等于「上一行同位置前一个数 + 上一行同位置的数」。即第 i 行（从 0 开始）有 i+1 个数，row[0]=row[i]=1，row[j]=上一行[j-1]+上一行[j]（1<=j<=i-1）。从第一行 [1] 开始，一行一行往下推即可。

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(ans[-1][j - 1] + ans[-1][j])
            row.append(1)
            ans.append(row)
        return ans
