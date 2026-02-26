# 力扣 热题100 · 第45题 二叉树的右视图
# 链接: https://leetcode.cn/problems/binary-tree-right-side-view/
#
# ---------- 思路 ----------
# 题目在问什么：从右边看二叉树，每层只能看到最右边的一个节点，按层序返回这些值。
#
# 做法：DFS 先右后左。这样同一层里一定是先访问到「最右边」的节点。用 depth 当下标，第一次到达某深度时（depth==len(ans)）把该节点值加入 ans，这样每层只记录第一个访问到的（即最右）。
#
# ---------- 关键点 ----------
# · 用 DFS，先递归右子树再递归左子树。这样同一层里一定是「最右边的节点」最先被访问到。用 depth 表示当前深度，第一次到达某一深度时（depth == len(ans)）说明当前节点是该层第一个被访问的也就是最右的，加入 ans；后面同层节点访问时 ans 已经变长，不会重复加。

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return ans
