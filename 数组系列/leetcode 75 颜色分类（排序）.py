# -*- coding: utf-8 -*-
"""
1. 问题描述：
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意: 不能使用代码库中的排序函数来解决这道题。

示例1:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

[2,0,2,1,1,0]
[0,2,2,1,1,0]
"""


def sortColors(nums: list) -> list:
    p = 1
    while p < len(nums):
        i = p
        while i > 0:
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
                i -= 1
            else:
                break
        p += 1

    return nums


if __name__ == '__main__':
    print(sortColors([2, 0, 2, 1, 1, 0]))
