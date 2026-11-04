"""
ASSESSMENT 3.2 - QUEUE (FIFO: First In, First Out)
Based on Assessment 3.1 (Last Name: PARAN)

Algorithm (from 3.1):
1. Start.
2. Create an empty queue.
3. Enqueue P, A, R, A, N into the queue.
4. Display the queue: P, A, R, A, N.
5. Dequeue one letter at a time. The removal order is P, A, R, A, N.
6. Continue until the queue is empty.
7. Stop.
"""


class Queue:
    def __init__(self):                 # Step 2: empty queue
        self.items = []

    def enqueue(self, item):            # Step 3: enqueue (add at rear)
        self.items.append(item)

    def dequeue(self):                  # Step 5: dequeue (remove from front)
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# Step 1: Start
print("=== QUEUE ===")

# Dynamic part: the user types the last name (Enter = PARAN)
name = input("Enter your last name (press Enter for PARAN): ").strip().upper() or "PARAN"

# Step 2: Create an empty queue
queue = Queue()

# Step 3: Enqueue each letter
for ch in name:
    queue.enqueue(ch)

# Step 4: Display the queue (front to rear)
print("\nQueue (front to rear):", queue.items)

# Step 5 and 6: Dequeue one letter at a time until the queue is empty
print("\nDequeuing letters:")
while not queue.is_empty():
    removed = queue.dequeue()
    print(f"Dequeued {removed} -> {queue.items}")

# Step 7: Stop
print("\nThe queue is empty. Stop.")
