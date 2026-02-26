# 064. 搜索二维矩阵

- **题目链接**：[搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给你一个满足下述两条属性的 m x n 整数矩阵： 
每行中的整数从左到右按非严格递增顺序排列。 
每行的第一个整数大于前一行的最后一个整数。 
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

示例 1： ![题目图示](./assets/064_search-a-2d-matrix_0.jpg)

输入： matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

输出： true

示例 2： ![题目图示](./assets/064_search-a-2d-matrix_1.jpg)

输入： matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13

输出： false

提示： 
- m == matrix.length 
- n == matrix[i].length 
- 1 <= m, n <= 100 
- -10^4^ <= matrix[i][j], target <= 10^4^
