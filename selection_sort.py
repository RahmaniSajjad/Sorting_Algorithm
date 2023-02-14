# The code sorts the list using selection sort algorithm and prints the sorted list and the number of comparisons made.
# The loop selects the minimum element and swaps it with the first element of the unsorted part of the list, and continues to do so until the entire list is sorted.
# The number of comparisons made is stored in the variable dd.

A = sorted([12, 3, 15, -4, 7], reverse=True)  # Create a list of numbers and sort it in descending order
n = len(A)  # Get the length of the list
print("list =", A)  # Print the original unsorted list
dd = 0  # Initialize a variable to count the number of comparisons made

for i in range(n - 1):  # Loop through the list from the first index to the second to last index
    min_index = i  # Assume the current index has the minimum value
    for j in range(i + 1, n):  # Loop through the unsorted part of the list to find the actual minimum value
        dd += 1  # Increment the number of comparisons made
        if A[min_index] > A[j]:  # If a smaller value is found, update the index of the minimum value
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]  # Swap the current value with the minimum value found
    print(A)  # Print the list after each iteration

print("sorted list =", A)  # Print the final sorted list
print(dd)  # Print the number of comparisons made during the sort
