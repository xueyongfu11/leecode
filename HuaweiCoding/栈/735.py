class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)):
            if stack == []:
                stack.append(asteroids[i])
                continue

            while stack != [] and stack[-1] > 0 and asteroids[i] < 0 and (abs(stack[-1]) < abs(asteroids[i])):
                stack.pop()

            if stack != [] and stack[-1] > 0 and asteroids[i] < 0 and (abs(stack[-1]) == abs(asteroids[i])):
                stack.pop()
                continue

            if stack != [] and stack[-1] > 0 and asteroids[i] < 0 and (abs(stack[-1]) > abs(asteroids[i])):
                continue
            else:
                stack.append(asteroids[i])

        return stack
