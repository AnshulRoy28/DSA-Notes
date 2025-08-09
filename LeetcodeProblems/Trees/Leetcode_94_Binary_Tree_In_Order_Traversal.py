def inorderTraversal(Self,root):
    if root==None:
        return []
    #As per the problem we each node has a left and right. 
    #In order traversal works as left->root->right simply recursively go through it 
    return inorderTraversal(root.left)+[root.val]+inorderTraversal(root.right)
    
'''
Java Implementation
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        // Add left subtree
        result.addAll(inorderTraversal(root.left));
        // Add root value
        result.add(root.val);
        // Add right subtree
        result.addAll(inorderTraversal(root.right));
        return result;
    }
}
'''
