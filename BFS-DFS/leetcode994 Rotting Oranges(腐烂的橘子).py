"""
关键词：BFS 数组
难度：中等

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""


class Solution:
    def orangesRotting(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])

        # 存放坏橘子坐标的容器
        queue = []

        # step1
        # 特例, n*n 矩阵 且 没有新鲜橘子, 返回 0
        for each_row in grid:
            if 1 not in each_row:
                return 0

        # step2
        # 遍历所有将坏橘子添加至容器内
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))

        # step3
        tim = -1
        # 遍历容器内的坏橘子 坐标
        while queue:
            queue_len = len(queue)  # 注意点，容器长度变化
            for _ in range(queue_len):
                i, j = queue.pop(0)  # 向前推出腐烂橘子的坐标
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    coo_i, coo_j = i + x, j + y
                    # 排除边界坐标和有新鲜橘子的坐标
                    if coo_i >= 0 and coo_j >= 0 and coo_i < row and coo_j < col and grid[coo_i][coo_j] == 1:
                        grid[coo_i][coo_j] = 2
                        queue.append((coo_i, coo_j))  # 向后添加腐烂橘子的坐标
            tim += 1
        # 判断是否还存在新鲜的橘子(元素为1)
        for each_row in grid:
            if 1 in each_row:
                return -1

        return tim


if __name__ == '__main__':
    s = Solution()
    res1 = s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    res2 = s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    res3 = s.orangesRotting([[0, 2]])
    print(res1)
    print(res2)
    print(res3)
