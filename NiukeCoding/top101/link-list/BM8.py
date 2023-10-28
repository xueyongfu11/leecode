# coding:utf-8
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
# class Solution:
#     def FindKthToTail(self , pHead , k ):
#         # write code here
#
#         length = 0
#         cur = pHead
#         while cur:
#             cur = cur.next
#             length += 1
#
#         if length >= k:
#             count = length - k
#             while count > 0:
#                 pHead = pHead.next
#                 count -= 1
#             return pHead
#         else:
#             return None


# 双指针法
class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here

        left = pHead
        right = pHead
        if k == 0:
            return None

        k -= 1
        while k > 0 and right:
            right = right.next
            k -= 1

        if right is None:
            return None

        while right.next:
            right = right.next
            left = left.next
        return left
