# 042. 将有序数组转换为二叉搜索树

- **题目链接**：[将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

示例 1： ![题目图示](./assets/042_convert-sorted-array-to-binary-search-tree_0.jpg)

输入： nums = [-10,-3,0,5,9]

输出： [0,-3,9,-10,null,5]

解释： [0,-10,5,null,-3,null,9] 也将被视为正确答案： ![题目图示](./assets/042_convert-sorted-array-to-binary-search-tree_1.jpg)

示例 2： ![题目图示](./assets/042_convert-sorted-array-to-binary-search-tree_2.jpg)

输入： nums = [1,3]

输出： [3,1]

解释： [1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示： 
- 1 <= nums.length <= 10^4^ 
- -10^4^ <= nums[i] <= 10^4^ 
- nums 按 严格递增 顺序排列
