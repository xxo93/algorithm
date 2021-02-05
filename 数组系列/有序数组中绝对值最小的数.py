class Solution:
    """
    Desc: 找出有序数组中绝对值最小的值
    eg1: [-10, -7, -4, -2, 0, 7, 9]
    eg2: [-8, -3, -1, 2, 3, 5, 9, 10, 11]   len: 9
    eg3: [-8, -3, 0, 2, 3, 5, 9, 10]
    """

    def minAbs_traversing(self, nums: list) -> int:
        """ 遍历法 """

        return 0

    def minAbs_dichotomy(self, nums: list) -> int:
        """ 二分法 """
        if len(nums) == 1:
            return abs(nums[0])
        start_index = 0
        end_index = len(nums) - 1
        while start_index <= end_index:
            mid_index = (start_index + end_index) // 2
            mid_num = nums[mid_index]
            if mid_num == 0:
                return 0
            if mid_num > 0:
                end_index = mid_index - 1
            if mid_num < 0:
                start_index = mid_index + 1

        return min(abs(nums[start_index]), abs(nums[end_index]))


if __name__ == '__main__':
    s = Solution()

    nums_list = [
        [-8, -3, -1, 2, 3, 5, 9, 10, 11],
        [-8, -3, -1, 0, 2, 5, 9],
        [-8, -3, 2, 3, 5, 9, 10],
        [-3, 1, 2],
    ]

    for i, nums in enumerate(nums_list):
        print(f'traversing output:', s.minAbs_dichotomy(nums))


    print('----------------')

    print('-- over! --')
