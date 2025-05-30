import sys
import json

from pathlib import Path
from solution_1 import Solution

def load_test_cases(filename):

    current_dir = Path(__file__).parent
    test_cases_path = current_dir / "test_cases_1.json"

    try:
        with open (test_cases_path, 'r') as f:
            data = json.load(f)
        return data.get("test_case", [])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        sys.exit(1)

def main():
    sol = Solution()

    test_cases = load_test_cases("test_cases_1.json")
    for i, test in enumerate(test_cases):
        edges1 = test.get("edges1")
        edges2 = test.get("edges2")
        expected = test.get("expected")
        result = sol.maxTargetNodes(edges1, edges2)
        print(f"edges1 = {edges1} edges2 = {edges2}")
        print(f"[largest path value: result = {result} and expected = {expected}]")
        isEqual = True
        if len(result) != len(expected):
            isEqual = False
        else:
            for i in range(len(result)):
                if result[i] != expected[i]:
                    isEqual = False
                    break
        if isEqual: 
            print(f"test {i}: \033[92mPass\033[0m")
        else:
            print(f"test {i}: \033[91mFail\033[0m")

if __name__ == "__main__":
    main()

