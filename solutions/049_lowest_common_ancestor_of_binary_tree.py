# 力扣 热题100 · 第49题 二叉树的最近公共祖先
# 链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
#
# ---------- 思路 ----------
# 题目在问什么：在二叉树里找 p 和 q 的「最近公共祖先」：同时是 p、q 祖先的节点里深度最大的。
#
# 做法：递归。若当前根是 None 或是 p 或是 q，直接返回根。否则递归求左子树、右子树里 p、q 的 LCA。若左右都非空，说明 p、q 分居两侧，当前根就是 LCA；若只有一侧非空，说明 p、q 都在那一侧，返回那一侧的结果。
#
# ---------- 关键点 ----------
# · 若当前根是 p 或 q，直接返回根：若另一个在子树里，LCA 就是当前根；若另一个不在，当前根会被带上去，在更高层和另一个相遇时，当前根就是 LCA。若根是空也返回空。
# · 否则递归求左、右子树里 p、q 的 LCA。若左右返回值都非空，说明 p、q 分别在两侧，当前根就是 LCA；若只有一侧非空，说明 p、q 都在那一侧，返回那一侧的结果即可。

from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
