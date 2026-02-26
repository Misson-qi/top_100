# 力扣 热题100 · 第52题 腐烂的橘子
# 链接: https://leetcode.cn/problems/rotting-oranges/
#
# ---------- 思路 ----------
# 题目在问什么：网格里 0 空、1 新鲜、2 腐烂。每分钟腐烂的橘子会把相邻新鲜橘子变腐烂。求全部变腐烂的最短时间；若有永远不烂的返回 -1。
#
# 做法：多源 BFS。一开始把所有 2 入队（时间 0），每次弹出一个 (i,j,t)，把上下左右的新鲜 1 变成 2 并 (ni,nj,t+1) 入队。若某时刻 fresh 变 0 则返回 t+1。队列空后若还有 fresh 则返回 -1。
#
# ---------- 关键点 ----------
# · 多源 BFS：所有 2 一起入队、时间 0，每轮扩散到的格子时间+1。这样「同一分钟」腐烂的橘子会一起扩散，时间正确。
# · 用 fresh 计数剩余 1 的个数：每把一个 1 改成 2 就 fresh--，若 fresh 变 0 说明刚感染完最后一个，返回当前 t+1（因为感染发生在「这一分钟」）。
# · 队列空时若 fresh>0：说明还有新鲜橘子没被任何 2 扩散到（不连通），返回 -1。

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while q:
            i, j, t = q.popleft()
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    if fresh == 0:
                        return t + 1
                    q.append((ni, nj, t + 1))
        return -1
