# -*- coding: utf-8 -*-
"""
1711 题目描述：
大餐 是指 恰好包含两道不同餐品 的一餐，其美味程度之和等于 2 的幂。
你可以搭配 任意 两道餐品做一顿大餐。
给你一个整数数组 deliciousness ，其中 deliciousness[i] 是第 i​​​​​​​​​​​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 大餐 的数量。
注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

示例 1：
输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

示例 2：
输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。

提示：
1 <= deliciousness.length <= 10^5
0 <= deliciousness[i] <= 2^20
"""
import time
from collections import Counter


# 执行时间装饰器
def execute_time(func):
    def int_time(*args, **kwargs):
        start_time = time.time()  # 程序开始时间
        ret = func(*args, **kwargs)
        total_time = time.time() - start_time
        print('程序耗时%.8f秒' % total_time)
        return ret

    return int_time


class Solution:
    @execute_time
    def feasting(self, deliciousness: list) -> int:
        """ 递归会超时 """
        # def power1(self, n):
        #     """ 超时。 判断一个数是否是2的幂 """
        #     if n == 2 or n == 1:
        #         return True
        #     if n % 2 == 0:
        #         return self.power(n / 2)
        #     return False

        def power2(self, n):
            """ 超时。 判断一个数是否是2的幂，2^0 = 1 """
            if n > 0:
                return n & (n - 1) == 0
            return False

        length = len(deliciousness)
        res_dict = {}
        num = 0
        for i in range(length):
            for j in range(i + 1, length):
                if power2(deliciousness[i] + deliciousness[j]):
                    num += 1
        print(num)
        # print(res)
        # return len(res)
        return num

    @execute_time
    def countPairs(self, deliciousness: list) -> int:
        """ 字典方法，时间复杂度O(N) """
        # deliciousness.sort()
        # print(deliciousness)
        mod_value = 10 ** 9 + 7
        map_values = Counter(deliciousness)
        print('.....map_values1:', map_values)
        res_list = []

        res = 0
        for value1, value1_count in map_values.items():
            for each_power in range(0, 22):
                exp_of_2 = pow(2, each_power)  # 2的幂
                value2 = exp_of_2 - value1  # 第2个数 = 2的幂 - 第1个数
                if exp_of_2 == 2 * value1:
                    res += value1_count * (value1_count - 1) / 2 % mod_value
                    res_list.append((value1, value2))
                else:
                    value2_count = map_values.get(value2, None)  # 找出第2个数的计数
                    if value2_count:
                        res += value1_count * value2_count % mod_value
                        res_list.append((value1, value2))
            map_values[value1] = 0

        print(res_list)
        return int(res)


if __name__ == '__main__':
    s = Solution()

    arr1 = [1, 3, 5, 7, 9]
    arr2 = [15, 1, 1, 3, 3, 3, 7]
    # arrs = [arr1, arr2, arr3]
    arrs = [arr2]

    # for arr in arrs:
    #     res = s.feasting(arr)
    #     print(res)

    print(s.countPairs(arr2))

    # map_values = Counter(arr3)
    # print('map_values:', map_values)

    print('-- over --')
