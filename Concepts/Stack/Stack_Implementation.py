class StackNode:
    def __init__(self,value=None,next_node=None):
        """
            Input:
                value (int | None): The value to store in the node.
                next_node (StackNode | None): The next node in the stack.

            Output:
                None

            Purpose:
                Represents a single node in a stack, storing a value and 
                a reference to the next node in the stack kinna like a linked list.
        """
        self.val=value
        self.next=next_node
    
class Stack:
    def __init__(self):
        """
        Input:
            None

        Output:
            None
        Purpose:
            Implements a stack data structure using linked nodes.
        """
        self.head = None
    
    def push(self,x):
        """
        Input:
            x (int): The value to be pushed onto the stack.

        Output:
            None

        Purpose:
            Push a new value onto the top of the stack.
        """
        self.head=StackNode(x,self.head) #Create a new node and have it point to the previous head

    def pop(self):
        """
        Input:
            None

        Output:
            int: The value from the top of the stack.

        Purpose:
            Remove and return the value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """

        if self.head is None: #If stack is empty you cannot pop from it cuz obv
            raise IndexError("The stack is empty you cannot pop")
        
        result=self.head.val #Store value of the topmost i.e head element
        self.head=self.head.next #Update the head pointer so it ignores the first element 
        return result
    
    def delete(self,value):
        """
        Input:
            value (int): The value to delete from the stack.

        Output:
            bool: True if the value was found and deleted, False otherwise.

        Purpose:
            Deletes the first occurrence of a given value from the stack.
        """
        current=self.head
        prev=None #We need to track the previous element to update pointer after deleting

        while current:
            #If element is found
            if current.val==value:
                if prev is None: #This only happens if the node to delete is the head of stack
                    self.head=current.next #Update head 
                else:
                    prev.next=current.next #Update prev 
                return True
            
            #If we did not find out element
            prev=current #update prev to be current 
            current=current.next #update current to the next element
            return False
    
    def print_stack(self):
        """
        Input:
            None

        Output:
            None

        Purpose:
            Prints all elements in the stack from top to bottom.
        """

        current=self.head
        if not current:
            print("Stack is empty")
            return 
        
        while current:
            print(current.val,end=" ")
            current=current.next
        print()
    
#Sample usage

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
w=s.pop()
s.print_stack()

'''
Java Version
public class StackNode {
    public int val;
    public StackNode next;
    private StackNode head = null;

    public StackNode() {
    }

    public StackNode(int value, StackNode next) {
        this.val = value;
        this.next = next;
    }

    public void push(int x) {
        head = new StackNode(x, head);
    }

    public int pop() {
        int result = head.val;
        head = head.next;
        return result;
    }

    public static void main(String[] args) {
        StackNode s = new StackNode();
        s.push(1);
        s.push(3);
        s.push(2);

        int w = s.pop();
        System.out.println(w);
    }
}

'''
