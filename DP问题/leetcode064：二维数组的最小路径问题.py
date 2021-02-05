""" 递归与动态规划
题目: 二维数组的最小路径问题
说明: 给你一个二维数组，二维数组中的每个数都是正数，要求从左上角走到右下角，每一步只能向右或者向下。沿途经过的数字要累加起来。返回最小的路径和。

input:
arr = [
    [1, 3, 5, 9],
    [8, 1, 3, 4],
    [5, 0, 6, 1],
    [8, 6, 4, 0],
]
output: 12
解释: 1 + 3 + 1 + 0 + 6 + 1 + 0 = 12
"""
"""
i <= row == len(arr)
j <= col == len(arr[0])

dp[i][j] = min( dp[i][j-1], dp[i-1][j] ) + arr[i][j]
边界：
i == 0, dp[i][j] = dp[0][j - 1] + grid[0][j]
j == 0, dp[i][j] = dp[i - 1][0] + grid[i][0]
j == 0 and i == 0, dp[i][j] = grid[0][0]
"""


class Solution:
    def minPathSum(self, grid: list) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for c in range(col)] for r in range(row)]

        for i in range(row):
            for j in range(col):
                if (i - 1) >= 0 and (j - 1) >= 0 and i <= row and j <= col:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
                if i == 0 and (j - 1) >= 0:
                    dp[i][j] = dp[0][j - 1] + grid[0][j]
                if j == 0 and (i - 1) >= 0:
                    dp[i][j] = dp[i - 1][0] + grid[i][0]
                if j == 0 and i == 0:
                    dp[i][j] = grid[0][0]
        print(dp)
        return dp[row - 1][col - 1]


if __name__ == '__main__':
    obj = Solution()
    arr = [
        [1, 3, 5, 9],
        [8, 1, 3, 4],
        [5, 0, 6, 1],
        [8, 6, 4, 0],
    ]
    # print(obj.minPathSum(arr))

    arr = [[1]]
    print(obj.minPathSum(arr))
    print('-- over! --')
