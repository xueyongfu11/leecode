
from typing import List

class Solution:
    def FindNumsAppearOnce(self , array: List[int]) -> List[int]:
        mp = dict()
        res = list()
        #遍历数组
        for i in range(len(array)):
            #统计每个数出现的频率
            if array[i] in mp:
                mp[array[i]] += 1
            else:
                mp[array[i]] = 1
        #再次遍历数组
        for i in range(len(array)):
            #找到频率为1的两个数
            if mp[array[i]] == 1:
                res.append(array[i])
        #整理次序
        res.sort(reverse=False)
        return res
