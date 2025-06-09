# main.py
import sys
import json
from pathlib import Path
from solution import Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(arr):
    """Convert list representation to TreeNode objects"""
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

def load_test_cases(filename):
    current_dir = Path(__file__).parent
    test_cases_path = current_dir / "test_cases.json"
    try:
        with open(test_cases_path, 'r') as f:
            data = json.load(f)
        return data.get("test_case", [])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        sys.exit(1)

def main():
    sol = Solution()
    test_cases = load_test_cases("test_cases.json")
    
    for i, test in enumerate(test_cases):
        tree_list = test.get("tree")
        target_sum = test.get("targetSum")
        expected = test.get("expected")
        
        # Build tree from list representation
        root = build_tree_from_list(tree_list)
        
        # Call the hasPathSum method
        result = sol.hasPathSum(root, target_sum)
        
        print(f"tree = {tree_list}")
        print(f"targetSum = {target_sum}")
        print(f"[path sum: result = {result} and expected = {expected}]")
        
        if expected == result:
            print(f"test {i}: \033[92mPass\033[0m")
        else:
            print(f"test {i}: \033[91mFail\033[0m")
        print()

if __name__ == "__main__":
    main()
