from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def charToIndex(c: str) -> int:
            return ord(c) - ord('a')

        # n - no. of strs, m - no. of letters in largest word

        groups = defaultdict(list)

        for word in strs: # O(n)
            array = [0] * 26

            for letter in word: # O(m)
                index = charToIndex(letter)
                array[index] += 1

            key = tuple(array)
            groups[key].append(word)
        
        return list(groups.values())


