def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        if root!=None:
            #Root left right traversal simple 
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        

'''
Java Implementation

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        /*
        Input:
            root (TreeNode): The root of the binary tree.

        Output:
            List<Integer>: List of node values in preorder traversal order.

        Purpose:
            Traverse the binary tree in preorder (root -> left -> right) 
            and collect the node values in a list recursively.
        */
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        // Visit root
        result.add(root.val);
        // Traverse left subtree
        result.addAll(preorderTraversal(root.left));
        // Traverse right subtree
        result.addAll(preorderTraversal(root.right));

        return result;
    }
}'''
