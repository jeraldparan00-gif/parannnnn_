"""
ASSESSMENT 3.2 - ARRAY
Based on Assessment 3.1 (Last Name: PARAN)

Algorithm (from 3.1):
1. Start.
2. Create an empty array named letters.
3. Add the letters P, A, R, A, N to the array.
4. Display the array: [P, A, R, A, N].
5. Remove each letter from the end of the array one at a time: N, A, R, A, P.
6. Display the array after each removal until it is empty:
   [P, A, R, A] -> [P, A, R] -> [P, A] -> [P] -> [].
7. Stop.
"""

# Step 1: Start
print("=== ARRAY ===")

# Dynamic part: the user types the last name (Enter = PARAN)
name = input("Enter your last name (press Enter for PARAN): ").strip().upper() or "PARAN"

# Step 2: Create an empty array named letters
letters = []

# Step 3: Add the letters to the array
for ch in name:
    letters.append(ch)

# Step 4: Display the array
print("\nArray:", letters)

# Step 5 and 6: Remove from the end one at a time, display after each removal
print("\nRemoving from the end:")
while len(letters) > 0:
    removed = letters.pop()
    print(f"Removed {removed} -> {letters}")

# Step 7: Stop
print("\nThe array is empty. Stop.")
