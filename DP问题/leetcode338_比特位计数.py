# -*- coding: utf-8 -*-
""" 
@Author: wangzhongmin
@Date: 2021/4/22
@Desc:
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:
输入: 2
输出: [0,1,1]

示例 2:
输入: 5
输出: [0,1,1,2,1,2]

进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""
from typing import List


class Solution:

    # 一般方法
    def countBitsList(self, num: int) -> List[int]:
        """ 一般方法 """

        def countOne(num: int) -> int:
            """ 计算 num 的 1 的个数 """
            c = 0
            while num > 0:
                # if num & 1 == 1:  # 最后一位(当前位)是1
                #     c += 1
                # num >>= 1
                num &= (num - 1)  # num = num & (num-1)
                c += 1
            return c

        arr = []
        for i in range(num + 1):
            arr.append(countOne(i))
        return arr

    # 动态规划
    def countBits_dp(self, num: int) -> List[int]:
        """ 动态转移方程
        奇数：i（奇数）的二进制的 1 的个数 = ( i-1 (偶数) 的二进制的 1 的个数) + 1。eg: count(i) = count(i-1) + 1
        偶数：j (偶数) 的二进制的 1 的个数 = j/2 的二进制 1 的个数。eg: count(j) = count(j/2)
        """
        # 初始化dp数组
        dp = list()
        dp.append(0)

        for i in range(1, num + 1):
            # 如果i是奇数
            if i & 1 == 1:
                dp.append(dp[i - 1] + 1)
            # 如果i是偶数
            else:
                dp.append(dp[i >> 1])
        return dp


if __name__ == '__main__':
    obj = Solution()
    num = 5

    # 一般方法
    print(obj.countBitsList(num))

    # 动态规划
    print(obj.countBits_dp(num))
