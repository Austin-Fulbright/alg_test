import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):

        n = len(moveTime)
        m = len(moveTime[0])

        dp = [[float('inf')] * m for _ in range(n)]

        minh = [] 
        heapq.heappush(minh, (0, 0, 0))
        dp[0][0] = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while minh: 
            r, c, time = heapq.heappop(minh)

            if r == n - 1 and c == m - 1:
                return time

            dp[r][c] = time

            for rd, cd in directions:
                i = rd + r
                j = cd + c
                if 0 <= i < n and 0 <= j < m and dp[i][j] == float('inf'):
                    time_next = max(time, moveTime[i][j]) + 1
                    print(f"({i}, {j}) = {time_next} ")
                    heapq.heappush(minh, (i, j, time_next))
        return -1
