


class Solution:
    def trans(self , s: str, n: int) -> str:
        if n==0:
            return s
        res = ""
        for i in range(n):
            if s[i] <= 'Z' and s[i] >= 'A':
                res += chr(ord(s[i]) - ord('A') + ord('a'))
            elif s[i] >= 'a' and s[i] <= 'z':
                res += chr(ord(s[i]) - ord('a') + ord('A'))
            else :
                res+=s[i]
        res = list(res.split(' '))[::-1]
        print(res)
        return ' '.join(res)

