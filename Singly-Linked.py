#Task 1

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


#Task 2 


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Delete 
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None:
            print("Node not found.")
            return
        current.next = current.next.next

    # Traverse 
    def traverse(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


#Task 3 
        
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insert at beginning
    print("Insert at beginning:")
    linked_list.insert_beginning(3)
    linked_list.insert_beginning(2)
    linked_list.insert_beginning(1)
    linked_list.traverse()  

    # Insert at end
    print("Insert at end:")
    linked_list.insert_end(4)
    linked_list.insert_end(5)
    linked_list.traverse()  

    # Delete head 
    print("Delete head:")
    linked_list.delete(1)
    linked_list.traverse() 

    # Delete end
    print("Delete middle:")
    linked_list.delete(3)
    linked_list.traverse()  
  