

class Solution:
    def solve(self , s: str, t: str) -> str:
        #若是其中一个为空，返回另一个
        if len(s) == 0:
            return t
        if len(t) == 0:
            return s
        #让s为较长的，t为较短的
        if len(s) < len(t):
            temp = t
            t = s
            s = temp
        #进位标志
        carry = 0
        i = len(s) - 1
        #从后往前遍历较长的字符串
        while i>=0 :
            #转数字加上进位
            temp = ord(s[i]) - ord('0') + carry
            #转较短的字符串相应的从后往前的下标
            j = i - len(s) + len(t)
            #如果较短字符串还有
            if j >= 0:
                #转数组相加
                temp += ord(t[j]) - ord('0')
            #取进位
            carry = int(temp / 10)
            #去十位
            temp = temp % 10
            s = s[:i] + chr(temp + ord('0')) + s[i+1:]
            i -= 1
        #最后的进位
        if carry == 1:
            s = '1' + s
        return s
