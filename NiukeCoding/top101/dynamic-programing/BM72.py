
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self , array ):
        # write code here
        dp = [0] * len(array)
        maxnum = array[0]
        last_index_maxnum = array[0]
        for i, value in enumerate(array):
            if i == 0: 
                dp[i] = value
                continue
                
            dp[i] = max(last_index_maxnum+value, value)
            last_index_maxnum = dp[i]
            maxnum = max(maxnum, dp[i])
        
        return maxnum

