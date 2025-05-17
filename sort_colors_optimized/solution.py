from typing import List
import copy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[i // 3][j // 3].add(num)

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for t in "123456789":
                            if (t not in rows[i] and 
                                t not in cols[j] and 
                                t not in squares[i // 3][j // 3]):
                                rows[i].add(t)
                                cols[j].add(t)
                                squares[i // 3][j // 3].add(t)

                                board[i][j] = t 
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                                rows[i].remove(t)
                                cols[j].remove(t)
                                squares[i // 3][j // 3].remove(t)
                        return False
            return True
        
        solve(board)




                    



