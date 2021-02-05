class Solution:
    """
    描述: 第350题：两个数组的交集: 给定两个数组，编写一个函数来计算它们的交集。
    示例1：
        输入: nums1 = [1,2,2,1], nums2 = [2,2]
        输出: [2,2]
    示例2：
        输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        输出: [4,9]
    """
    def intersections(self, nums1: list, nums2: list) -> list:
        """ 两个无序数组，使用循环遍历 """
        res = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    nums2.remove(num2)
                    res.append(num2)
                    break
        return res

    def intersections_pointer(self, nums1: list, nums2: list) -> list:
        """ 两个数组，变为有序数组，使用指针 """
        # 输入: nums1 = [4,5,9], nums2 = [4,4,8,9,9]
        # 输出: [4,9]
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0

        while (i < len(nums1)) and (j < len(nums2)):
            a = nums1[i]
            b = nums2[j]
            if a == b:
                res.append(a)
                i += 1
                j += 1
            elif a > b:
                j += 1
            elif a < b:
                i += 1
        return res




if __name__ == '__main__':
    s = Solution()

    res = s.intersections([1,2,2,1], [2,2])
    print(res)
    res = s.intersections([4,9,5], [9,4,9,8,4])
    print(res)

    res2 = s.intersections_pointer([1,2,2,1], [2,2])
    print(res2)
    res2 = s.intersections_pointer([4,9,5], [9,4,9,8,4])
    print(res2)
