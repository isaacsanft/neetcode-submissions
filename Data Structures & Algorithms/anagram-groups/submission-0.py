from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs: # O(n)
            counts = Counter(word)
            key = tuple(sorted(counts.items())) # O(n log n)

            groups[key].append(word)
        
        return list(groups.values())


