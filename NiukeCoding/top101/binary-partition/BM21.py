
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self , nums ):
        # write code here
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] == nums[end]:
                if nums[mid+1] < nums[end]:
                    start = mid + 1
                else:
                    end = mid
            else:
                end = mid
        return nums[start]