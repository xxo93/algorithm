# -*- coding: utf-8 -*-
""" 全排列: 回溯
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        return []


if __name__ == '__main__':
    obj = Solution()

    Arr = [
        [1, 2, 3],
        [2, 2, 3, 3],
        [3, 6, 1, 5],
    ]

    for nums in Arr:
        print(obj.permute(nums))
