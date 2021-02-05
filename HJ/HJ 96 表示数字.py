# -*- coding:utf-8 -*-
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
