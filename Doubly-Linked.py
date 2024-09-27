# Task 1: Implement Node class
class Node:
    def __init__(self, data):
        self.data = data  # Data of the node
        self.prev = None  # Previous node
        self.next = None  # Next node

# Task 2: Implement DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list

    # Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:  
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    # Delete node 
    def delete(self, data):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head

        # If the node to delete is the head node
        if current.data == data:
            if current.next:
                current.next.prev = None
            self.head = current.next
            return

        # Traverse the list to find the node
        while current and current.data != data:
            current = current.next

        if current is None:
            print("Node not found.")
            return

        # If node found, adjust the pointers
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    # Traverse the list forwards
    def traverse_forward(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Traverse the list backwards
    def traverse_backward(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head

        # Move to the last node
        while current.next:
            current = current.next

        # Now traverse backwards
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Task 3: Test the implemented functionality
if __name__ == "__main__":
    dbl = DoublyLinkedList()

    # Insert at the beginning
    print("Insert at Beginning:")
    dbl.insert_beginning(3)
    dbl.insert_beginning(2)
    dbl.insert_beginning(1)

    # Insert at the end
    print("Insert at End:")
    dbl.insert_end(4)
    dbl.insert_end(5)

    # Traverse forward
    print("Traverse forward:")
    dbl.traverse_forward()  
    # Traversing backward
    print("Traverse backward:")
    dbl.traverse_backward() 

    # Delete head node
    print("Delete head node:")
    dbl.delete(1)
    dbl.traverse_forward()  

    # Delete middle node
    print("Delete middle node:")
    dbl.delete(3)
    dbl.traverse_forward()  

  
 

