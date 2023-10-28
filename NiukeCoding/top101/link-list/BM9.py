# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here

        left = head
        right = head
        v = ListNode(-1)
        v.next = left

        while n > 0 and right:
            right = right.next
            n -= 1

        if right is None:
            return left.next

        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return v.next
