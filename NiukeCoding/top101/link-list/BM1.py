# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类

class Solution:
    def ReverseList(self , head):
        # write code here

        tail = None
        while head:
            next_node = head.next
            cur_node = head
            cur_node.next = tail
            tail = cur_node
            head = next_node
        return tail

