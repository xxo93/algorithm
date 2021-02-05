m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [5,  1,  9,  11],
    [2,  4,  8,  10],
    [13, 3,  6,  7 ],
    [15, 14, 12, 16]
]


class Solution:
    def rotate(self, matrix) -> None:
        """
        desc: 时间复杂度: O(N^2), 空间复杂度: O(1)
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        start = 0
        gap = len(matrix) - 1  # 寻找指针位置
        while gap > 0:
            for i in range(gap):
                matrix[start][start + i], matrix[start + i][start + gap], \
                matrix[start + gap][start + gap - i], matrix[start + gap - i][start] = \
                    matrix[start + gap - i][start], matrix[start][start + i], \
                    matrix[start + i][start + gap], matrix[start + gap][start + gap - i]
            start += 1
            gap -= 2

        print(matrix)


if __name__ == '__main__':
    s = Solution()
    s.rotate(m1)
    s.rotate(m2)
