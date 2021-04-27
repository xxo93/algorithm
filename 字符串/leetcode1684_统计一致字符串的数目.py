# -*- coding: utf-8 -*-
"""
给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。
如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致 字符串。
请你返回 words 数组中 一致 字符串的数目。

示例 1：
输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。

示例 2：
输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。

示例 3：
输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。

提示：
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
allowed 中的字符 互不相同 。
words[i] 和 allowed 只包含小写英文字母
"""

def countConsistentStrings(allowed: str, words: list) -> int:
    a = list(allowed)
    num = 0
    for word in words:
        # 字符去重
        w = set(word)
        s = 0
        for i in w:
            if i in a:
                s += 1
        if s == len(w):
            num += 1

    print(num)
    return num

def countConsistentStrings_优化(allowed: str, words: list) -> int:
    n = 0
    for word in words:
        n += 1
        for l in word:
            if l not in allowed:
                n -= 1
                break
    print('优化：', n)
    return n


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    countConsistentStrings(allowed, words)
    countConsistentStrings_优化(allowed, words)

    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    countConsistentStrings(allowed, words)
    countConsistentStrings_优化(allowed, words)


    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    countConsistentStrings(allowed, words)
    countConsistentStrings_优化(allowed, words)
