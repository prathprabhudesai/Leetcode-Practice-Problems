'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if (root is None):
            return None
        level_order_traversal = []
        curr_level = [root]
        while(1):
            next_level = []
            level_order_traversal.insert(0,[])
            while len(curr_level) != 0:
                node = curr_level.pop(0)
                level_order_traversal[0].append(node.val)
                if (node.left):
                    next_level.append(node.left)
                if (node.right):
                    next_level.append(node.right)
            if len(next_level):
                curr_level = next_level
            else:
                break
        return level_order_traversal