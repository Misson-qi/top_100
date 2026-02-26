# 041. 二叉树的层序遍历

- **题目链接**：[二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1： ![题目图示](./assets/041_binary-tree-level-order-traversal_0.jpg)

输入： root = [3,9,20,null,null,15,7]

输出： [[3],[9,20],[15,7]]

示例 2：

输入： root = [1]

输出： [[1]]

示例 3：

输入： root = []

输出： []

提示： 
- 树中节点数目在范围 [0, 2000] 内 
- -1000 <= Node.val <= 1000
