# 力扣 热题100 · 第48题 路径总和 III
# 链接: https://leetcode.cn/problems/path-sum-iii/
#
# ---------- 思路 ----------
# 题目在问什么：找「路径和等于 targetSum」的路径数量。路径必须从上到下、从某节点到其子节点，且只能往下走。
#
# 做法：从根到当前节点的路径和记作 cur。若「从根到上面某点」的和为 cur-targetSum，则从那个点到当前点这一段和就是 targetSum。用字典记录「根到当前路径上」每个前缀和出现的次数，到当前节点时加上 pre[cur-targetSum]，再把 cur 加入 pre，递归左右，回溯时 pre[cur]--。
#
# ---------- 关键点 ----------
# · 路径必须从上到下连续。从根到当前节点的和 cur 是确定的；若「从某祖先到当前」这段和等于 targetSum，则「从根到该祖先」的和 = cur - targetSum。所以用字典 pre 记录「从根到当前路径上」每个前缀和出现的次数，到当前节点时，以当前为终点的合法路径数 = pre[cur - targetSum]，然后再把 cur 加入 pre，递归左右，回溯时 pre[cur]--。
# · pre[0]=1 要写：当从根到当前的路径和刚好等于 targetSum 时，整段就是一条路径，对应「前缀为空、和为 0」，所以要 pre[0]=1 才统计得到。
# · 先查 pre[cur-targetSum] 再加 pre[cur]：这样统计的前缀都是「严格在当前节点之上的祖先」，不会把当前节点自己当起点。回溯时 pre[cur]--，因为离开当前节点后，这条路径上的前缀和就不算数了，否则兄弟子树会多算。

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre = defaultdict(int)
        pre[0] = 1

        def dfs(node: Optional[TreeNode], cur: int) -> int:
            if not node:
                return 0
            cur += node.val
            cnt = pre[cur - targetSum]
            pre[cur] += 1
            cnt += dfs(node.left, cur) + dfs(node.right, cur)
            pre[cur] -= 1
            return cnt

        return dfs(root, 0)
