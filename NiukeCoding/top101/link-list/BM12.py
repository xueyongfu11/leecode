# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:

    def sortInList(self, head):
        # write code here
        if not head or not head.next: return head

        fast = head.next   # 重要
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        right = self.sortInList(head)
        left = self.sortInList(head2)

        root = ListNode(-1)
        cur = root
        while left and right:
            if left.val > right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return root.next
