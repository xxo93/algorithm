class Solution:
    """ 题目14: 最长公共前缀
    描述：编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，则返回""
    示例1：
        输入: ["flower","flow","flight"]
        输出: "fl"
    示例2：
        输入: ["dog","racecar","car"]
        输出: ""
    """

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

        return ''


if __name__ == '__main__':
    s = Solution()

    # res1 = s.longestCommonPrefix(["flower", "flow", "flight"])
    # res1 = s.longestCommonPrefix(["hell", "hello"])
    res1 = s.longestCommonPrefix(["hellss"])
    print(res1)

    # res2 = s.longestCommonPrefix(["dog", "racecar", "car"])
    # print(res2)

    print('-- over --')
