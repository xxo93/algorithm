# -*- coding: utf-8 -*-
""" 最长上升子序列(Longest Increasing Subsequence，LIS)

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k, 且满足 0 ≤ i < j < k ≤ n-1， 使得 arr[i] < arr[j] < arr[k]
，返回 true ; 否则返回 false 。 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:
输入: [1,2,3,4,5]
输出: true
示例 2:
输入: [5,4,3,2,1]
输出: false
示例 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""


class Solution:
    def increasingTriplet(self, nums: list) -> int:
        """ 方法1 """
        length = len(nums)
        if length <= 2:
            return False

        dp = [1 for _ in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == 3:
                        return True

        return False

    def increasingTriplet2(self, nums: list) -> int:
        """ 方法2: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) """
        length = len(nums)
        if length <= 2:
            return False



        return False


if __name__ == '__main__':
    s = Solution()

    arr1 = [10, 9, 2, 5, 3, 7, 101, 18]
    arr2 = [0, 1, 0, 3, 2, 3]
    arr3 = [7, 7, 7, 7, 7, 7, 7]
    arrs = [arr1, arr2, arr3]

    for arr in arrs:
        res = s.increasingTriplet(arr)
        print(res)

    print('-- over --')
