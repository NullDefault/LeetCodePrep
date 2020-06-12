"""
~Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = 2 ** 31

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack and self.stack.pop() == self.min_val:
            self.min_val = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def get_min(self):
        """
        :rtype: int
        """
        return self.min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
