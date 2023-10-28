
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self , input , k ):
        # write code here
        import heapq
        if k >= len(input):
            return input

        if k == 0:
            return []

        pg = []
        for i in range(k):
            heapq.heappush(pg, input[i] * -1)

        for i in range(k, len(input)):
            if (-1 * pg[0]) > input[i]:
                heapq.heapreplace(pg, -1 * input[i])

        res = []
        for i in range(k):
            res.append(-1 * pg[0])
            heapq.heappop(pg)
        return res
