class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        #让str1为较长的字符串
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        res = ''
        max_len = 0
        #遍历str1的长度
        for i in range(len(str1)):
            #查找是否存在
            if str1[i - max_len : i + 1] in str2:
                res = str1[i - max_len : i + 1]
                max_len += 1
        return res
