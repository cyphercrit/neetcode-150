from typing import Optional
from tree_node import TreeNode

'''
You are given the root of a binary tree root. Invert the binary tree and return its root.
'''

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)