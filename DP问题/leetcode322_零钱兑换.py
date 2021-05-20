# -*- coding: utf-8 -*-
"""
解析：https://www.cnblogs.com/hengzhezou/p/11042906.html
解析：https://blog.csdn.net/qq_17550379/article/details/82909656

给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

示例 6：当硬币金额面值不限的情况
输入：coins = [1, 2, 5, 7, 10], amount = 14
输出：2 而不是 3
解释：14 = 7 + 7  而不是 14 = 10 + 2 + 2

示例6分析：思路类似于[青蛙跳楼梯]
dp = [0, -1, ..., -1], len(dp) = amount + 1
dp[i] = min(dp[i-coins[0]] + dp[i-coins[1]] + dp[i-coins[2]] + dp[i-coins[3]] + dp[i-coins[4]]) + 1
dp[i] = min(dp[i-coins[n]]) + 1 , if i >= coins[n] , 0 < n < len(coins)

"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp, len(dp) = amount + 1
        dp = [0] + [amount + 1] * amount
        print(dp)

        # 外层循环负责遍历dp
        for i in range(amount + 1):
            # 内层循环负责找出 dp[i] 的最小值
            for coin in coins:
                # 只有总钱数大于目前讨论的硬币面值才比较
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        print(dp)
        # 如果没有更新dp，说明无解 返回-1
        if (dp[amount] == amount + 1):
            return -1

        return dp[amount]


if __name__ == '__main__':
    obj = Solution()

    coins, amount = [1, 2, 5], 11
    print(obj.coinChange(coins, amount))

    coins, amount = [2], 3
    print(obj.coinChange(coins, amount))

    coins, amount = [1], 0
    print(obj.coinChange(coins, amount))

    coins, amount = [1], 1
    print(obj.coinChange(coins, amount))

    coins, amount = [1], 2
    print(obj.coinChange(coins, amount))

    coins, amount = [1, 2, 5, 7, 10], 14
    print(obj.coinChange(coins, amount))
