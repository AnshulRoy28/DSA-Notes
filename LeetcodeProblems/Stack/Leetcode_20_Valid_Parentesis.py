def valid_Parenthesis(s):
    """
    Input:
        s (str): String with '()', '{}', '[]' characters.

    Output:
        bool: True if brackets are valid, False otherwise.

    Purpose:
        Validates that brackets are correctly matched and nested using a stack.
    """

    map = {"(": ")", "{": "}", "[": "]"}
    stack=[]
    for i in s:
        if i in map.keys(): #If i is opening bracket store it
            stack.append(i)
        else:
            if len(stack)==0: #If we encounter a closing bracket but stack is empty i.e s=")" the string is invalid 
                return False
            elif i==map[stack[-1]]: #If the i'th element matches the corresponding value of the last element in stack then all is well
                stack.pop() #Pop element from stack
            else:
                return False 
    if len(stack)==0: #At the end if stack is empty i.e all brackets matched i.e all parenthesis are valid
        return True
    else:
        return False

"""
Java Implementation 
class Solution {
    public static boolean isValid(String s) {

        Stack < Character > stack = new Stack < > ();

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i); // Access each character in the String

            // Push into the stack on opening brackets
            if ((currentChar == '(' || currentChar == '[' || currentChar == '{')) {
                stack.push(currentChar);
            } else if (stack.isEmpty()) {
                return false; // If stack is empty on closing bracket
            } else {
                Character top = stack.peek();
                // Checking for valid pairs of brackets
                if ((top == '[' && currentChar == ']') || (top == '{' && currentChar == '}') ||
                    (top == '(' && currentChar == ')')) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
"""

