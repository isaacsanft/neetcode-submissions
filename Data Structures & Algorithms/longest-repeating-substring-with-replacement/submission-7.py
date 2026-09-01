from collections import defaultdict

class Solution:
    def windowSize(self, left, right):
        return right - left + 1

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        counts = defaultdict(int)

        for right in range(len(s)):
            counts[s[right]] += 1

            max_key = max(counts, key = counts.get)
            most_frequent_letter = counts[max_key]

            while (self.windowSize(left, right) - most_frequent_letter) > k:
                counts[s[left]] -= 1
                left += 1
            
            max_len = max(self.windowSize(left, right), max_len)
        
        return max_len


        