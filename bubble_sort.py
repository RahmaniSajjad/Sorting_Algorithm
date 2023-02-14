# The code implements the bubble sort algorithm to sort a list of numbers.
# The inner loop compares adjacent elements and swaps them if they are in the wrong order.
# The outer loop repeats this process until no more swaps are made, which means that the list is sorted.
# The number of swaps made is counted and printed at the end.

# Create a list of numbers to sort
A = [8, 22, 7, 9, 31, 5, 13]

# Get the length of the list
n = len(A)

# Initialize a variable to count the number of swaps made
count = 0

# Print the original list
print("list =", A)

# Loop through the list, comparing adjacent elements and swapping them if they are in the wrong order
for i in range(n - 1):
    bubble_found = False
    for j in range(n - 1, i, -1):
        if A[j] < A[j - 1]:
            # Swap the elements
            count += 1
            A[j], A[j - 1] = A[j - 1], A[j]
            bubble_found = True
    # If no swaps were made in the inner loop, the list is already sorted
    if not bubble_found:
        break
    # Print the list after each iteration (optional)
    print(A)

# Print the sorted list and the number of swaps made
print("sorted list =", A)
print(count)
