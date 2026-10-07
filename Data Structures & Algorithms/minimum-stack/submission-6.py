class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if len(self.minstack) == 0 or self.minstack[-1] >= val:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.minstack[-1]==self.stack[-1]:
            bb=len(self.minstack)-1
            self.minstack = self.minstack[:bb]
        aa = len(self.stack)-1
        self.stack = self.stack[:aa]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]