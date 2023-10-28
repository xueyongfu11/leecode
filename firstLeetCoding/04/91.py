# 纯递归方法
class Solution_v1:
    def __init__(self):
        self.num = 0

    def numDecodings(self, s: str) -> int:

        def recu_decoding(string):
            '''
            每个拆分方法到最后都会剩余一个或者两个字符
            :param string:
            :return:
            '''
            if string[0] == '0':
                return

            if len(string) == 1:
                if string != '0':
                    self.num += 1
                return

            fir_num = string[0]
            sec_num = string[1]

            if len(string) == 2:
                if sec_num == '0':
                    # 只能拆出两个
                    self.num += 1
                else:
                    # 一定可以拆出一个
                    recu_decoding(string[1:])

                    if fir_num == '1':
                        self.num += 1

                    if fir_num == '2' and sec_num in [str(i) for i in range(7)]:
                        self.num += 1
                return

            thr_num = string[2]

            if sec_num == '0':
                # 只能拆出两个
                recu_decoding(string[2:])
            else:
                # 一定可以拆出一个
                recu_decoding(string[1:])

                # 判断是否可以拆出两个
                if fir_num == '1' and thr_num != '0':
                    recu_decoding(string[2:])

                if fir_num == '2' and sec_num in [str(i) for i in range(7)] and thr_num != '0':
                    recu_decoding(string[2:])

        recu_decoding(s)
        print(self.num)
        return self.num


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0

        # dp数组表示，每个索引所对应的值表示，索引+1长度的字符串的解码的个数
        dp = [1 for _ in range(len(s))]
        if len(s) == 1:
            return 1
        if s[1] == '0':
            if s[0] in ['1', '2']:
                dp[1] = 1
            else:
                return 0
        else:
            if int(s[:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1

        for i in range(2, len(s)):
            if s[i] == '0':  # 要组合解码
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:  # 可分开解码
                if s[i - 1] == '0':  # 需分开解码
                    dp[i] = dp[i - 1]
                else:
                    if 10 <= int(s[i - 1:i + 1]) <= 26:  # 组合解码
                        dp[i] = dp[i - 2] + dp[i - 1]
                    else:
                        dp[i] = dp[i - 1]  # 分开解码
        print(dp[-1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    string = '10'
    solution.numDecodings(string)
