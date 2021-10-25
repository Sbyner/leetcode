class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        if self.mins:
            if self.mins[-1] >= val:
                self.mins.append(val)
        else:
            self.mins.append(val)
            
    def pop(self) -> None:
        val = self.data.pop()
        if val == self.mins[-1]:
            self.mins.pop()
            
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
