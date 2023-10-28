class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        head = ListNode(0)
        head.next = pHead1
        cur = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next

        if pHead1 is None:
            cur.next = pHead2
        if pHead2 is None:
            cur.next = pHead1
        return head.next








if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2

    solution.Merge(node1, node1)
