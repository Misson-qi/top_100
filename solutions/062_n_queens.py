# 力扣 热题100 · 第62题 N 皇后
# 链接: https://leetcode.cn/problems/n-queens/
#
# ---------- 思路 ----------
# 题目在问什么：在 n×n 棋盘放 n 个皇后，互不攻击（不同行、列、主对角、副对角）。求所有摆法。
#
# 做法：按行放。第 row 行枚举放在哪一列 col，用集合记录已占用的列、主对角(row-col)、副对角(row+col)。不冲突就放，递归 row+1，放满 n 行就按格式记录当前棋盘并回溯。
#
# ---------- 关键点 ----------
# · 按行放皇后：第 0 行放一个，第 1 行放一个……这样自然保证不同行。每一行我们枚举「放在哪一列」。皇后会攻击同一列、同一主对角线、同一副对角线，所以要用三个集合记录：哪些列已占用、哪些主对角已占用、哪些副对角已占用。同一主对角线上的格子 (r,c) 满足 r-c 相同（例如 (1,0) 和 (2,1) 的 1-0=2-1）；同一副对角线上 r+c 相同。所以用 col、row-col、row+col 三个 set 就能快速判断当前列能不能放。
# · 递归到 row==n 说明 n 行都放好了，path 里按顺序存的是每一行皇后所在的列号。根据列号拼成题目要求的字符串：第 c 列有皇后就是 "."*c + "Q" + "."*(n-1-c)。

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col, diag1, diag2 = set(), set(), set()

        def backtrack(row: int, path: List[int]) -> None:
            if row == n:
                board = ["." * c + "Q" + "." * (n - 1 - c) for c in path]
                ans.append(board)
                return
            for c in range(n):
                if c in col or (row - c) in diag1 or (row + c) in diag2:
                    continue
                col.add(c)
                diag1.add(row - c)
                diag2.add(row + c)
                path.append(c)
                backtrack(row + 1, path)
                path.pop()
                col.discard(c)
                diag1.discard(row - c)
                diag2.discard(row + c)

        backtrack(0, [])
        return ans
