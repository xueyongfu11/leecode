class Solution:
    def isIPv4(self, IP: str):
        s = IP.split('.')
        # IPv4必定为4组
        if len(s) != 4:
            return False
        for i in range(len(s)):
            # 不可缺省，有一个分割为零，说明两个点相连
            if len(s[i]) == 0:
                return False
            # 比较数字位数及不为零时不能有前缀零
            if len(s[i]) < 0 or len(s[i]) > 3 or (s[i][0] == '0' and len(s[i]) != 1):
                return False
            # 遍历每个分割字符串，必须为数字
            for j in range(len(s[i])):
                if s[i][j] < '0' or s[i][j] > '9':
                    return False
            # 转化为数字比较，0-255之间
            num = int(s[i])
            if num < 0 or num > 255:
                return False
        return True

    def isIPv6(self, IP: str):
        s = IP.split(':')
        # IPv6必定为8组
        if len(s) != 8:
            return False
        for i in range(len(s)):
            # 每个分割不能缺省，不能超过4位
            if len(s[i]) == 0 or len(s[i]) > 4:
                return False
            for j in range(len(s[i])):
                # 不能出现a-fA-F以外的大小写字符
                if not (s[i][j].isdigit() or s[i][j] >= 'a' and s[i][j] <= 'f' or s[i][j] >= 'A' and s[i][j] <= 'F'):
                    return False
        return True

    def solve(self, IP: str) -> str:
        if len(IP) == 0:
            return "Neither"
        if Solution.isIPv4(self, IP):
            return "IPv4"
        elif Solution.isIPv6(self, IP):
            return "IPv6"
        return "Neither"
