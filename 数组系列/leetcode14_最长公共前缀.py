""" 关键词: 分治，递归，公共前缀
题目14: 最长公共前缀
描述：编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，则返回""
示例1：
    输入: ["flower","flow","flight", "flag"]
    输出: "fl"
示例2：
    输入: ["dog","racecar","car"]
    输出: ""
"""
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """ 借助max(), min(); 利用ASCII码的值进行比较 """
        if not strs:
            return ''

        # 以最小的字符串为基准值
        a = min(strs)
        b = max(strs)

        len_a = len(a)
        for i in range(len_a):
            if a[i] != b[i]:
                return a[0:i]
        return a

    def longestCommonPrefix_DivideConquer(self, strs: list) -> str:
        """ 分治法 """
        if not strs:
            return ''

        def lcp(start, end, arr):
            if start == end:
                return arr[start]

            # 二分
            mid = (start + end) >> 1

            # 分成左右2个区间
            interval_l, interval_r = arr[: mid + 1], arr[mid + 1:]

            # 递归：分别计算左右区间的最长公共前缀，返回公共前缀
            lcp_l, lcp_r = lcp(0, len(interval_l)-1, interval_l), lcp(0, len(interval_r)-1, interval_r)

            # 比较两个公共前缀的最长公共前缀
            minLength = min(len(lcp_l), len(lcp_r))
            for i in range(minLength):
                if lcp_l[i] != lcp_r[i]:
                    return lcp_l[:i]

            return lcp_l[:minLength]

        return lcp(0, len(strs) - 1, strs)


if __name__ == '__main__':
    s = Solution()


    print(s.longestCommonPrefix(["flower","flow","flight", "flag"]))
    print(s.longestCommonPrefix_DivideConquer(["flower", "flow", "flight", "flag"]))

    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    print(s.longestCommonPrefix_DivideConquer(["dog", "racecar", "car"]))

    print('-- over --')
