from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph1 = [-1]*n
        graph2 = [-1]*n
        cur = edges[node1]
        graph1[node1] = 0
        count = 1 
        while(cur != -1 and graph1[cur] == -1):
            graph1[cur] = count
            cur = edges[cur]
            count+=1
        cur = edges[node2]
        graph2[node2] = 0
        count = 1
        while(cur != -1 and graph2[cur] == -1):
            graph2[cur] = count
            cur = edges[cur]
            count+=1
        result = -1
        maxdist = n+1 
        for i in range(n):
            if graph1[i] != -1 and graph2[i] != -1:
                curdist = max(graph1[i], graph2[i])
                if curdist < maxdist:
                    result = i
                    maxdist = curdist 
        return result 
