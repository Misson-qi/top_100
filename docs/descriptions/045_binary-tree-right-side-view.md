# 045. 二叉树的右视图

- **题目链接**：[二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给定一个二叉树的 根节点 root ，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1：

输入： root = [1,2,3,null,5,null,4]

输出： [1,3,4]

解释： ![题目图示](./assets/045_binary-tree-right-side-view_0.png)

示例 2：

输入： root = [1,2,3,4,null,null,null,5]

输出： [1,3,4,5]

解释： ![题目图示](./assets/045_binary-tree-right-side-view_1.png)

示例 3：

输入： root = [1,null,3]

输出： [1,3]

示例 4：

输入： root = []

输出： []

提示: 
- 二叉树的节点个数的范围是 [0,100] 
- -100 <= Node.val <= 100
