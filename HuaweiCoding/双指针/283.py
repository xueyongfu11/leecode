class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p_0 = None
        for i in range(len(nums)):
            if p_0 is None and nums[i] == 0:
                p_0 = i
                continue

            if nums[i] != 0 and p_0 is not None:
                nums[p_0] = nums[i]
                nums[i] = 0
                p_0 += 1
        return nums





