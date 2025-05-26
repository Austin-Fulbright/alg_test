from typing import List
from collections import defaultdict
from collections import Counter

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def checkmostfreq(seq):
            val, cnt = Counter(seq).most_common(1)[0]
            return cnt

        n = len(colors)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)

        vis = [0] * n
        vispath = [[""]]* n

        def dfs(u: int, path: str) -> int:
            vis[u] = 1
            path += colors[u]
            maxfreq = checkmostfreq(path) 
            for v in graph[u]:
                if vis[v] == 0:
                    next_freq = dfs(v, path)
                    if next_freq == -1:
                        return -1
                    maxfreq = max(maxfreq, next_freq) 
                elif vis[v] == 1:
                    return -1
            vis[u] = 2
            return maxfreq 
        return dfs(0, "")


        
       
