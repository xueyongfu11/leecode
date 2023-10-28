class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        p = None
        n = 0
        pre_v = None
        for i in range(len(nums)):
            if i == 0:
                total += 1
                n += 1
                pre_v = nums[i]
                continue

            if nums[i] == pre_v:
                n += 1

                if p is None:
                    if n > 2:
                        p = i
                    else:
                        total += 1
                else:
                    if n <= 2:
                        total += 1
                        nums[p] = nums[i]
                        p += 1
                    else:
                        pass
            else:
                n = 1
                total += 1
                if p is not None:
                    nums[p] = nums[i]
                    p += 1
            pre_v = nums[i]
        return total

