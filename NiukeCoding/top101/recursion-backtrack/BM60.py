
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return string字符串一维数组
#
class Solution:
    def generateParenthesis(self , n):
        # write code here
        res = []
        self.func(n, res, 0, 0, [])
        return res


    def func(self, n, res, left, right, tmp):
        if len(tmp) == 2*n:
            if left == n and right==n:
                res.append(''.join(tmp))
            return

        left += 1
        tmp.append('(')
        if self.is_valid(n, left, right):
            self.func(n, res, left, right, tmp)
        tmp.pop(-1)
        left -= 1

        right += 1
        tmp.append(')')
        if self.is_valid(n, left, right):
            self.func(n, res, left, right, tmp)
        tmp.pop(-1)
        right -= 1

    def is_valid(self, n, left, right):
        if right > n or right > n or right > left:
            return False
        return True

