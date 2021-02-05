# -*- coding: utf-8 -*-
"""
描述：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的
方法可以爬到楼顶呢？ 注意：给定 n 是一个正整数。

示例1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""
"""
1   dp[1] = 1
2   dp[2] = 2
3   dp[3] = 3
4   dp[4] = 5
dp[n] = dp[n-1] + dp[n-2]
"""


class Solution:
    def climb_stairs_recursive(self, n: int) -> int:
        """ 递归法 """
        if n == 1 or n == 2:
            return n
        if n >= 3:
            return self.climb_stairs_recursive(n - 1) + self.climb_stairs_recursive(n - 2)

        return n

    def climb_stairs_dp(self, n: int) -> int:
        """ 动态规划 """
        if n == 1:
            return 1
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n - 1]


if __name__ == '__main__':
    s = Solution()
    n = 7
    res2 = s.climb_stairs_recursive(n)
    res3 = s.climb_stairs_dp(n)
    print(res2)
    print(res3)

    print('-- over --')
