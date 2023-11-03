

#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @param pattern string字符串 
# @return bool布尔型
#
class Solution:
    def match(self , str , pattern ):
        # write code here
        

s = Solution()
print(s.match("aaa","a*a"))

class Solution:
    def match(self , str , pattern ):
        if not pattern:                   #1.特殊情况，不存在匹配模式，那么就没有匹配字符串
            return not str
         #2. 递归的终止条件f(1) = 1：在这里就是 首位即匹配。
        first_match = str and pattern[0] in {str[0], '.'}    

        #如果模式长度 >= 2,并且 模式索引[1] == '*'情况，也要分两种：
        if len(pattern) >= 2 and pattern[1] == '*':
            #第一种就是模式长度>2的情况下：字符串完全匹配从模式索引2之后的位置
            return (self.match(str, pattern[2:]) or
                    #或者模式长度 =2的情况下：字符串从索引1位置开始，完全匹配模式
                    first_match and self.match(str[1:], pattern))
        else:
        #否则，模式长度>=2,而模式索引从1开始是 点字符或 *字符在其他位置，
            return first_match and self.match(str[1:], pattern[1:])