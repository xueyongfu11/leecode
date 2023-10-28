# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.stack_min == [] or node < self.stack_min[-1]:
            self.stack_min.append(node)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self):
        # write code here
        self.stack_min.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.stack_min[-1]
