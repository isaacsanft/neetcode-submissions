class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 0
            if t[i] not in letters:
                letters[t[i]] = 0
            letters[s[i]] += 1
            letters[t[i]] -= 1
        for value in letters.values():
            if value != 0:
                return False
        return True

        