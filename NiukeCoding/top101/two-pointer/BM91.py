

#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 反转字符串
# @param str string字符串
# @return string字符串
#
class Solution:
    def solve(self , str ):
        # write code here
        tmp = []
        for i in range(len(str), 0, -1):
            i -= 1
            tmp.append(str[i])
        return ''.join(tmp)