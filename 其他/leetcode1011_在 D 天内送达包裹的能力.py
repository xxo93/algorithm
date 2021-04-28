# -*- coding: utf-8 -*-
""" 
@Author: wwx800191
@Date: 2021/4/26
@Desc:
附两道一毛一样的题目:  875. 爱吃香蕉的珂珂; 1231. 分享巧克力 (会员题)
模板代码:
class Solution:
    def can(self, cap, weights, D):
        cur, days = 0, 1  # 记得第一天开始
        for w in weights:
            if cur+w <= cap:
                cur += w
            else:
                cur = w   # 别忘了要载货
                days += 1
            if days > D: return False # 剪枝
        return True

    def shipWithinDays(self, weights, D):
        l, r = max(weights), sum(weights) # 至少要一天载最重的那一个
        while l<=r:                       # 套模版：最左边的can()=True
            m = (l+r) >> 1
            if self.can(m, weights, D):
                r = m-1
            else:
                l = m+1
        return l
# #################################################################################
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 最小值得是任何一个货物都可以运走, 不可以分割货物
        start = max(weights)
        # 最大值是一趟就全部运走, 所以是所有货物之和
        end = sum(weights)
        # 二分法模板
        while start < end:
            # 先求中间值
            mid = (start + end)//2

            # 计算这个中间值需要计算需要多少天运完
            days = self.countDays(mid, weights)
            # 如果天数超了, 说明运载能力有待提升, start改大一点, 继续二分搜索
            if days > D:
                start = mid + 1
            # 否则运载能力改小一点继续搜索
            else:
                end = mid
        return start

    def countDays(self, targetWeight, weights):
        days = 1
        current = 0
        for weight in weights:
            current += weight
            if current > targetWeight:
                days += 1
                current = weight
        return days

# #################################################################################
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。
传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。
我们装载的重量不会超过船的最大运载重量。
返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

示例 1：
输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10
请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。

示例 2：
输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

示例 3：
输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

提示：
1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

"""
"""
我们将「最少需要运送的天数」与 D 进行比较，就可以解决这个判定问题。
当其小于等于 D 时，我们就忽略二分的右半部分区间；
当其大于 D 时，我们就忽略二分的左半部分区间。

- 细节

二分查找的初始左右边界应当如何计算呢？

对于左边界而言，由于我们不能「拆分」一个包裹，因此船的运载能力不能小于所有包裹中最重的那个的重量，即左边界为数组 weights 中元素的最大值。

对于右边界而言，船的运载能力也不会大于所有包裹的重量之和，即右边界为数组 weights 中元素的和。

我们从上述左右边界开始进行二分查找，就可以保证找到最终的答案。

"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        # 确定左右边界: 运输一次的最小的运载能力的可能性区间
        left, right = max(weights), sum(weights)

        # 进行二分查找
        while left < right:
            # need: 需要的天数；curr: 当前运载的货物
            need_day, curr = 1, 0
            # 获取中间的运载能力, 查找所需要的运载能力
            mid = (left + right) >> 1

            for w in weights:
                # 計算當前貨物重量
                curr += w
                # 当前货物重量大于运载能力，需要的天数+1。当前货物重量重置成下一天的第1件货物重量
                if curr > mid:
                    need_day += 1
                    curr = w

            # 如果 need_day > D ，运载能力有待提高，left = mid
            if need_day > D:
                left = mid + 1
            # 否则运载能力降低，继续二分搜索
            else:
                right = mid
        print(left)
        return left


if __name__ == '__main__':
    obj = Solution()

    weights, D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5
    obj.shipWithinDays(weights, D)  # 15

    weights, D = [3, 2, 2, 4, 1, 4], 3
    obj.shipWithinDays(weights, D)  # 6

    weights, D = [1, 2, 3, 1, 1], 4
    obj.shipWithinDays(weights, D)  # 3
