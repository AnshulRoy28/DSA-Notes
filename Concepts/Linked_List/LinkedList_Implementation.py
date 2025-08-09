class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head=None

    def append(self, data):
        """
        Input:
            data: The value to append to the linked list.
        Output:
            None
        Purpose:
            Adds a new node with the given data at the end of the list.
        """
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def add_to_beginning(self, data):
        """
        Input:
            data: The value to add at the beginning of the linked list.
        Output:
            None
        Purpose:
            Inserts a new node with the given data at the start of the list.
        """
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def delete_with_value(self, data):
        """
        Input:
            data: The value of the node to delete.
        Output:
            None
        Purpose:
            Deletes the first node found with the specified data.
        """
        if not self.head:
            return

        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next

    def print_list(self):
        """
        Input:
            None
        Output:
            None
        Purpose:
            Prints all elements in the linked list in order.
        """
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

# Example usage
if __name__=="__main__":
    ll=LinkedList()
    ll.append(10)
    ll.append(20)
    ll.add_to_beginning(5)
    ll.print_list()         # Output: 5 -> 10 -> 20 -> None
    ll.delete_with_value(10)
    ll.print_list()         # Output: 5 -> 20 -> None
