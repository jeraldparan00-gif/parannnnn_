"""
ASSESSMENT 3.2 - DEQUE (Double-Ended Queue)
Based on Assessment 3.1 (Last Name: PARAN)

Algorithm (from 3.1):
1. Start.
2. Create an empty deque.
3. Insert P, A, R, A, N at the rear.
4. Display the deque: P, A, R, A, N.
5. Remove letters from the front one at a time: P, A, R, A, N.
6. Continue until the deque is empty.
7. Stop.
"""

from collections import deque

# Step 1: Start
print("=== DEQUE ===")

# Dynamic part: the user types the last name (Enter = PARAN)
name = input("Enter your last name (press Enter for PARAN): ").strip().upper() or "PARAN"

# Step 2: Create an empty deque
letters = deque()

# Step 3: Insert each letter at the rear
for ch in name:
    letters.append(ch)

# Step 4: Display the deque (front to rear)
print("\nDeque (front to rear):", list(letters))

# Step 5 and 6: Remove from the front one at a time until the deque is empty
print("\nRemoving from the front:")
while len(letters) > 0:
    removed = letters.popleft()
    print(f"Removed {removed} -> {list(letters)}")

# Step 7: Stop
print("\nThe deque is empty. Stop.")
