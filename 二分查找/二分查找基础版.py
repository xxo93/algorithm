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

        return left if nums[left] == item else  -1


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
