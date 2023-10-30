class MinStack(object):

    def __init__(self):
        self.theStack = []
        self.min = 0
        self.hasElement = False
        self.mins = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.theStack.append(val)
        if not self.hasElement or self.min >= val:
            self.mins.append(val)
            self.min = val
            self.hasElement = True
        
    def pop(self):
        """
        :rtype: None
        """
        valRet = self.theStack.pop()
        if valRet == self.min:
            self.mins.pop()
            if len(self.mins) != 0:
                self.min = self.mins[len(self.mins) - 1]
            else:
                self.min = 0
                self.hasElement = False

    def top(self):
        """
        :rtype: int
        """
        return self.theStack[len(self.theStack) - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
