#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def threeSum(self , num ):
        # write code here
        num.sort()
        res = []
        for i in range(len(num)):
            compare_value = -1 * num[i]
            left = i + 1
            right = len(num) - 1
            while right > left:
                if num[left] + num[right] > compare_value:
                    right -= 1
                elif num[left] + num[right] < compare_value:
                    left += 1
                else:
                    tmp = [num[i], num[left], num[right]]
                    right -= 1
                    left += 1
                    if tmp not in res:
                        res.append(tmp)
                    
        return res

s = Solution()
print(s.threeSum([-2,0,1,1,2]))