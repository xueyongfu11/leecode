#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#

class Solution:
    def solve(self , nums):
        if nums == "0":  
            return 0
        if nums == "10" or nums == "20":   
            return 1
        for i in range(1, len(nums)): 
            if nums[i] == '0':
                if nums[i - 1] != '1' and nums[i - 1] != '2':
                    return 0
        
        dp = [0] * len(nums)
        for i, char in enumerate(nums):
            if i == 0:
                dp[i] = 1
                continue

            if i == 1:
                if (int(nums[i-1]) == 2 and int(char) > 6) or int(nums[i-1]) > 2 or int(nums[i-1]) == 0:
                    dp[i] = 1
                else:
                    if int(nums[i]) == 0:
                        dp[i] = 1
                    else:
                        dp[i] = 2
                continue
            
            # just not merge
            if (int(nums[i-1]) == 2 and int(char) > 6) or int(nums[i-1]) > 2 or int(nums[i-1]) == 0:
                dp[i] = dp[i-1]
            else:
                if int(char) == 0:   # must merge
                    dp[i] = dp[i-2]
                else:
                    # can merge: if merge: dp[i-2]  if not merge: dp[i-1]
                    dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]


s = Solution()
print(s.solve("12"))