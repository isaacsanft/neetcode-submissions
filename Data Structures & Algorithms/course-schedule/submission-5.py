from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        adj = defaultdict(set)
        in_degree = defaultdict(int)
        head = set(range(numCourses))
        count = 0

        for course, prereq in prerequisites:
            head.discard(course)
            adj[prereq].add(course)
            in_degree[course] += 1
        
        if len(head) == 0:
            return False

        queue = deque(list(head))
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses
