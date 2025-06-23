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

def check_arrays_eq(result, expected):
    if len(result) != len(expected):
        return False
    for i in range(len(result)):
        if result[i] != expected[i]:
            return False
    return True

def main():
    sol = Solution()

    test_cases = load_test_cases("test_cases.json")
    for i, test in enumerate(test_cases):
        numbers = test.get("nums")
        expected = test.get("expected")
        result = sol.threeSum(numbers)
        print(f"numbers = {numbers}") 
        print(f"[two sum with sorted array: result = {result} and expected = {expected}]")
        eq = check_arrays_eq(result, expected)
        if eq: 
            print(f"test {i}: \033[92mPass\033[0m")
        else:
            print(f"test {i}: \033[91mFail\033[0m")
    
       

if __name__ == "__main__":
    main()

