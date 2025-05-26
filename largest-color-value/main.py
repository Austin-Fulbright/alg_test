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
        colors = test.get("colors")
        edges = test.get("edges")
        expected = test.get("expected")
        result = sol.largestPathValue(colors, edges)
        print(f"[largest path value: result = {result} and expected = {expected}]")
        if result == expected: 
            print(f"test {i}: \033[92mPass\033[0m")
        else:
            print(f"test {i}: \033[91mFail\033[0m")
    
       

if __name__ == "__main__":
    main()

