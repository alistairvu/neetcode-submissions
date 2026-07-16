# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        memo = {}

        def size(node: Optional[TreeNode]):
            if node == None:
                return 0
            
            if node in memo:
                return memo[node]
            
            left, right = size(node.left), size(node.right)
            memo[node] = left + right + 1
            return memo[node]
        
        def dfs(node: Optional[TreeNode], rem: int):
            if node == None:
                return -1
            
            left_size = size(node.left)

            if left_size + 1 == rem:
                return node.val
            elif left_size + 1 > rem:
                return dfs(node.left, rem)
            else:
                return dfs(node.right, rem - left_size - 1)
        
        size(root)
        return dfs(root, k)