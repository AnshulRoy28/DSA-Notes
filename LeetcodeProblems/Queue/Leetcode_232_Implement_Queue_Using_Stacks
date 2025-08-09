class Myqueue:
    def __init__(self):
        #Goal is to implement a queue using 2 stacks
        self.s1=[]
        self.s2=[]

    def push(self,x):
        #step1
        while self.s1:
            self.s2.append(self.s1.pop()) #Move all elements of s1 to s2

        #step2
        self.s1.append(x) #Add i to the empty s1

        #step3
        while self.s2:
            self.s1.append(self.s2.pop()) #Move all elements back to s1

        """Basically what we are doing here is 
        step 0
        i=4, s1=[3,2,1] , s2=[]
        step 1
        s1=[], s2=[1,2,3]
        step 2
        s1=[4] s2=[1,2,3]
        step 3
        s1=[4,3,2,1] s2=[]
        """

    def pop(self):
        if not self.s1:
            raise IndexError("No elements in Queue cannot pop")
        return self.s1.pop() # pops the last element of s1 '1' in the above example 
    
    def peek(self):
        return self.s1[-1] #Shows us the last element in stack s1 i.e '1' in our example
    
    def empty(self):
        return len(self.s1)==0 #If s1 is empty then our que is empty 
    

"""Java Implementation
class Solution {
    Stack < Integer > s1;
    Stack < Integer > s2;
    public MyQueue() {
        s1 = new Stack < > ();
        s2 = new Stack < > ();
    }

    public void push(int x) {
        while (!s1.isEmpty()) {
            s2.push(s1.pop());
        }
        s1.push(x);
        while (!s2.isEmpty()) {
            s1.push(s2.pop());
        }

    }

    public int pop() {
        return s1.pop();
    }

    public int peek() {
        return s1.peek();
    }

    public boolean empty() {
        return s1.isEmpty();
    }
}
"""
