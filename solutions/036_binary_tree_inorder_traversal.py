# 力扣 热题100 · 第36题 二叉树的中序遍历
# 链接: https://leetcode.cn/problems/binary-tree-inorder-traversal/
#
# ---------- 思路 ----------
# 题目在问什么：按「左-根-右」顺序遍历二叉树，返回值的列表。要求用迭代（栈）实现，不用递归。
#
# 做法：用栈模拟。当前节点不为空就一路往左走并压栈；为空就弹栈，访问栈顶（加入结果），然后当前节点改为栈顶的右子，继续。这样相当于「先走完左边，再根，再右边」。
#
# ---------- 关键点 ----------
# · 用栈模拟中序：当前节点不空就一路往左走并压栈；当前为空就弹栈，访问弹出来的节点（加入结果），再把「当前」设为该节点的右子，继续。这样相当于先把左边都走完，再访问根，再处理右边，顺序就是左-根-右。
# · 循环条件 root or st：root 不空说明还有子树要处理（先压左链）；root 为空说明该回溯了，从栈里弹出一个节点访问，再转去它的右子树。

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st, ans = [], []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            ans.append(root.val)
            root = root.right
        return ans
