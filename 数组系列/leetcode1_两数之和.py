# -*- coding:utf-8 -*-
"""
@Author: wangzhongmin
@Time  : 2021/8/5 17:57
@Desc  : 简单题
"""
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        时间复杂度：O(n^2)
        """
        p1 = 0
        while p1 < len(nums):
            for i in range(p1 + 1, len(nums)):
                if nums[p1] + nums[i] == target:
                    return [p1, i]
            p1 += 1

    #
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        使用 MAP
        时间复杂度：O(n)
        """

        return []


if __name__ == '__main__':
    obj = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print(obj.twoSum(nums, target))
