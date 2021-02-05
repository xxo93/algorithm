"""
题目描述
每天早上都有很多人去坐电梯,每个人都可能到不同的楼层.
同时电梯还有一个容量限制.电梯最多只能带K个人.
电梯从第a层到第b层,会花费|a-b|的时间.
现在有N个人,以及知道每个人想要去的地方,
请问如何坐电梯,才能使每个人到达到他们对应的楼层,且所花费时间最少.电梯最后要会到第1层.

解答要求
时间限制：1000ms, 内存限制：64MB
输入:
对于每个输入文件,先输入两个整数N,K.表示有N个人,以及电梯的容量K.
接下来一行,有N个整数,f1, f2, … , fn. 表示每个人要到达的地方.
(1 <= N, K <= 2000, 1 <= fi <= 2000)
输出:
输出最小的花费时间.

样例1
输入:
4 2
2 3 4 4
输出:
8
"""


def func():
    n, k = map(int, input().strip().split(' '))
    f = list(map(int, input().strip().split(' ')))
    f.sort(reverse=True)
    num = 0
    for i in range(0, n, k):    # n个人，电梯容量为k
        num += (f[i] - 1) * 2
    print(num)


if __name__ == "__main__":
    s = func()
    # print(s)
