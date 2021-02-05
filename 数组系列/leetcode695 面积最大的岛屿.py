""" # BFS/DFS
695. 岛屿的最大面积
思路：队列进行BFS

给定一个包含了一些 1 和 0 的费控二维数组 grid。

一个岛屿是由相邻的 1 （代表土地）构成的组合，协力的[相邻]要求两个 1 必须在 水平 或 竖直方向上相邻 。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二位数组中的最大面积。如果没有岛屿，则返回面积为 0 。

注：
1. 只能水平和竖直方向才是相邻
2. 每个维度不超过 50 。

Example 1:
输入：
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：return 6

Example 2:
输入：[[0,0,0,0,0,0,0,0]]
输出：return 0
"""
# BFS 解法
# 8*13
grid1 = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
grid2 = [
    [0, 0, 0, 0, 0, 0, 0, 0]
]


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])

        # 记录总面积
        total_area = 0

        for i in range(row):
            for j in range(col):

                # 初始化面积
                area = 0
                # 记录值为 1 的坐标点
                queue = []

                # 从第一个 1 找起
                if grid[i][j] == 1:
                    area += 1
                    grid[i][j] = 0
                    queue.append((i, j))

                    while queue:

                        cur_i, cur_j = queue.pop(0)

                        # 搜索上下左右的点坐标是否为 1
                        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            temp_i, temp_j = cur_i + x, cur_j + y

                            # 排除边界坐标且坐标为1的点
                            if temp_i >= 0 and temp_j >= 0 and temp_i < row and temp_j < col and grid[temp_i][temp_j] == 1:
                                grid[temp_i][temp_j] = 0
                                area += 1
                                queue.append((temp_i, temp_j))  # 向后添加新面积的坐标

                # 选取面积较大的记录下来。每计算得到一次面积进行保存一次
                total_area = max(total_area, area)

        return total_area


if __name__ == '__main__':
    s = Solution()
    res1 = s.maxAreaOfIsland(grid1)
    res2 = s.maxAreaOfIsland(grid2)
    print('res1:', res1)
    print('res2:', res2)
