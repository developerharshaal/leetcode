class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


#OPTIMIZED CODE

class MyQueue:

    def __init__(self):
        self.inp = []
        self.out = []

    def push(self, x: int) -> None:
        self.inp.append(x)

    def pop(self) -> int:
        if self.out:
            return self.out.pop()
        else:
            while self.inp:
                self.out.append(self.inp.pop())
            return self.out.pop()

    def peek(self) -> int:
        if self.out:
            return self.out[-1]

        else:
            while self.inp:
                self.out.append(self.inp.pop())
            return self.out[-1]
        

    def empty(self) -> bool:
        return not self.inp and not self.out
        
