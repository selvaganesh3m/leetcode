class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_head(self, value):
        node = Node(value=value)
        # if the list is empty
        if self.head is None:
            self.head = node
            self.tail = self.head
           
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head

        # if one or more node   
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = self.tail
            self.tail.next = self.head

    def insert_at_tail(self, value):
        node = Node(value=value)

        # if the list is empty
        if self.tail is None:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
        
        # if one or more node   
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail

    def delete_at_head(self):
        # if there is one element
        if self.head and (self.head is self.tail):
            self.head.next = None
            self.head.prev = None
            self.tail.next = None
            self.tail.prev = None
            self.head = None
            self.tail = None

        # if there is more than one element in linked list
        if self.head is not None:
            old_head = self.head
            self.head = old_head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            old_head.next = None
            old_head.prev = None
        else:
            print("Nothing to delete, list is already empty.")


    def delete_at_tail(self):
        if self.tail is None:
            print("Nothing to delete, list is already empty.")
        else:
            # if there is one element
            if self.tail and (self.tail == self.head):
                self.head.next = None
                self.head.prev = None
                self.tail.next = None
                self.tail.prev = None
                self.head = None
                self.tail = None
            else:
                # if there is more than one element
                old_tail = self.tail
                self.tail = old_tail.prev
                old_tail.next = None
                old_tail.prev = None
                self.tail.next = self.head
                self.head.prev = self.tail
                
        

    def display(self, reverse=False):
        if not reverse:
            temp = self.head
            while temp:
                print(temp.value, end=" <=> ")
                if temp == self.tail:
                    break
                temp = temp.next
        else:
            temp = self.tail
            while temp:
                print(temp.value, end=" <=> ")
                if temp == self.tail:
                    break
                temp = temp.prev
        print("\n")
        self.current_data()

    def current_data(self):
        if self.head is not None:
            print(f"Head={self.head.value}")
            print(f"Tail={self.tail.value}")
            print("------------------------")
            print(f"Head Next Value :{self.head.next.value}")
            print(f"Head Prev Value :{self.head.prev.value}")
            print(f"Tail Next Value :{self.tail.next.value}")
            print(f"Tail Prev Value :{self.tail.prev.value}")
        else:
            print("Linked list is empty")



circular = CircularLinkedList()

# circular.insert_at_head(10)
# circular.insert_at_head(11)
# circular.insert_at_head(12)
# circular.insert_at_head(13)
# circular.insert_at_head(14)
# circular.insert_at_tail(15)
# circular.insert_at_tail(16)
# circular.insert_at_tail(17)
# circular.insert_at_tail(18)
# circular.insert_at_tail(19)
# circular.delete_at_head()
# circular.delete_at_tail()


circular.display()





