# 力扣 热题100 · 第18题 矩阵置零
# 链接: https://leetcode.cn/problems/set-matrix-zeroes/
#
# ---------- 思路 ----------
# 题目在问什么：若某个位置是 0，把该行该列全部变成 0。要求 O(1) 额外空间。
#
# 做法：用第一行、第一列当「标记」：若 matrix[i][j]==0，就令 matrix[i][0]=0 和 matrix[0][j]=0，表示第 i 行、第 j 列最后要整行整列置零。先单独记下第一行、第一列本身有没有 0（row0、col0），再遍历 1~m-1 行、1~n-1 列根据 matrix[i][0]、matrix[0][j] 把内部置零，最后根据 row0、col0 把第一行第一列置零。
#
# ---------- 关键点 ----------
# · 用第一行、第一列当「标记」：若 matrix[i][j]==0，就令 matrix[i][0]=0、matrix[0][j]=0，表示第 i 行、第 j 列待会要整行整列置零。但这样会覆盖第一行第一列原来的值，所以一开始先用 row0、col0 记下「第一行/第一列本身有没有 0」，最后再根据这两个变量决定是否把第一行、第一列整体置零。
# · 分两轮：第一轮只打标记（matrix[i][0]、matrix[0][j]），不把内部立刻改掉，否则后面的 0 可能漏标。第二轮根据首行首列的标记，把 (1,1) 到 (m-1,n-1) 里该置零的置零，最后根据 row0、col0 处理第一行和第一列。

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row0 = any(matrix[0][j] == 0 for j in range(n))
        col0 = any(matrix[i][0] == 0 for i in range(m))
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0:
            for j in range(n):
                matrix[0][j] = 0
        if col0:
            for i in range(m):
                matrix[i][0] = 0
