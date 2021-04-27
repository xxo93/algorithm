# -*- coding: utf-8 -*-
""" 
@Author: wangzhongmin
@Date: 2021/3/23
@Desc:
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

示例 1：
输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]
输出：
[[0,0,0],
 [0,1,0],
 [0,0,0]]

示例 2：
输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]
输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]

提示：
给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
"""
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        pass


if __name__ == '__main__':
    obj = Solution()

    Arr1 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print(obj.updateMatrix(Arr1))


    Arr1 = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]
    print(obj.updateMatrix(Arr1))
