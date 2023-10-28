class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        forward_p = 0
        back_p = len(height) - 1
        max_c = 0
        while forward_p < back_p:
            max_c = max(max_c, (back_p - forward_p) * min(height[forward_p], height[back_p]))
            if height[forward_p] > height[back_p]:
                back_p -= 1
            else:
                forward_p += 1
        return max_c