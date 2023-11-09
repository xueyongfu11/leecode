

#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param height int整型一维数组 
# @return int整型
#
class Solution:
    def maxArea(self , height ):
        # write code here
        max_value = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_value = max(max_value, (right-left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_value


s = Solution()
print(s.maxArea([6,4,3,1,4,6,99,62,1,2,6]))

