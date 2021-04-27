# -*- coding: utf-8 -*-
""" 双指针
第344题：反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
01、题目分析
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

示例1:
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

示例2:
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""

def revertStr(s):
    length =len(s)
    left = 0
    right = length-1

    print('before:', s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -= 1
    print('after:', s)
    return s

if __name__ == '__main__':

    revertStr(["h","e","l","l","o"])
    revertStr(["H","a","D","n","c","h"])
