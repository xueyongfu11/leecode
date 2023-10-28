class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def merge(self, li1, li2):
        if li1 == None:
            return li2
        if li2 == None:
            return li1

        head = ListNode(-1)
        cur = head
        while li1 is not None and li2 is not None:
            if li1.val <= li2.val:
                cur.next = li1
                li1 = li1.next
            else:
                cur.next = li2
                li2 = li2.next
            cur = cur.next

        if li1 is not None:
            cur.next = li1
        if li2 is not None:
            cur.next = li2
        return head.next

    def divide_list(self, lists, left, right):
        if left > right:
            return None
        elif left == right:
            return lists[left]
        else:
            middle = int((left + right) / 2)
            li1 = self.divide_list(lists, left, middle)
            li2 = self.divide_list(lists, middle + 1, right)
            return self.merge(li1, li2)

    def mergeKLists(self, lists):
        return self.divide_list(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    pass
