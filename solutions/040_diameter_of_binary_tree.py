# 力扣 热题100 · 第40题 二叉树的直径
# 链接: https://leetcode.cn/problems/diameter-of-binary-tree/
#
# ---------- 思路 ----------
# 题目在问什么：二叉树的直径 = 任意两节点之间路径的最大长度（边数）。这条路径不一定过根。
#
# 做法：对每个节点，若「最长路径」经过它，则路径长 = 左子树深度 + 右子树深度（两边各一条最长链拼起来）。所以做 DFS，递归返回子树深度，在递归里用 左深+右深 更新全局最大直径。
#
# ---------- 关键点 ----------
# · 若最长路径经过某节点，那这条路径 = 从该节点往左能走到的最远距离 + 往右能走到的最远距离（边数）。所以对每个节点，用「左子树深度 + 右子树深度」更新全局最大直径。递归时返回「从该节点到叶子的最大深度」（给父节点用），在递归里用 左深+右深 更新答案即可。
# · 直径可能过任意节点，所以 DFS 遍历时在每个节点都算一次「过当前节点的最长路径」，取全局最大。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            ans = max(ans, L + R)
            return 1 + max(L, R)

        depth(root)
        return ans
