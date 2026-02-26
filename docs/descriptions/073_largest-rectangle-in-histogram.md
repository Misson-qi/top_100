# 073. 柱状图中最大的矩形

- **题目链接**：[柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1: ![题目图示](./assets/073_largest-rectangle-in-histogram_0.jpg)

输入： heights = [2,1,5,6,2,3]

输出： 10

解释： 最大的矩形为图中红色区域，面积为 10

示例 2： ![题目图示](./assets/073_largest-rectangle-in-histogram_1.jpg)

输入： heights = [2,4]

输出： 4

提示： 
- 1 <= heights.length <=10^5^ 
- 0 <= heights[i] <= 10^4^
