class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = float("inf")

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_element))
        if val < self.min_element:
            self.min_element = val 

    def pop(self) -> None:
        value = self.stack.pop()
        if value[0] == self.min_element:
            self.min_element = value[1]
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.min_element