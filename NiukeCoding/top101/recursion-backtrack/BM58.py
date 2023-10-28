

#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串 
# @return string字符串一维数组
#
class Solution:
    def Permutation(self , str ):
        # write code here
        str = ''.join(sorted(str))
        flags = [False] * len(str)
        res = []
        self.func(str, res, [], flags)
        return res

    def func(self, str, res, tmp, flags):
        if len(tmp) == len(str):
            res.append(''.join(tmp))
            return
        
        for i, c in enumerate(str):
            if flags[i] or (i > 0 and str[i] == str[i-1] and not flags[i-1]):
                continue
            
            tmp.append(c)
            flags[i] = True
            self.func(str, res, tmp, flags)
            tmp.pop(-1)
            flags[i] = False

s = Solution()
print(s.Permutation('abc'))