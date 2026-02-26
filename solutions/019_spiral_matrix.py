# 力扣 热题100 · 第19题 螺旋矩阵
# 链接: https://leetcode.cn/problems/spiral-matrix/
#
# ---------- 思路 ----------
# 题目在问什么：按「从外到里、顺时针」的顺序，把矩阵转成一维数组。
#
# 做法：用四个变量 t、b、l、r 表示当前这一圈的上下左右边界。按顺序：先从左到右走顶行，再从上到下走右列，再从右到左走底行，再从下到上走左列。每走完一条边就把对应的边界往里缩一格（t++、b--、l++、r--）。当 t>b 或 l>r 时结束。
#
# ---------- 关键点 ----------
# · 用 t,b,l,r 表示当前这一圈的上下左右边界。每圈按顺序走四条边：顶行（l 到 r）、右列（t 到 b）、底行（r 到 l）、左列（b 到 t）。每走完一条边就把对应边界往里缩一格（顶行走完 t++，右列走完 r--，底行走完 b--，左列走完 l++）。
# · 走完一条边后要检查：若 t>b 或 l>r 就 break。因为有时最后一圈只剩一行或一列，顶行和底行可能是同一行，若不再 break 会重复打印。所以「顶行走完 t++ 后 if t>b: break」再走右列，这样只剩一行时就不会再走右、底、左。

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ans = []
        while t <= b and l <= r:
            for j in range(l, r + 1):
                ans.append(matrix[t][j])
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for j in range(r, l - 1, -1):
                ans.append(matrix[b][j])
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
        return ans
