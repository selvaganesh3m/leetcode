class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_at_head(self, value):
        node = Node(value=value)
        # if linked list has only head
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node

        # if linked list is empty
        if self.head is None:
            self.head = node
            self.tail = node

    def insert_at_tail(self, value):
        node = Node(value=value)

        # if linked list has only tail
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        # if linked list is empty
        if self.head is None:
            self.head = node
            self.tail = node


    def delete_at_head(self):
        if self.head:
            # if only one element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            
            # if more than one element in list
            else:
                self.head = self.head.next
                self.head.prev = None
        else:
            print("Nothing to delete, linked list is already empty")

    def delete_at_tail(self):
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            print("Nothing to delete, linked list is already empty")


    def display(self, reverse=False):
        if not reverse:
            temp = self.head
            while temp:
                print(temp.value, end=" <=> ")
                temp = temp.next
        else:
            temp = self.tail
            while temp:
                print(temp.value, end=" <=> ")
                temp = temp.prev
        self.current_data()

    def current_data(self):
        print("\n")
        if not self.head:
            print("List is empty")
        else:
            print(f"Head :{self.head.value}")
            print(f"Tail :{self.tail.value}")





    

doubly = DoublyLinkedList()
# doubly.insert_at_tail(13)
# doubly.insert_at_head(1)
# doubly.insert_at_head(2)
# doubly.insert_at_head(3)
# doubly.insert_at_head(4)
# doubly.insert_at_head(5)
# doubly.insert_at_head(6)
# doubly.insert_at_head(7)
# doubly.insert_at_head(8)
# doubly.insert_at_head(9)
# doubly.insert_at_tail(10)
# doubly.insert_at_tail(11)
# doubly.insert_at_tail(12)
# doubly.insert_at_head(14)
# # doubly.delete_at_head()
# doubly.delete_at_tail()

doubly.display()
print("\n")