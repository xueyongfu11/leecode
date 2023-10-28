# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param a int整型一维数组
# @param n int整型
# @param K int整型
# @return int整型
#
class Solution:
    def findKth(self, a, n, K):
        return self.binary(a, K, 0, n - 1)

    def binary(self, nums, K, start, end):
        index = self.partition(nums, start, end)
        if K == len(nums) - index:
            return nums[index]
        elif K > len(nums) - index:
            return self.binary(nums, K, start, index - 1)
        else:
            return self.binary(nums, K, start + 1, end)

    def partition(self, nums, start, end):
        pivot = nums[end]

        while start < end:
            while nums[start] <= pivot and start < end:
                start += 1
            nums[end] = nums[start]

            while nums[end] >= pivot and start < end:
                end -= 1
            nums[start] = nums[end]
        nums[end] = pivot
        return end


if __name__ == '__main__':
    s = Solution()
    s.partition([1, 3, 5, 4, 2], 0, 4)
