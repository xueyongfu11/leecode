# coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self, head):
        # write code here
        if head is None or head.next is None:
            return True

        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        # reverse
        cur = slow.next
        nxt = None
        while cur:
            tmp = cur.next
            cur.next = nxt
            nxt = cur
            cur = tmp
        new_head = nxt

        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True


if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node3.next = node4
    node2.next = node3
    node1.next = node2

    solution.isPail(node1)