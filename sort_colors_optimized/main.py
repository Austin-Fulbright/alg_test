# main.py
import sys
import json

from pathlib import Path
from solution import Solution

def load_test_cases(filename):

    current_dir = Path(__file__).parent
    test_cases_path = current_dir / "test_cases.json"

    try:
        with open (test_cases_path, 'r') as f:
            data = json.load(f)
        return data.get("test_case", [])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        sys.exit(1)

def boards_equal(board1, board2):
    if len(board1) != len(board2):
        return False
    for i in range(len(board1)):
        if board1[i] != board2[i]:
            return False
    return True

def main(): 
    sol = Solution()

    test_cases = load_test_cases("test_cases.json")
    for i, test in enumerate(test_cases):
        board = test.get("board")
        expected = test.get("expected")
        print(f"[test {i} nums = {board} expected = {expected}]")
        sol.solveSudoku(board)
        print(f"[solve sudoku board result = {board} and expected = {expected}]")
        if boards_equal(board, expected): 
            print(f"test {i}: \033[92mPass\033[0m")
        else:
            print(f"test {i}: \033[91mFail\033[0m")
    
       

if __name__ == "__main__":
    main()

