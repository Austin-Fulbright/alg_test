import json
from solution_1 import evenSubsetMax

def run_tests():
    with open('test_cases_1.json', 'r') as f:
        test_cases = json.load(f)

    for idx, case in enumerate(test_cases, 1):
        nums = case['input']
        expected = case['expected']
        result = evenSubsetMax(nums)
        status = "PASS" if result == expected else "FAIL"
        # Option #1: convert to string and pad
        print(f"Test {idx:>2}: input={str(nums):<15} expected={expected:<3} got={result:<3} → {status}")

        # — OR —
        # Option #2: use repr without padding
        # print(f"Test {idx:>2}: input={nums!r} expected={expected:<3} got={result:<3} → {status}")

if __name__ == "__main__":
    run_tests()
