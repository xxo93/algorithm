# -*- coding: utf-8 -*-
""" 
@Author: wangzhongmin
@Date: 2021/3/22
@Desc: 
"""


def bubbling(nums):
    length = len(nums)
    for index in range(length):
        for i in range(length - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    print(nums)

if __name__ == '__main__':
    nums = [3, 6, 5, 1, 8, 2, 9, 6, 7]
    bubbling(nums)

