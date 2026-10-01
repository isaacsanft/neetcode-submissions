# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(root1, root2):
            if root1 is None and root2 is None:
                return True
            if (root1 is None) ^ (root2 is None):
                return False
            if root1.val != root2.val:
                return False
            return compare(root1.left, root2.left) and compare(root1.right, root2.right)

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if compare(node, subRoot):
                    return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return False