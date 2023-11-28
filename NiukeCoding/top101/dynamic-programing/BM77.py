

#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def longestValidParentheses(self , s ):
        # write code here
        if len(s) <= 1:
            return 0

        dp = [0] * len(s)
        stack = [0]
        max_len = 0
        for i in range(1, len(s)):
            c = s[i]
            if stack and s[stack[-1]] == '(' and c == ')':
                stack.pop(-1)
                if stack:
                    dp[i] = max(max_len, i - stack[-1])
                else:
                    dp[i] = max(max_len, i +1)
                max_len = max(max_len, dp[i])
            else:
                stack.append(i)
                dp[i] = max_len
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses('()'))