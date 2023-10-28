class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        li = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack != [] and temperatures[stack[-1]] < temp:
                index = stack.pop()
                li[index] = i - index
            stack.append(i)
        return li

