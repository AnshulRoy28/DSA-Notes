#Import LinkedList class from LinkedList code its a dependency or use the following 
#class ListNode:
#    def __init__(self, val):
#        self.val = val
#        self.next = None

class QueueImpl:
    def __init__(self):
        self.front=None #Since wer using a linked list front is the head 
        self.rear=None  #Rear is the eld where we do the enque operations 

    def enqueue(self,val):
        new_node=ListNode(val) #Create new node
        if self.rear is None: #If the queue is empty
            self.front=self.rear=new_node #Front=rear as theirs only one element
            return
        self.rear.next=new_node #Else update rear pointer 
        self.rear=new_node

    def dequeue(self):
        if self.front is None: #If queue is empty 
            return -1
        data=self.front.val #Get the value of front
        self.front=self.front.next #Update the pointer for the front to be next element
        if self.front is None: #If the queue becomes empty
            self.rear=None #update rear
        return data

    def peek(self):
        if self.front is None:
            return -1
        return self.front.val #front is already the first value so no need to do anything

    def is_empty(self):
        return self.front is None #if front is None linkedlist is empty return true else False

    def display(self):
        curr=self.front
        print("Queue:",end=" ")
        while curr:
            print(curr.val,end=" ")
            curr=curr.next
        print()

#Driver Code 
queue = QueueImpl()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
print("Dequeued:", queue.dequeue())
queue.display()
print("Front element:", queue.peek())

"""
Java Implementation

import LinkedList.ListNode;
// Queue class using ListNode
public class QueueImpl {
    ListNode front, rear;
    public void enqueue(int val) {
        ListNode newNode = new ListNode(val);
        if (rear == null) {
            front = rear = newNode;
            return;
        }
        rear.next = newNode;
        rear = newNode;
    }
    public int dequeue() {
        if (front == null) {
            return -1;
        }
        int data = front.val;
        front = front.next;
        if (front == null) {
            rear = null;
        }
        return data;
    }
    public int peek() {
        if (front == null) {
            return -1;
        }
        return front.val;
    }
    public boolean isEmpty() {
        if (front == null) {
            return true;
        }
        return false;
    }
    public void display() {
        ListNode curr = front;
        System.out.print("Queue: ");
        while (curr != null) {
            System.out.print(curr.val + " ");
            curr = curr.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        QueueImpl queue = new QueueImpl();
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.enqueue(40);
        queue.display();
        System.out.println("Dequeued: " + queue.dequeue());
        queue.display();
        System.out.println("Front element: " + queue.peek());
    }
}
"""
