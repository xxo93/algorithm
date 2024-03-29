# -*- coding: utf-8 -*-
class Solution:
    def strDissipating(self, params_str=None):
        """ 思路：栈
        这个游戏输入一串字符，逐个消去相邻的相同字符对。
        如果字符全部被消完，则输出不带引号的“None”
        输入格式:
        一个字符串，可能带有相邻的相同字符，如“aabbbc”
        输出格式：
        一个字符串，消去了相邻的成对字符，如“bc”
        """
        # params_str = input().strip().lower()
        ele_list = list(params_str)
        print(ele_list)

        res = []
        while len(ele_list) > 0:
            if len(res) == 0:
                res.append(ele_list.pop(0))
            if len(res) > 0 and len(ele_list) > 0:
                if res[-1] == ele_list[0]:
                    res.pop()
                    ele_list.pop(0)
                else:
                    res.append(ele_list.pop(0))

        return ''.join(res) if len(res) > 0 else None


    """ 更优解法 """
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


if __name__ == '__main__':
    obj = Solution()

    a = "aaa"
    print(obj.strDissipating(a))
    print(obj.removeDuplicates(a))

    a = 'ccabbacd'
    print(obj.strDissipating(a))
    print(obj.removeDuplicates(a))

    a = 'aaBbbc'
    print(obj.strDissipating(a))
    print(obj.removeDuplicates(a))

    a = 'ccabbacdYyy'
    print(obj.strDissipating(a))
    print(obj.removeDuplicates(a))
