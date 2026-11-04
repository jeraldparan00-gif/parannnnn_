"""
ASSESSMENT 3.2 - STACK (LIFO: Last In, First Out)
Based on Assessment 3.1 (Last Name: PARAN)

Algorithm (from 3.1):
1. Start.
2. Create an empty stack.
3. Push P, A, R, A, N onto the stack.
4. Display the stack from bottom to top: P, A, R, A, N.
5. Pop one letter at a time. The removal order is N, A, R, A, P.
6. Continue until the stack is empty.
7. Stop.
"""


class Stack:
    def __init__(self):                 # Step 2: empty stack
        self.items = []

    def push(self, item):               # Step 3: push
        self.items.append(item)

    def pop(self):                      # Step 5: pop
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# Step 1: Start
print("=== STACK ===")

# Dynamic part: the user types the last name (Enter = PARAN)
name = input("Enter your last name (press Enter for PARAN): ").strip().upper() or "PARAN"

# Step 2: Create an empty stack
stack = Stack()

# Step 3: Push each letter onto the stack
for ch in name:
    stack.push(ch)

# Step 4: Display the stack from bottom to top
print("\nStack (bottom to top):", stack.items)

# Step 5 and 6: Pop one letter at a time until the stack is empty
print("\nPopping letters:")
while not stack.is_empty():
    removed = stack.pop()
    print(f"Popped {removed} -> {stack.items}")

# Step 7: Stop
print("\nThe stack is empty. Stop.")
