# 力扣 热题100 · 第20题 旋转图像
# 链接: https://leetcode.cn/problems/rotate-image/
#
# ---------- 思路 ----------
# 题目在问什么：把 n×n 矩阵原地顺时针旋转 90 度。
#
# 做法：两步。第一步：按主对角线对称交换，即 matrix[i][j] 和 matrix[j][i] 交换（只换 i<j 的，避免换两次）。第二步：每一行左右反转。合起来就是顺时针 90 度。
#
# ---------- 关键点 ----------
# · 两步：先按主对角线转置（matrix[i][j] 和 matrix[j][i] 交换），再把每一行左右反转。转置后行变列；再反转每行，就相当于把「列」从右往左排，合起来就是顺时针转 90 度。可以画一个 2×2 格子自己转一下验证。
# · 转置时只交换 i<j 的 (i,j) 和 (j,i)：若 i 和 j 都遍历就会换两次，等于没换。所以循环里写 j>i 或 j 从 i+1 开始。

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
