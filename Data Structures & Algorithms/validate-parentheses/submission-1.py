class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if c == "}" and top == "{" or c == "]" and top == "[" or c == ")" and top == "(":
                        continue
                return False
                
        if stack:
            return False
        
        return True

        