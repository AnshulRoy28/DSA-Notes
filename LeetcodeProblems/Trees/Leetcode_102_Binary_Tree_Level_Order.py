from collections import deque
def levelOrder(self, root):
        if not root:
            return []
    
        result=[]
        queue=deque([root])

        while queue:
            level_size=len(queue)
            current_level=[]

            for i in range(level_size):
                node=queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result    

"""Java Implementation 
class Solution {
    public List < List < Integer >> levelOrder(TreeNode root) {
        Queue < TreeNode > queue = new LinkedList < TreeNode > ();
        List < List < Integer >> finalResult = new LinkedList < List < Integer >> ();

        if (root == null) {
            return finalResult;
        }

        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List < Integer > tempResult = new LinkedList < Integer > ();

            for (int i = 0; i < size; i++) {
                if (queue.peek().left != null) queue.add(queue.peek().left);
                if (queue.peek().right != null) queue.add(queue.peek().right);
                tempResult.add(queue.remove().val);
            }

            finalResult.add(tempResult);
        }
        return finalResult;
    }
}
"""
