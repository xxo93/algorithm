# -*- coding: utf-8 -*-
"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        if target > nums[-1]:
            return len(nums)

        # 按索引二分
        left, right = 0, len(nums) - 1

        while left < right:
            # 二分搜索
            mid = (left + right) >> 1

            # 条件
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    obj = Solution()

    arr, target = [1, 3, 5, 6], 5
    print(obj.searchInsert(arr, target))   # 2

    arr, target = [1, 3, 5, 6], 2
    print(obj.searchInsert(arr, target))   # 1

    arr, target = [1, 3, 5, 6], 7
    print(obj.searchInsert(arr, target))   # 4

    arr, target = [1, 3, 5, 6], 0
    print(obj.searchInsert(arr, target))   # 0
