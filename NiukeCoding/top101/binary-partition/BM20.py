
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def __init__(self):
        self.n = 0

    def InversePairs(self , nums):
        # write code here
        tmp = [0] * len(nums)
        self.merge(nums, tmp, 0, len(nums) - 1)
        return self.n % 1000000007

    def merge(self, nums, tmp, start, end):
        if start >= end:
            return

        mid = start + (end - start) // 2
        self.merge(nums, tmp, start, mid)
        self.merge(nums, tmp, mid + 1, end)

        s = start
        e = mid + 1
        k = 0
        while s <= mid and e <= end:
            if nums[s] > nums[e]:
                self.n += (mid - s + 1)
                tmp[k] = nums[e]
                e += 1
            else:
                tmp[k] = nums[s]
                s += 1
            k += 1

        while s <= mid:
            tmp[k] = nums[s]
            k += 1
            s += 1

        while e <= end:
            tmp[k] = nums[e]
            k += 1
            e += 1

        m = 0
        for i in range(start, end + 1):
            nums[i] = tmp[m]
            m += 1


