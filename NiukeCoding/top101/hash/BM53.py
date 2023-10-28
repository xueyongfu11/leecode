

class Solution:
    def minNumberDisappeared(self , nums ):
        # write code here
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            if (abs(nums[i]) < len(nums) + 1) and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.minNumberDisappeared([-1,2,3,4]))