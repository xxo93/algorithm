# -*- coding: utf-8 -*-
'''
给定一个包含了一些 1 和 0 的费控二维数组 grid。
一个岛屿是由相邻的 1 （代表土地）构成的组合，协力的[相邻]要求两个 1 必须在 水平 或 竖直方向上相邻 。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二位数组中的岛屿个数。如果没有岛屿，则返回为 0 。

注：
1. 只能水平和竖直方向才是相邻
2. 每个维度不超过 50 。

Example1:
Input: grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
Output: 1

Example2:
Input: grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]
Output: 3
'''
grid1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
grid2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]

def numIslands(grid: list) -> int:
    n = 0

    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):

            q = []
            if grid[i][j] == 1:
                q.append((i, j))
                grid[i][j] = 0

                n += 1

                while q:
                    temp_i, temp_j = q.pop(0)
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        coor_x, coor_y = temp_i + x, temp_j + y
                        if coor_x >= 0 and coor_x < row and coor_y >= 0 and coor_y < col and grid[coor_x][coor_y] == 1:
                            q.append((coor_x, coor_y))
                            grid[coor_x][coor_y] = 0
    print(grid)
    return n


if __name__ == '__main__':

    print(numIslands(grid1))
    print(numIslands(grid2))
