class Solution:

    def notAlphanum(self, c: str) -> bool:
        if 48 <= ord(c.lower()) <= 57 or 97 <= ord(c.lower()) <= 122:
            return False
        return True

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and self.notAlphanum(s[left]):
                left += 1
            while left < right and self.notAlphanum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True

        