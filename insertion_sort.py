# The code implements the insertion sort algorithm to sort a list of integers.
# The algorithm maintains a sorted sub-list of the input list, starting with the first element.
# For each subsequent element in the input list, the algorithm finds its correct position in the sorted sub-list and inserts it.
# The for loop iterates over each index k in the input list, starting from the second element.
# The variable item stores the value at index k.
# The while loop shifts larger values in the sorted sub-list to the right until item is in its correct position.
# The index i keeps track of the position where item should be inserted in the sorted sub-list.
# Finally, item is inserted at index i in the sorted sub-list.
# The original list and the sorted list are printed to the console.

A = [5, 2, -3, 4, 6, -7, 1, 9, 12, 5, -6]

# Print the original list
print("list =", A)

for k in range(1, len(A)):
    # Keep the value of index k
    item = A[k]

    # Assign k to another variable so that k doesn't change
    i = k

    # Shift larger values to the right
    while i > 0 and item < A[i - 1]:
        A[i] = A[i - 1]
        i -= 1

    # Insert the item in its sorted position
    A[i] = item

    # Print the list after each iteration (optional)
    print(A)

# Print the sorted list
print("sorted list =", A)
