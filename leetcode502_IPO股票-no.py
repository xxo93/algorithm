# -*- coding: utf-8 -*-
""" 贪心 堆
# 134 加油站
502. IPO
假设 力扣（LeetCode）即将开始其IPO。为了以更高的价格将股票卖给风险投资公司，
力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。
帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。

给定若干个项目。对于每个项目 i，它都有一个纯利润 Pi，并且需要最小的资本 Ci 来启动相应的项目。
最初，你有 W 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
总而言之，从给定项目中选择最多 k 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。

示例：
输入：k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].
输出：4
解释：
由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。

提示：
假设所有输入数字都是非负整数。
表示利润和资本的数组的长度不超过 50000。
答案保证在 32 位有符号整数范围内。
"""
from typing import List
from heapq import nlargest, heappop, heappush


class Solution:
    """ 贪心 """
    def findMaximizedCapital_timeout(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """ 数据量大的时候会 超时
        :param k: 项目数目
        :param w: 初始资本
        :param profits: 纯利润
        :param capital: 成本（启动资金）
        :return: 累积资本
        """
        map = list(zip(profits, capital))
        # 按项目纯利润倒序排序
        map.sort(key=lambda x: x[0], reverse=True)
        c = k if k <= len(map) else len(map)
        # 遍历次数，可做项目数
        for _ in range(c):
            for pro, cap in map:
                if w >= cap:
                    w += pro
                    # 找到一个可做项目(项目不可重复做)，做完该项目即移除，进项寻找下个可做项目
                    map.remove((pro, cap))
                    break
        return w

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """ 堆 ？
        一个小根堆存成本
        一个大根堆存利润
        每次取成本小于资本的利润放入大根堆，然后每次取大根堆里的最大利润（贪心）
        最终利润即是答案
        """
        n = len(capital)    # 项目数量

        _heap = []
        for i in range(n):
            # 入堆(按成本)
            heappush(_heap, (profits[i], capital[i]))

        # 遍历次数，可做项目数，项目不可重复做
        for _ in range(min(k, n)):
            for i in range(len(_heap)):
                # 按利润倒序，找出利润最大的那个项目
                [(max_pro, cap)] = nlargest(1, _heap, key=lambda x: x[0])
                if w >= cap:
                    # 做完一个项目就结束
                    w += max_pro
                    break
        return w


if __name__ == '__main__':
    obj = Solution()

    k, w = 2, 0
    profits, capital = [1, 2, 3], [0, 1, 1]
    print(obj.findMaximizedCapital(k, w, profits, capital))
