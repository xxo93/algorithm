# -*- coding: utf-8 -*-
""" 双指针
【HJ96 表示数字】
题目描述
将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变
注意：输入数据可能有多行
输入描述:
输入一个字符串

输出描述:
字符中所有出现的数字前后加上符号“*”，其他字符保持不变

示例1
输入
Jkdi234klowe90a3
输出
Jkdi*234*klowe*90*a*3*
"""


def fun_stacks():
    while 1:
        """ 方法1：栈 """
        n = list(input().strip())

        res = []
        while len(n) > 0:
            ele = n.pop(0)

            if len(res) == 0 and ele.isalpha():
                res.append(ele)
            elif len(res) == 0 and ele.isdigit():
                res.append('*')
                res.append(ele)
            elif len(res) != 0 and len(n) == 0 and ele.isdigit():
                res.append('*')
                res.append(ele)
            elif len(res) != 0 and ((res[-1].isalpha() and ele.isdigit()) or (res[-1].isdigit() and ele.isalpha())):
                res.append('*')
                res.append(ele)
            else:
                res.append(ele)

        if len(res) != 0 and res[-1].isdigit():
            res.append('*')

        print(''.join(res))


def fun_pointers():
    while 1:
        """ 方法1：指针 """
        n = list(input().strip())

        res = []
        while len(n) > 0:
            pass

        print(''.join(res))


if __name__ == '__main__':
    fun_stacks()

    fun_pointers()

# ******************************************************************* #

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

# ******************************************************************* #

"""
【HJ102 字符统计】
请编写程序，找出一段给定文字中出现最频繁的那个英文字母。
输入格式：
输入在一行中给出一个长度不超过1000的字符串。字符串由ASCII码表中任意可见字符及空格组成，至少包含1个英文字母，以回车结束（回车不算在内）。

输出格式：
在一行中输出出现【频率最高】的那个英文字母及其出现【次数】，其间以空格分隔。如果有并列，则输出按字母序最小的那个字母。统计时不区分大小写，输出小写字母。

输入样例：
This is a simple TEST.  There ARE numbers and other symbols 1&2&3...........
输出样例：
e 7
"""

char = input()

dic = {}
for i in char:
    i = i.lower()
    if i.isalpha():
        if dic.get(i, None) is None:
            dic[i] = 1
        else:
            dic[i] += 1

max_fre = max(dic.values())

alpha = []
for k, v in dic.items():
    if v == max_fre:
        alpha.append(k)

print(min(alpha), max_fre)

# 字典排序
# dic = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
# print(dic)


# ******************************************************************* #

""" 最大上升子序列
题目描述
Redraiment是走梅花桩的高手。Redraiment总是起点不限，从前到后，往高的桩子走，但走的步数最多，不知道为什么？
你能替Redraiment研究他最多走的步数吗？

Example 1:
Input:
6
2 5 1 5 4 5
Output:
3
Explanation:
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5
从第5格开始走最多有2步,4 5
所以这个结果是3。
"""

while 1:
    length = int(input().strip())
    arr = input().strip().split()
    # print(length, arr)

    if length <= 1:
        print(length)
        continue

    nums = [int(i) for i in arr]
    print(length, nums)

    dp = [1 for _ in range(length)]

    for i in range(length):
        for j in range(i):
            if nums[j] < nums[i]:
                # [2, 5, 1, 5, 4, 5]
                dp[i] = max(dp[j] + 1, dp[i])

    print('dp:', dp)
    print(max(dp))
    continue
