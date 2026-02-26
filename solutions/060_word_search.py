# 力扣 热题100 · 第60题 单词搜索
# 链接: https://leetcode.cn/problems/word-search/
#
# ---------- 思路 ----------
# 题目在问什么：二维网格里相邻（上下左右）格子能否按顺序连成给定单词，每个格子最多用一次。
#
# 做法：从每个格子出发做 DFS，看能否从 word[0] 开始匹配。当前匹配到 word[k]：若 k 已到末尾返回 True；若越界或格子不等于 word[k] 返回 False；否则把格子临时改掉（或记 visited），向四方向递归 k+1，有一个 True 就返回 True，最后恢复格子。
#
# ---------- 关键点 ----------
# · 同一个格子不能重复走：DFS 时从 (i,j) 会往上下左右四个方向递归。如果不对当前格子做标记，可能从 (i,j) 走到 (i+1,j)，又从 (i+1,j) 走回 (i,j)，形成重复使用。所以进入 (i,j) 时先把 board[i][j] 存起来再改成空串（或任意不会和字母相等的字符），递归完四个方向后再把格子恢复回去。这样在「当前这条路径」上，走过的格子不会被再走一次。
# · 要从每个格子 (i,j) 都试一次 dfs(i, j, 0)：因为单词可能从棋盘上任意一个格子开始，我们不知道起点在哪，所以枚举所有格子作为起点，只要有一个起点能走出完整单词就返回 True。

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            board[i][j], tmp = "", board[i][j]
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                if dfs(i + di, j + dj, k + 1):
                    return True
            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
