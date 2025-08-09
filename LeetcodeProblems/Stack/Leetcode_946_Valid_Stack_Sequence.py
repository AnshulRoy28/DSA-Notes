def validateStackSequence(pushed,popped):
    """
    Input:
        pushed (list[int]): Push order of integers onto the stack.
        popped (list[int]): Desired pop order.

    Output:
        bool: True if 'popped' can be obtained from 'pushed' via valid stack operations, else False.

    Purpose:
        Check if the given pop sequence is possible by simulating stack pushes and pops.
    """

    stack=[]
    pop_index=0
    for i in pushed:
        stack.append(i) #Push element to the stack

        while stack and stack[-1]==popped[pop_index]: 
            stack.pop()         #Pop if top element matches the desired pop
            pop_index+=1        #increment pop index 

    return not stack #If stack empty return True else False


"""
Java Implementation
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        if (pushed.length == 1) {
            return pushed[0] == popped[0];
        }
        int popIndex = 0;
        Stack < Integer > st = new Stack < > ();
        for (int ele: pushed) {
            st.push(ele);
            while (!st.isEmpty() && st.peek() == popped[popIndex]) {
                st.pop();
                popIndex++;
            }
        }
        return st.isEmpty();
    }
}

"""