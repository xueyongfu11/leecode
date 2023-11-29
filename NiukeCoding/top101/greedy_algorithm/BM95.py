# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# pick candy
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def candy(self, arr):
        # write code here
        nums = [1] * len(arr)

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                nums[i] = nums[i - 1] + 1

        for i in range(2, len(arr) + 1):
            if arr[-i] > arr[-i + 1]:
                if nums[-i] <= nums[-i + 1]:
                    nums[-i] = nums[-i + 1] + 1
        return sum(nums)
