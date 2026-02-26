# 065. 在排序数组中查找元素的第一个和最后一个位置

- **题目链接**：[在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=study-plan-v2&envId=top-100-liked)
- **题目标签**：见 [热题100-学习计划顺序.md](../热题100-学习计划顺序.md)

---

## 题目描述

给定目标值在数组中的开始位置和结束位置。 如果数组中不存在目标值 target ，返回  [-1, -1] 。 你必须设计并实现时间复杂度为  O(log n)  的算法解决此问题。

示例 1：

输入： nums = [ 5,7,7,8,8,10] , target = 8

输出： [3,4]

示例 2：

输入： nums = [ 5,7,7,8,8,10] , target = 6

输出： [-1,-1]

示例 3：

输入： nums = [], target = 0

输出： [-1,-1]

提示： 
- 0 <= nums.length <= 10^5^ 
- -10^9^  <= nums[i] <= 10^9^ 
- nums  是一个非递减数组 
- -10^9^  <= target <= 10^9^
