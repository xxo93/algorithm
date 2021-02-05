# -*- coding: utf-8 -*-
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



