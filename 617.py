from typing import Optional

from helpers.binary_tree import BinaryTree, TreeNode


# Title: 617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge_r(node1: TreeNode, node2: TreeNode) -> TreeNode:
            # this pattern is like inserting a node to a binary search tree recursively
            if node1 and node2:
                newNode = TreeNode(node1.val + node2.val)
                newNode.left = merge_r(node1.left, node2.left)
                newNode.right = merge_r(node1.right, node2.right)
                return newNode
            else:
                return node1 or node2

        return merge_r(root1, root2)


#### test

#### case 1
t1node1 = TreeNode(1, right=TreeNode(2))
t1node1.left = TreeNode(3, left=TreeNode(5))

t2node2 = TreeNode(2)
t2node2.left = TreeNode(1, right=TreeNode(4))
t2node2.right = TreeNode(3, left=TreeNode(7))

s = Solution()
result = s.mergeTrees(t1node1, t2node2)
assert BinaryTree().transverse_bfs(result) == [3, 4, 5, 5, 4, 7]

#### case 2
t3node1 = TreeNode(1)
t4node1 = TreeNode(1, left=TreeNode(2))
s = Solution()
result = s.mergeTrees(t3node1, t4node1)
assert BinaryTree().transverse_bfs(result) == [2, 2]
