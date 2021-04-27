
class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n - 1)

    def isExpOf2(self, n: int) -> bool:
        """ 判断n是否为2的幂次方 """
        return n > 0 and n & (n - 1) == 0

    def hammingWeight(self, n: int) -> int:
        """ 使用掩码
        描述：编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
        例1：
            输入：整型数11 (0000 0000 0000 0000 0000 0000 0000 1011)
            输出：3
            解释：输入的二进制串 0000 0000 0000 0000 0000 0000 0000 1011 中，共有三位为 '1'。
        """
        mask = 1
        count = 0
        for _ in range(32):
            if n & mask != 0:
                count += 1
            mask <<= 1
        return count


if __name__ == '__main__':
    s = Solution()

    res = s.sumNums(3)
    print(res)

    exp = s.isExpOf2(1)
    print(exp)

    hamming = s.hammingWeight(11)
    print(hamming)
