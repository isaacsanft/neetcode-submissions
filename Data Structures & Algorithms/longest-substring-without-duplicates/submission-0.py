from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        counts = defaultdict(int)

        while right < len(s):

            counts[s[right]] += 1

            if counts[s[right]] > 1:
                if s[left] == s[right]:
                    left += 1
                    counts[s[right]] -= 1
                else:
                    while s[left] != s[right]:
                        counts[s[left]] -= 1
                        left += 1
                    counts[s[left]] -= 1
                    left += 1 

            window_size = right - left + 1

            if window_size > max_len:
                max_len = window_size
            
            right += 1
            
        return max_len

