from collections import deque
def levelOrder(self, root):
        if not root:
            return [] #Tree empty return 
    
        result=[]
        queue=deque([root]) #Use Queue for BFS traversal 

        while queue:
            level_size=len(queue) #Number of nodes at current lvl 
            current_level=[] #List to hold values of current lvl 

            #Process nodes at current lvl 
            for i in range(level_size):
                node=queue.popleft() #Remove node from que
                current_level.append(node.val) #Add node's value to current_lvl

                #If left child exists add to queue
                if node.left:
                    queue.append(node.left)
                
                #If right child exists add to queue
                if node.right:
                    queue.append(node.right)
            #After processing add current lvl val to result
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
