# main_2.py

import json
from solution_2 import compute_gains

def run_tests():
    with open('test_cases_2.json', 'r') as f:
        tests = json.load(f)

    for idx, case in enumerate(tests, 1):
        nums = case['input']['nums']
        k = case['input']['k']
        expected = case['expected']
        result = compute_gains(nums, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {idx}: nums={nums}, k={k}, expected={expected}, got={result} -> {status}")

if __name__ == "__main__":
    run_tests()
