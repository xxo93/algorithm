# -*- coding: utf-8 -*-
"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1 。

案例1:
s = "leetcode"
返回 0

案例2:
s = "loveleetcode",
返回 2
"""


def firstUniqChar(char):
    dic = {}
    for i in char:
        if dic.get(i, None) is None:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)

    for k, v in dic.items():
        if v == 1:
            return char.index(k)

    return -1


if __name__ == '__main__':
    a = 'leetcode'
    print(firstUniqChar(a))

    a = 'loveleetcode'
    print(firstUniqChar(a))

    print('-- over! --')
