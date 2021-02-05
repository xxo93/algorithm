# -*- coding: utf-8 -*-
def absSort(params_int=None, params_list=None) -> list:
    """
    sort() 时间复杂度：N*log(N)
    params_int: 整数 5
    params_list: 数组 [7, 8, 3, 4, 2, 5, 6, 1]
    """
    # params_int = input().strip()
    # params_list = input().strip()

    """ 方式1 """
    params_list.sort()
    # lambda 排序表达方式1
    def uer_abs(x):
        return abs(x-params_int)
    params_list.sort(key=uer_abs)
    # lambda 排序表达方式2
    params_list.sort(key=lambda x: abs(params_int-x))

    # a = map(lambda x: abs(params_int-x), params_list)
    """ 方法2 """
    for i in range(1, len(params_list)):
        for j in range(i):
            if abs(params_list[i]-params_int) == abs(params_list[i-1]-params_int):
                if params_list[i] < params_list[i-1]:
                    params_list[i], params_list[i-1] = params_list[i-1], params_list[i]
    return params_list


if __name__ == '__main__':

        a, b = 5,       [1, 2, 3, 4, 5, 10, 17, 18, 19]
        print(absSort(a, b))

        a, b = 5,       [7, 8, 3, 4, 2, 5, 6, 1]
        # abs(a-b[i])   [2, 3, 2, 1, 3, 0, 1, 4]
        # return        [5, 4, 6, 3, 7, 2, 8, 1]

        print(absSort(a, b))
        a, b = 100 , [101, 99]

        print(absSort(a, b))

        # print(absSort())
