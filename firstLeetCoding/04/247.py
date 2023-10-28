class Solution:
    def numDecodings(self, n, m) -> list:
        if m == 1:
            return ['0', '1', '8']
        if m == 2:
            if n > m:
                return ['00', '11', '69', '88', '96']
            return ['11', '69', '88', '96']

        values = self.numDecodings(n, m - 2)

        new_values = []
        for v in values:
            if n > m:
                new_values.append('0' + v + '0')
            new_values.append('1' + v + '1')
            new_values.append('6' + v + '9')
            new_values.append('8' + v + '8')
            new_values.append('9' + v + '6')
        return new_values


if __name__ == '__main__':
    solution = Solution()
    num = 6
    res = solution.numDecodings(num, num)
    print(res)
