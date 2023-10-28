class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]   [89,62,70,58,47,47,46,76,100,70]
        :rtype: List[int]  [8,1,5,4,3,2,1,1,0,0]
        """
        stack = []
        wait_days = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while 1:
                if not stack or temperatures[stack[-1]] >= temperatures[i]:
                    stack.append(i)
                    break
                else:
                    v = stack.pop()
                    wait_days[v] = i - v

        return wait_days


s = Solution()
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
