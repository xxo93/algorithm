# -*- coding:utf-8 -*-
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
