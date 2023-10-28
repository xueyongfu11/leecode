class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        """链表是否为空
        :return 如果链表为空 返回真
        """
        return self.head is None

    def length(self):
        """链表长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        """链表头部添加元素
        :param item: 要保存的具体数据
        """
        node = ListNode(item)
        node.next = self.head
        self.head = node


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _map = [('{', '}'), ('(', ')'), ('[', ']')]
        sll = SingleLinkList()
        for c in s:
            if sll.head is None:
                sll.add(c)
                continue
            if (sll.head.val, c) in _map:
                sll.head = sll.head.next
            else:
                sll.add(c)
        if sll.head:
            return False
        else:
            return True


s = Solution()
print(s.isValid('()'))
