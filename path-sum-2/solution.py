from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]: 
        result = []

        if not root:
            return result

        def dfs(node: TreeNode, currentSum: int, currentPath: List[int]):
            print(currentPath)
            currentPath.append(node.val)
            csum = currentSum - node.val
            if node.left or node.right:
                if node.left:
                    dfs(node.left, csum, currentPath)
                if node.right:
                    dfs(node.right, csum, currentPath)
            else:
                if csum == 0:
                    result.append(currentPath[:])
            currentPath.pop()

        dfs(root, targetSum, []) 
        return result 

