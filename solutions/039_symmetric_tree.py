# 力扣 热题100 · 第39题 对称二叉树
# 链接: https://leetcode.cn/problems/symmetric-tree/
#
# ---------- 思路 ----------
# 题目在问什么：判断一棵二叉树是否「轴对称」，即左子树和右子树镜像对称。
#
# 做法：写一个函数 mirror(a, b) 判断两棵树是否镜像。镜像条件：a、b 都空则真；一个空一个不空或值不等则假；否则 a 的左和 b 的右镜像、a 的右和 b 的左镜像。主函数里若 root 为空则真，否则看 root.left 和 root.right 是否镜像。
#
# ---------- 关键点 ----------
# · 两棵树「镜像」的意思是：根值相等，且 a 的左和 b 的右镜像、a 的右和 b 的左镜像。所以写一个函数 mirror(a, b)，递归时比较 (a.left, b.right) 和 (a.right, b.left)。主函数里看 root.left 和 root.right 是否镜像即可。
# · 先判空：都空返回 True；一个空一个不空返回 False；再比较 val，不等返回 False。这样不会访问空指针。

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right) if root else True
