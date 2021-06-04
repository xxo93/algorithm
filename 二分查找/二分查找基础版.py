# -*- coding: utf-8 -*-

class Solution():
    def binarySearch(self, nums: list, item: int):
        """
        :param nums: 有序数组
        :param item: 目标元素
        :return: 待查找的元素的位置
        """
        # 定义查找范围的左右指针
        left, right = 0, len(nums) - 1

        while left < right:

            # 定义开始二分的中间位置mid
            mid = (left + right) >> 1

            # 中间值小于目标值
            if nums[mid] < item:
                left = mid + 1

            # 中间值大于目标值
            else:
                right = mid

        return left if nums[left] == item else -1

    def binarySearch_loop(self, arr, l, r, x):
        """ 递归实现二分查找
        :param arr: 有序数组
        :param l: 左指针，初始为 0
        :param r: 右指针，初始为 len(arr)
        :param x: 目标值
        :return: 目标值的索引(若存在) 或 -1(若不存在)
        """
        # 基本判断
        if l <= r:

            # mid = int(l + (r - l) / 2)
            mid = (l + r) >> 1

            # 元素正好等于数组中间位置元素
            if arr[mid] == x:
                return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
            elif arr[mid] > x:
                return self.binarySearch_loop(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
            else:
                return self.binarySearch_loop(arr, mid + 1, r, x)

        else:
            # 不存在
            return -1


if __name__ == '__main__':
    obj = Solution()

    arr, target = [1, 3, 5, 7, 8, 9, 12, 15], 5
    print(obj.binarySearch(arr, target))

    arr, target = [1, 3, 5, 7, 8, 9, 12, 15], 6
    print(obj.binarySearch(arr, target))

    arr, target = [1, 3, 5, 7, 8, 9, 12, 15], 12
    print(obj.binarySearch(arr, target))

    arr, target = [1, 3, 5, 7, 8, 9, 12, 15], 13
    print(obj.binarySearch(arr, target))

    arr, target = [1, 3, 5, 7, 8, 9, 9, 9, 12, 18], 9
    print(obj.binarySearch(arr, target))

    # 测试数组
    arr, x = [2, 3, 4, 10, 40], 10
    result = obj.binarySearch_loop(arr, 0, len(arr) - 1, x)
    print(result)
