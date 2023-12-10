"""

"""

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        g = {}
        def dfs(root):
            if len(g[root]) == 0: 
                return 
            for neighbor in g[root]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        for e in connections:
            