# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回表达式的值
# @param s string字符串 待计算的表达式
# @return int整型
#


class Solution:
    def solve(self, s):
        s = s.strip()
        stack = []
        res = 0
        num = 0
        sign = '+'
        index = 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            if s[index] == '(':
                end = index + 1
                lens = 1
                while lens > 0:
                    if s[end] == '(':
                        lens += 1
                    if s[end] == ')':
                        lens -= 1
                    end += 1
                num = self.solve(s[index + 1: end - 1])
                index = end - 1
                continue
            if '0' <= s[index] <= '9':
                num = num * 10 + int(s[index])
            if not '0' <= s[index] <= '9' or index == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1 * num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                num = 0
                sign = s[index]
            index += 1
        while stack:
            res += stack.pop()
        return res
