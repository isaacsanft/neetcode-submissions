from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                if grid[i][j] == "1":
                    island_deque = deque([(i, j)])
                    while island_deque:
                        node = island_deque.popleft()
                        r, c = node[0], node[1]
                        for dr, dc in directions:
                            new_r = r + dr
                            new_c = c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                                if grid[new_r][new_c] == "1":
                                    island_deque.append((new_r, new_c))
                                visited.add((new_r, new_c))
                    islands += 1
        
        return islands
                                