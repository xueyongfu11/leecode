class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        back_p = 0
        last_v = None
        for i in range(len(nums)):
            if i == 0:
                last_v = nums[i]
                continue

            if last_v == nums[i]:
                continue
            else:
                back_p += 1
                nums[back_p] = nums[i]
                last_v = nums[i]
        return back_p + 1


if __name__ == '__main__':
    cost = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    solution.removeDuplicates(cost)