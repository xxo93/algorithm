# -*- coding: utf-8 -*-
"""
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。
平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，
若有一个气球的直径的开始和结束坐标为 Xstart，Xend， 且满足 Xstart ≤ x ≤ Xend，则该气球会被引爆。
可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。
我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

Example:
输入: [[10,16], [2,8], [1,6], [7,12]]
输出: 2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
"""
"""
类似于区间调度问题，使用贪心算法：
首先对所有气球按照起始坐标大小排序，然后每次总是优先选择起始坐标小的气球中的右边坐标，然后再选择下一个；

维护一个设计区间
"""
s = [
    [10, 16],
    [7, 12],
    [2, 8],
    [1, 6],
]


class Solution:
    def findMinArrowShots(self, points: list) -> int:

        if len(points) <= 1:
            return len(points)
        points.sort()

        # 记录射击次数
        count = 1

        # 初始化的射击区间
        shoot_ran = points[0]

        # 遍历 points[1:] 的气球
        for cur_ball in points[1:]:
            # 该气球与射击区间存在交集，即气球的左端点<=射击区间的右端点
            if cur_ball[0] <= shoot_ran[1]:
                p_start = max(cur_ball[0], shoot_ran[0])
                p_end = min(cur_ball[1], shoot_ran[1])
                # 更新射击区间
                shoot_ran = [p_start, p_end]
            else:
                # 更新新的射击区间，并添加射击次数
                count += 1
                shoot_ran = cur_ball

        return count





if __name__ == '__main__':
    s = Solution()

    nums_list = [
        [[10, 16], [2, 8], [1, 6], [7, 12]],
        [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]],
    ]

    for i, nums in enumerate(nums_list):
        print(f'output:', s.findMinArrowShots(nums))

    print('----------------')

    print('-- over! --')
