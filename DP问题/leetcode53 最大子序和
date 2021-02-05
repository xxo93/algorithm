# -*- coding: utf-8 -*-
"""
描述：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例：
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""
"""
定义dp[i]：表示以 nums[i] 结尾的连续子数组的最大和。

dp[i] = max(dp[i-1], nums[i])

len(nums)>1:
dp[i] = dp[i-1] + nums[i] , if (dp[i-1] >= 0)
dp[i] = nums[i] , if (dp[i-1] < 0)

len(nums)==1:
dp[0] = nums[0]

:return max(dp[0], dp[1], ... dp[i])
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:
        """ 动态规划 """
        if len(nums) == 1:
            return nums[0]

        length = len(nums)
        dp = [nums[0]]
        for i in range(1, length):
            if dp[i - 1] >= 0:
                dp.append(dp[i - 1] + nums[i])
            else:
                dp.append(nums[i])

        return max(dp)


if __name__ == '__main__':
    s = Solution()

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res2 = s.maxSubArray(arr)
    print(res2)

    print('-- over --')
