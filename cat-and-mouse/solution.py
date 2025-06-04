from typing import List
from collections import deque
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int: 
        mouse = 1
        cat = 2
        hole = 0
        def dfs(node, visited):
            if node == 0:
                return [0] 
            best_path = None 
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    subpath = dfs(neighbor, visited)
                    if subpath is not None:
                        candidate = [node] + subpath
                    if best_path is None or len(candidate) < len(best_path):
                        best_path = candidate 
            visited.remove(node)
            return best_path

        get_best_path = dfs(mouse, set()) 
        
        print(get_best_path)

        return 0 
