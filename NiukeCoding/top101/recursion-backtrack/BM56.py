import copy
class Solution:
    def permuteUnique(self , num ):
        # write code here
        res = []
        num.sort()
        flags = [False] * len(num)
        self.func(num, res, [], flags)
        return res

    def func(self, num, res, tmp, flags):
        if len(tmp) == len(num):
            res.append(copy.deepcopy(tmp))
            return

        for i, n in enumerate(num):
            # 最后i-1跟关键，意思是在一个循环中
            if flags[i] or (i > 0 and num[i] == num[i-1] and not flags[i-1]):
                continue

            tmp.append(num[i])
            flags[i] = True
            self.func(num, res, tmp, flags)
            tmp.pop(-1)
            flags[i] = False