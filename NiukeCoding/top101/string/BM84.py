# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param strs string字符串一维数组
# @return string字符串
#
class Solution:
    def longestCommonPrefix(self, strs):
        # write code here
        if not strs:
            return ''

        prefix = ''
        i = 0
        while True:
            flag = False
            tmp = None
            for string in strs:
                if len(string) <= i:
                    flag = True
                    break
                elif not tmp:
                    tmp = string[i]
                else:
                    if tmp != string[i]:
                        flag = True
                        break
            i += 1

            if not flag:
                prefix += tmp
            else:
                break

        return prefix
