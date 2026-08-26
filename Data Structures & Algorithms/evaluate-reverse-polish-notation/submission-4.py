class Solution:

    def calculate(self, a: str, b: str, sign: str):
        if sign == "+":
            return a + b
        elif sign == "-":
            return a - b
        elif sign == "*":
            return a * b
        elif sign == "/":
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = {"+", "-", "/", "*"}
        for token in tokens:
            if token in signs:
                    if len(stack) >= 2:
                        b = stack.pop()
                        a = stack.pop()
                        stack.append(self.calculate(a, b, token))
            else:
                stack.append(int(token))

        if stack:
            return stack.pop()


        