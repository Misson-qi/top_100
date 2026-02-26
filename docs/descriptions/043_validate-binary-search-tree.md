# 043. 验证二叉搜索树

- **题目链接**：[验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。 有效 二叉搜索树定义如下： 
- 节点的左 子树 只包含  严格小于 当前节点的数。 
- 节点的右子树只包含 严格大于 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

示例 1： ![题目图示](./assets/043_validate-binary-search-tree_0.jpg)

输入： root = [2,1,3]

输出： true

示例 2： ![题目图示](./assets/043_validate-binary-search-tree_1.jpg)

输入： root = [5,1,4,null,null,3,6]

输出： false

解释： 根节点的值是 5 ，但是右子节点的值是 4 。

提示： 
- 树中节点数目范围在 [1, 10^4^ ] 内 
- -2^31^ <= Node.val <= 2^31^ - 1
