#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串一维数组
#

class Solution:
    def restoreIpAddresses(self , s ):
        # write code here
        res = []
        self.func(s, res, 0, [], 0)
        return res

    def func(self, s, res, deep, tmp, index):
        if deep == 3:
            if self.is_valid(s[index:]):
                tmp.append(s[index:])
                res.append('.'.join(tmp))
                tmp.pop(-1)
            return

        for i in range(index+1, len(s)):
            if self.is_valid(s[index:i]):
                tmp.append(s[index:i])
                self.func(s, res, deep+1, tmp, i)
                tmp.pop(-1)

    def is_valid(self, substr):
        if substr == '0' or (not substr.startswith('0') and 0 < int(substr) < 256):
            return True
        else:
            return False

s = Solution()
print(s.restoreIpAddresses("25525522135"))


