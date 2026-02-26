# 019. 螺旋矩阵

- **题目链接**：[螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给你一个 m 行 n 列的矩阵  matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1： ![题目图示](./assets/019_spiral-matrix_0.jpg)

输入： matrix = [[1,2,3],[4,5,6],[7,8,9]]

输出： [1,2,3,6,9,8,7,4,5]

示例 2： ![题目图示](./assets/019_spiral-matrix_1.jpg)

输入： matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

输出： [1,2,3,4,8,12,11,10,9,5,6,7]

提示： 
- m == matrix.length 
- n == matrix[i].length 
- 1 <= m, n <= 10 
- -100 <= matrix[i][j] <= 100
