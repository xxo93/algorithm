# -*- coding:utf-8 -*-
"""
【HJ99 自守数】
描述：自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。
功能：请求出n以内的自守数的个数
"""

n = input()
n_int = int(n)

res = 0
for i in range(n_int):
    ge_res = str(i ** 2)  # 平方后的个位数
    if ge_res.endswith(str(i)):
        res += 1

    print(i, ge_res)

print('+++', res)
