# -*- coding: utf-8 -*-
"""
给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
在执行完所有删除操作后，返回最终得到的字符串。
本题答案保证唯一。

示例 1：
输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。

示例 2：
输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"

示例 3：
输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"

提示：
1 <= s.length <= 10^5
2 <= k <= 10^4
s 中只含有小写英文字母。
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i, e in enumerate(s, 1):
            if stack and stack[-1][0] == e:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([e, 1])


        return ''.join(i[0]*i[1] for i in stack)


if __name__ == '__main__':
    obj = Solution()

    s, k = "abcd", 2
    print(obj.removeDuplicates(s, k))

    s, k = "deeedbbcccbdaa", 3
    print(obj.removeDuplicates(s, k))

    s, k = "pbbcggttciiippooaais", 2
    print(obj.removeDuplicates(s, k))

    ...
