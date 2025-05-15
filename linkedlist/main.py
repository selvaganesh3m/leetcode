from singly import singly
from doubly import doubly
from circular import circular

def choose_linked_list():
    print("""
Choose the type of Linked List:
    1. Singly Linked List
    2. Doubly Linked List
    3. Circular Linked List
    4. Exit
""")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            return singly, "Singly"
        elif choice == 2:
            return doubly, "Doubly"
        elif choice == 3:
            return circular, "Circular"
        elif choice == 4:
            return None, "Exit"
        else:
            print("Invalid choice.")
            return None, None
    except ValueError:
        print("Please enter a valid number.")
        return None, None

def choose_operation():
    print("""
Choose an operation:
    1. Insert
    2. Delete
    3. Display
    4. Back to Main Menu
""")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Try again.")
        return None

def choose_position(action):
    print(f"""
Where do you want to {action}?
    1. At the Head
    2. At the Tail
""")
    try:
        pos = int(input("Enter your choice: "))
        if pos in [1, 2]:
            return pos
        else:
            print("Invalid position.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

def handle_insert(ll):
    pos = choose_position("insert")
    if pos:
        value = input("Enter the value to insert: ")
        if pos == 1:
            ll.insert_at_head(value)
        else:
            ll.insert_at_tail(value)
        ll.display()

def handle_delete(ll):
    pos = choose_position("delete")
    if pos:
        if pos == 1:
            ll.delete_at_head()
        else:
            ll.delete_at_tail()
        ll.display()

def main():
    while True:
        ll, ll_name = choose_linked_list()
        if ll_name == "Exit":
            print("Goodbye!")
            break
        elif ll is None:
            continue
        
        print(f"\n--- {ll_name} Linked List ---")
        while True:
            op = choose_operation()
            if op == 1:
                handle_insert(ll)
            elif op == 2:
                handle_delete(ll)
            elif op == 3:
                ll.display()
            elif op == 4:
                print("Returning to Main Menu...\n")
                break
            else:
                print("Invalid operation.")
    

if __name__ == "__main__":
    main()
