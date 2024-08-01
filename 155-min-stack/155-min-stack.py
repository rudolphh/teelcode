class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1] if self.mins else val))
        
        
    def pop(self):
        """
        :rtype: None
        """
        self.mins.pop()
        return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()