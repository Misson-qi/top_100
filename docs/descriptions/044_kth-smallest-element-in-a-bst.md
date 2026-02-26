# 044. 二叉搜索树中第 K 小的元素

- **题目链接**：[二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第  k   小的元素（ k 从 1 开始计数）。

示例 1： ![题目图示](./assets/044_kth-smallest-element-in-a-bst_0.jpg)

输入： root = [3,1,4,null,2], k = 1

输出： 1

示例 2： ![题目图示](./assets/044_kth-smallest-element-in-a-bst_1.jpg)

输入： root = [5,3,6,2,4,null,null,1], k = 3

输出： 3

提示： 
- 树中的节点数为 n 。 
- 1 <= k <= n <= 10^4^ 
- 0 <= Node.val <= 10^4^

进阶： 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
