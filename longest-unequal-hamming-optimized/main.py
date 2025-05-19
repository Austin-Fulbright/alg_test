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

def main():
    sol = Solution()

    test_cases = load_test_cases("test_cases.json")
    for i, test in enumerate(test_cases):
        words = test.get("words")
        groups = test.get("groups")
        expected = test.get("expected")
        print(f"[test {i} words = {words} groups = {groups} expected = {expected}]")
        result = sol.getWordsInLongestSubsequence(words, groups)
        print(f"[sort colors result = {result} and expected = {expected}]")
        isEqual = True
        if len(result) != len(expected):
            isEqual = False
        for i in range(len(result)):
            if expected[i] != result[i]:
                isEqual = False
                break
        if isEqual: 
            print(f"test {i}: \033[92mPass\033[0m")
        else:
            print(f"test {i}: \033[91mFail\033[0m")
    
       

if __name__ == "__main__":
    main()

