# -*- coding: utf-8 -*-
"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

[
   [2],
  [3,4],
 [6,5,7],
[4,1,8,3]
]
则自顶向下的最小路径和为11（即，2 + 3 + 5 + 1 = 11）。
"""
import math


class Solution:
    def minimumTotal(self, triangle: list) -> int:
        row = len(triangle)

        dp = [[0 for j in range(i + 1)] for i in range(row)]
        dp[0][0] = triangle[0][0]

        for r in range(len(triangle)):
            for c in range(r + 1):
                if r == 0 and c == 0:
                    dp[0][0] = triangle[0][0]
                elif c == 0 and r > 0:
                    dp[r][0] = dp[r - 1][0] + triangle[r][c]
                elif c == r and r > 0:
                    dp[r][c] = dp[r - 1][c - 1] + triangle[r][c]
                else:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c]) + triangle[r][c]
                # print(r, c)
        print(dp)
        return min(dp[-1])


if __name__ == '__main__':
    obj = Solution()
    arr = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    print(obj.minimumTotal(arr))

    print('-- over! --')
