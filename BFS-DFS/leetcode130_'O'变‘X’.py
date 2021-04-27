# -*- coding: utf-8 -*-
""" 
@Author: wwx800191
@Date: 2021/3/30
@Desc: 
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (0, -1),  # 左边
            (0, +1),  # 右边
            (-1, 0),  # 上边
            (+1, 0),  # 下边
        ]
        row, col = len(board), len(board[0])
        visited = set()

        def add_visited(pointer):
            """
                将边界点pointer周围联通的所有的‘O’都添加到visited集合里面去,方便以后dfs去过滤
            """
            x, y = pointer
            visited.add(pointer)
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and board[new_x][new_y] == 'O' and (
                        new_x, new_y) not in visited:
                    add_visited((new_x, new_y))

        def dfs(x, y):
            """
            将非边界点（x, y）周围的所有联通的'O'都置为'X'
            """
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and board[new_x][new_y] == 'O' and (
                        new_x, new_y) not in visited:
                    board[new_x][new_y] = 'X'
                    dfs(new_y, new_y)

        # 第一步将边界上面的所有的节点添加到visited数组里面去
        for i in range(col):
            if board[0][i] == 'O':
                add_visited((0, i))
            if board[row - 1][i] == 'O':
                add_visited((row - 1, i))
        for i in range(row):
            if board[i][0] == 'O':
                add_visited((i, 0))
            if board[i][col - 1] == 'O':
                add_visited((i, col - 1))
        # 再遍历整个图，若此时找到'O'，我们再进行搜索，搜索还是按照模板
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
                    dfs(i, j)
        return board

if __name__ == '__main__':

    obj = Solution()
    board = [
        ['O', 'O', 'O', 'X'],
        ['O', 'X', 'O', 'O'],
        ['O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O'],
    ]
    obj.solve(board)
