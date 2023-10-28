

class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(len(nums)):
            max_v = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] > max_v:
                        max_v = dp[j]
            dp[i] = max_v + 1
        print(dp)
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = solution.lengthOfLIS(nums)
    print(res)
