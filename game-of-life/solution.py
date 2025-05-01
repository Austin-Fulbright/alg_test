from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                aliveNeighbors = 0

                for x in range(max(0, i - 1), min(n, i + 2)): 
                    for y in range(max(0, j - 1), min(m, j + 2)):
                        #check state bit
                        aliveNeighbors += board[x][y] & 1

                if aliveNeighbors == 3 or aliveNeighbors == 4:
                    board[i][j] |= 2

        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1

