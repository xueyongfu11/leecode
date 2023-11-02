
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr ):
        # write code here
        nums = set()
        slow = fast = 0
        max_len = 0
        while fast < len(arr):
            if slow == fast:
                nums.clear()
                nums.add(arr[slow])
            elif arr[fast] in nums:
                max_len = max(max_len, fast - slow)
                while arr[slow] != arr[fast]:
                    nums.remove(arr[slow])
                    slow += 1
                slow += 1
            else:
                nums.add(arr[fast])
            fast += 1
        max_len = max(max_len, fast - slow)
        return max_len
