from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]],edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        graph1 = [[] for _ in range(n)]
        graph2 = [[] for _ in range(m)]
        for u, v in edges1: 
            graph1[u].append(v)
            graph1[v].append(u)
        for u, v in edges2: 
            graph2[u].append(v)
            graph2[v].append(u)
        finalGraph = [-1]*n
        maxin2 = 0
        if (k - 1) >= 0:
            for i in range(m):
                maxin2 = max(maxin2, self.bfs(i, graph2, k - 1))
        for i in range(n):
            count = self.bfs(i, graph1, k)
            finalGraph[i] = count + maxin2 
        return finalGraph 

    def bfs(self, start: int, graph: List[List[int]], k: int) -> int:
        if len(graph) < 1:
            return 1 

        n = len(graph)
        visited = [False]*n
        dist = [-1]*n
        q = deque([start])
        visited[start] = True
        dist[start] = 0
        count = 1

        while q:
            u = q.pop()
            for neighbor in graph[u]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    visited[neighbor] = True
                    dist[neighbor] = dist[u] + 1
                    if dist[neighbor] <= k:
                        count += 1
                    
        return count 


