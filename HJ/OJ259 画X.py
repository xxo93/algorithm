"""
n = 1: 3**0
x
n = 2: 3**1
x x
 x
x x
n = 3: 3**(n-1) * 3**(n-1)
x x   x x
 x     x
x x   x x
   x x
    x
   x x
x x   x x
 x     x
x x   x x
"""


def func(n):
    # n = int(input().strip())
    print('...n:', n)

    matrix = []  # 用一个二维列表来表示结果。3^(n-1)阶矩阵
    # 初始化map，根据题意得到的是一个3^(n-1)x3^(n-1)字符矩阵
    length = pow(3, n - 1)

    for i in range(length):
        matrix.append([' ' for _ in range(length)])

    print(matrix)
    def dfs(level, matrix, r, c):
        '''
        using depth-first-search to solve this problem
        :param level: current level
        :param matrix: the map to be drawn
        :param r: index of row to start in the draw_map
        :param c: index of col to start in the draw_map
        :return:
        '''
        # terminator：递归退出条件
        if level == 1:
            matrix[r][c] = 'X'
            return
        # current level logic
        a_len = pow(3, level - 2)   # 每个B(n-1)块的间距是3^(n-2)
        for row in range(3):        # 每一层都抽象成三行三列的矩阵
            for col in range(3):
                # filter：剪枝，过滤不符合条件的块，即坐标为(0,1)、(1,0)、(1,3)、(2,1) 为空
                if (col == 1 and row != 1) or (row == 1 and col != 1):
                    continue
                # drill down: 进入下一层，注意起始位置是相对上一层的
                dfs(level - 1, matrix, r + row * a_len, c + col * a_len)

    dfs(n, matrix, 0, 0)

    # print(matrix)

    for i in matrix:
        print(''.join(i))


if __name__ == "__main__":
    # s = func()
    # print(s)
    # func(1)
    # func(2)
    func(3)
    func(4)
