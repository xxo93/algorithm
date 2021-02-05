# -*- coding: utf-8 -*-
""" 最长上升子序列(Longest Increasing Subsequence，LIS)
描述：给定一个无序的整数数组，找到其中最长上升子序列的长度。

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
"""

"""
我们分两种情况进行讨论：
如果nums[i]比前面的所有元素都小，那么dp[i]等于1（即它本身）（该结论正确）
nums = [6, 5, 7, 9, 8, 5, 4]    # 7
nums[6] = 4
dp[6] = 4
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 3
dp[5] = 3
dp[6] = 3
如果nums[i]前面存在比他小的元素nums[j]，那么dp[i]就等于dp[j]+1（该结论错误，比如
nums[3]>nums[0]，即9>1,但是dp[3]并不等于dp[0]+1）
"""


class Solution:
    """
    因为dp[i]前面比他小的元素，不一定只有一个！
    可能除了 nums[j]，还包括 nums[k]，nums[p] 等等等等。
    所以 dp[i] 除了可能等于 dp[j]+1，还有可能等于 dp[k]+1，dp[p]+1 等等等等。
    所以我们求 dp[i]，需要找到 dp[j]+1，dp[k]+1，dp[p]+1 等等等等 中的最大值
    """

    def lengthOfLIS(self, nums: list) -> int:
        """ 动态规划 """
        length = len(nums)
        if length <= 1:
            return length

        dp = [1 for _ in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    s = Solution()

    # arr1 = [10, 9, 2, 5, 3, 7, 101, 18]
    arr1 = [2, 5, 1, 5, 4, 5]
    arr2 = [0, 1, 0, 3, 2, 3]
    arr3 = [7, 7, 7, 7, 7, 7, 7]
    arrs = [arr1, arr2, arr3]

    for arr in arrs:
        res = s.lengthOfLIS(arr)
        print(res)

    print('-- over --')
