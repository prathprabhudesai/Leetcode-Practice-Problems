/*
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 Example 1:
 Input: root = [3,9,20,null,null,15,7]
 Output: 3

 Example 2:
 Input: root = [1,null,2]
 Output: 2

 Example 3:
 Input: root = []
 Output: 0

 Example 4:
 Input: root = [0]
 Output: 1

 Constraints:

 The number of nodes in the tree is in the range [0, 104].
 -100 <= Node.val <= 1000
*/

/**
 *  * Definition for a binary tree node.
 *   * struct TreeNode {
 * *     int val;
 *  *     struct TreeNode *left;
 *   *     struct TreeNode *right;
 *    * };
 *     */
int maxDepth(struct TreeNode* root)
{
    if (root == NULL)
    {
        return 0;
    }
    int left_depth = maxDepth(root->left);
    int right_depth = maxDepth(root->right);
    if (left_depth > right_depth)
    {
        return (left_depth + 1);
    }
    return (right_depth + 1);
}
