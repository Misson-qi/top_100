# 力扣 热题100 · 第51题 岛屿数量
# 链接: https://leetcode.cn/problems/number-of-islands/
#
# ---------- 思路 ----------
# 题目在问什么：网格里 '1' 是陆地、'0' 是水，上下左右连着的陆地算一座岛，求岛的数量。
#
# 做法：遍历每个格子，遇到 '1' 就答案加一，并从这里开始 DFS/BFS 把整座岛都标记掉（改成 '0' 或单独 visited），这样同一座岛只会被数一次。
#
# ---------- 关键点 ----------
# · 遇到 '1' 就 ans++ 并 DFS 把整座岛改成 '0'：这样同一座岛只会被计一次，且之后不会再扫到这座岛上的 '1'。
# · DFS 内先判越界和 grid[i][j]!='1' 再改值：避免重复进入或改错。改完再四方向递归，这样每个 '1' 只会被访问一次。

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(i + di, j + dj)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
