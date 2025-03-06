class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("Node with value {key} not found.")
            return
        prev.next = temp.next
        temp = None
    def display(self):
        temp = self.head
        if not temp:
            print("Linked list is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")
llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_beginning(5)
llist.insert_at_end(30)
print("Linked list after insertions:")
llist.display()
llist.delete_node(20)
print("Linked list after deletion:")
llist.display()


