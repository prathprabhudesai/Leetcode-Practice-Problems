/*
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

1
/ \
2   2
/ \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

1
/ \
2   2
\   \
3    3

Follow up: Solve it both recursively and iteratively.
*/
/**
 *  * Definition for a binary tree node.
 *   * struct TreeNode {
 * *     int val;
 *  *     struct TreeNode *left;
 *   *     struct TreeNode *right;
 *    * };
 *     */

bool isMirror(struct TreeNode * root1, struct TreeNode * root2)
{
    if ((root1 == NULL) && (root2 == NULL))
    {
        return true;
    }
    if (root1 && root2 && (root1->val == root2->val))
    {
        return (isMirror(root1->left, root2->right) &&
                isMirror(root1->right, root2->left));
    }
    return false;
}


bool isSymmetric(struct TreeNode* root)
{
    return isMirror(root, root);

}
