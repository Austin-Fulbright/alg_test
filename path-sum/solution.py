from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int)-> bool: 
        if not root:
            return False

        def dfs(node: TreeNode, currentSum: int) -> bool:
            result = currentSum - node.val
            if node.left or node.right:
                left = dfs(node.left, result) if node.left else: False
                right = dfs(node.right, result) if node.right else: False
                return left or right
            else:
                return result == 0
            
        return dfs(root, targetSum) 

