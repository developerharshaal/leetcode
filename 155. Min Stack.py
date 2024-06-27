class MinStack:

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.min:
            val = min(self.min[-1], val)
        self.min.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




class MinStack:

    def __init__(self):
        self.st = []
        self.mini = 2**31 - 1

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.mini = val
            self.st.append(val)
        else:
            if val < self.mini:
                self.st.append(2*val - self.mini)
                self.mini = val
            else:
                self.st.append(val)

    def pop(self) -> None:
        if len(self.st) == 0:
            return None
        el = self.st[-1]
        self.st.pop()

        if el < self.mini:
            self.mini = 2*self.mini - el
        

    def top(self) -> int:
        if len(self.st) == 0: return
        el = self.st[-1]
        if el < self.mini: return self.mini
        return el

    def getMin(self) -> int:
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()