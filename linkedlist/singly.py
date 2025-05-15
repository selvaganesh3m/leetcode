class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # Insert Operations
    def insert_at_head(self, value):
        node = Node(value=value)

        # if head is already exist
        if self.head:
            node.next = self.head
            self.head = node

        # if there is only one head
        if self.head == self.tail:
            node.next = self.head
            self.head = node
            self.tail = node.next
        
        # if there is no head (which is empty linked list)
        if not self.head.next:
            self.head = node
            self.tail = node

    def insert_at_tail(self, value):
        node = Node(value=value)

        # if there is no tail (which is empty linked list)
        if self.head is None:
            self.head = node
            self.tail = node
        
        # if tail already exists
        else:
            self.tail.next = node
            self.tail = node

    def delete_at_head(self):
        # if there is head
        if self.head:
            # if there is more than one node in linked list
            if new_head := self.head.next:
                self.head = new_head
            # if there is only one node in linked list
            else:
                self.head = None
                self.tail = None
        # if there is no node in linked list (empty linked list)
        else:
            print("Nothing to delete, linked list is empty")

    
    def delete_at_tail(self):
        # if there is only one element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        if self.tail:
            # if there is more than one element in linked list
            temp = self.head
            while temp:
                if temp.next == self.tail:
                    self.tail = temp
                    self.tail.next = None
                else:
                    temp = temp.next
        # if there is no node in linked list(empty linked list)
        else:
            print("Nothing to delete, linked list is empty")

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <- ")
            temp = temp.next

    def current_data(self):
        print("\n")
        if not self.head:
            print("List is empty")
        else:
            print(f"Head :{self.head.value}")
            print(f"Tail :{self.tail.value}")

    

singly = SinglyLinkedList()

# Insterting
# singly.insert_at_head(1)
# singly.insert_at_head(2)
# singly.insert_at_head(3)
# singly.insert_at_head(4)
# singly.insert_at_head(5)
# singly.insert_at_head(6)
# singly.insert_at_head(7)
# singly.insert_at_tail(8)

print("\n")


# Display
singly.display()


print("\n")