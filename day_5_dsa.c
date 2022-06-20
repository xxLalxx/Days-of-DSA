/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* searchBST(struct TreeNode* root, int val){

    if(root == NULL)
        return NULL;
    else if(root->val > val)
        return searchBST(root->left, val);
    else if(root->val < val)
        return searchBST(root->right, val);
    else
        return root;
}