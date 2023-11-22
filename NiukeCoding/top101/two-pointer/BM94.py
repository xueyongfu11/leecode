#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self, arr):
        # write code here
        if len(arr) <= 2:
            return 0
        total = 0
        start = 0
        end = len(arr) - 1
        maxL = maxR = 0
        while start < end:
            maxL = max(maxL, arr[start])
            maxR = max(maxR, arr[end])

            if maxL < maxR:
                total += maxL - arr[start]
                start += 1
            else:
                total += maxR - arr[end]
                end -= 1
        return total
