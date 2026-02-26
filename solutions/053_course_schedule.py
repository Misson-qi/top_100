# 力扣 热题100 · 第53题 课程表
# 链接: https://leetcode.cn/problems/course-schedule/
#
# ---------- 思路 ----------
# 题目在问什么：有 n 门课和若干先修关系 [a,b] 表示选 a 前要先选 b。问能否全部修完（即图中无环）。
#
# 做法：建图后 DFS 判环。每个节点状态：0 未访问、1 访问中、2 已完成。从某点开始 DFS 时先标 1，递归其邻居，若遇到状态 1 说明有环（ back edge），返回 False；递归完标 2。所有点都 DFS 一遍，都无环则 True。
#
# ---------- 关键点 ----------
# · 等价于判断有向图有没有环。用 DFS：每个点三种状态——0 未访问、1 正在访问（在 DFS 栈里）、2 已访问完。进入一个点先标 1，递归它的邻居；若递归时碰到状态 1 的点，说明有一条边指回当前路径，即环，返回 False；递归完标 2。若碰到状态 2 的点，说明是别的分支，不用管。
# · 建图：题目 [a,b] 表示选 a 前要先选 b，即 b→a，所以 g[b].append(a)。要对每个点都尝试 DFS，因为图可能不连通，只从 0 可能漏掉别的分量里的环。

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        state = [0] * numCourses  # 0 未访问 1 访问中 2 完成

        def dfs(u: int) -> bool:
            if state[u] == 1:
                return False
            if state[u] == 2:
                return True
            state[u] = 1
            for v in g[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True

        return all(dfs(i) for i in range(numCourses))
