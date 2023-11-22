

from functools import cmp_to_key

class Solution:
    def merge(self , intervals):
        res = list()
        #去除特殊情况
        if len(intervals) == 0:
            return res
        #按照区间首排序
        intervals.sort(key=cmp_to_key(lambda a,b:a.start - b.start))
        #放入第一个区间
        res.append(intervals[0])
        #遍历后续区间，查看是否与末尾有重叠
        for i in range(len(intervals)):
            #区间有重叠，更新结尾
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            #区间没有重叠，直接加入
            else:
                res.append(intervals[i])
        return res


