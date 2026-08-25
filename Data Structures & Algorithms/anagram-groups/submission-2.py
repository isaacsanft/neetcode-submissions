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
                array[charToIndex(letter)] += 1

            groups[tuple(array)].append(word)
        
        return list(groups.values())


