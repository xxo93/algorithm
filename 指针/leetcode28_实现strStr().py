# -*- coding: utf-8 -*-
""" 字符串 双指针
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中
找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。
这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0
 
提示：
0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """ 双指针 """
        p, pi = 0, 0
        while p <= (len(haystack) - len(needle)):
            # 记录相同的字符数
            same = 0
            for i in needle:
                s = haystack[pi]
                if s == i:
                    pi += 1
                    same += 1
                else:
                    p += 1
                    pi = p
                    break
            # 如果字符数相同，则存在
            if same == len(needle):
                return p
        return -1


if __name__ == '__main__':
    obj = Solution()

    haystack, needle = 'hello', 'll'
    print(obj.strStr(haystack, needle))

    haystack, needle = 'aaaaa', 'bba'
    print(obj.strStr(haystack, needle))

    haystack, needle = '', ''
    print(obj.strStr(haystack, needle))
