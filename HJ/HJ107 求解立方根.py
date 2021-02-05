"""
题目描述
计算一个数字的立方根，不使用库函数。保留一位小数。

输入描述:
待求解参数，为double类型（一个实数）

输出描述:
输入参数的立方根。保留一位小数。

示例1
输入 216
输出 6.0
"""
"""
牛顿迭代法：https://blog.csdn.net/sunbobosun56801/article/details/78088085

"""
import math


def getCubeRoot(num=None):
    # INPUT
    number = float(input().strip())

    # 初始化一个估计解
    t = 5
    while abs(t * t * t - number) > 0.01:
        t = t - (t * t * t * 0.1 - number * 0.1) / (3.0 * t * t)

    # OUTPUT
    print("%.1f" % t)


if __name__ == '__main__':
    getCubeRoot()
    ...
