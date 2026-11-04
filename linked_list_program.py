"""
ASSESSMENT 3.2 - LINKED LIST
Based on Assessment 3.1 (Last Name: PARAN)

Algorithm (from 3.1):
1. Start.
2. Create an empty linked list.
3. Insert P, A, R, A, N at the end of the list.
4. Display the list: P -> A -> R -> A -> N.
5. Remove the first node repeatedly until the list is empty.
6. Display the list after each removal.
7. Stop.
List states: P -> A -> R -> A -> N; A -> R -> A -> N; R -> A -> N; A -> N; N; Empty.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):                 # Step 2: empty linked list
        self.head = None

    def insert_at_end(self, data):      # Step 3: insert at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_first(self):             # Step 5: remove the first node
        removed = self.head.data
        self.head = self.head.next
        return removed

    def is_empty(self):
        return self.head is None

    def display(self):                  # Steps 4 and 6: display the list
        if self.head is None:
            return "Empty"
        parts = []
        current = self.head
        while current:
            parts.append(current.data)
            current = current.next
        return " -> ".join(parts)


# Step 1: Start
print("=== LINKED LIST ===")

# Dynamic part: the user types the last name (Enter = PARAN)
name = input("Enter your last name (press Enter for PARAN): ").strip().upper() or "PARAN"

# Step 2: Create an empty linked list
linked_list = LinkedList()

# Step 3: Insert each letter at the end of the list
for ch in name:
    linked_list.insert_at_end(ch)

# Step 4: Display the list
print("\nList:", linked_list.display())

# Step 5 and 6: Remove the first node repeatedly, display after each removal
print("\nRemoving the first node:")
while not linked_list.is_empty():
    removed = linked_list.remove_first()
    print(f"Removed {removed} -> {linked_list.display()}")

# Step 7: Stop
print("\nThe list is empty. Stop.")
