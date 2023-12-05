
"""
    好像是遍历顺序的问题?
    按照 dfs(root.right), root.val, dfs(root.left) 的顺序遍历即可获得 最大->最小
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def bstToGst(self, _root: TreeNode) -> TreeNode:
        prefix_sum = []
        def dfs(root: TreeNode):
            if root.right:
                dfs(root.right)
            prefix_sum.append((prefix_sum[-1] if len(prefix_sum) else 0) + root.val)
            root.val = prefix_sum[-1]
            if root.left:
                dfs(root.left)
        dfs(_root)

        return _root