# -*- coding: utf-8 -*-
""" 633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：
输入：c = 4
输出：true

示例 3：
输入：c = 3
输出：false

示例 4：
输入：c = 2
输出：true

示例 5：
输入：c = 1
输出：true

提示: 0 <= c <= 2^31 - 1

分析:
根据等式 a^2 + b^2 = c ，可得知 a 和 b 的范围均为 [0, sqrt(c)]
"""
import math


class Solution:
    def judgeSquareSum_enum(self, c: int) -> bool:
        """ 枚举法
            时间复杂度：O(sqrt(c))
            空间复杂度：O(1)O(1)
        """
        max_num = int(math.sqrt(c))
        for a in range(max_num + 1):
            b = int(math.sqrt(c - a ** 2))
            if a ** 2 + b ** 2 == c:
                return True
        return False

    def judgeSquareSum_point(self, c: int) -> bool:
        """ 双指针
        分析可得: a 和 b 的扫描范围均为 [0, sqrt(c)]
        若 a^2 + b^2 = c : 找到符合条件的 a 和 b, 返回 True
        若 a^2 + b^2 > c : 当前值比目标值要小, a++
        若 a^2 + b^2 < c : 当前值比目标值要大, a--
        时间复杂度：O(sqrt(c))
        空间复杂度：O(1)O(1)
        """
        print('---', c)
        # 初始化左右指针
        a, b = 0, int(math.sqrt(c))

        while a <= b:
            if a ** 2 + b ** 2 == c:
                return True
            elif a ** 2 + b ** 2 > c:
                b -= 1
            elif a ** 2 + b ** 2 < c:
                a += 1
        return False


if __name__ == '__main__':
    obj = Solution()

    # print(obj.judgeSquareSum_enum(2))
    # for i in range(5, 0, -1):
    #     print(obj.judgeSquareSum_enum(i))


    # print(obj.judgeSquareSum_point(2))
    for i in range(5, 0, -1):
        print(obj.judgeSquareSum_point(i))
