

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) -1
        while start < end:
            tem = s[start]
            s[start] = s[end]
            s[end] = tem
            start += 1
            end -= 1
        return s


if __name__ == '__main__':
    cost = ["h","e","l","l","o"]
    solution = Solution()
    solution.reverseString(cost)