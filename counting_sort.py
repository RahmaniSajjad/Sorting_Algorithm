# The code implements the counting sort algorithm to sort a list of integers.
# The algorithm counts the number of occurrences of each value in the list, then rebuilds the list in sorted order using the counts.
# The maximum value in the list is found using the max function.
# The counts are stored in a list count with one element for each possible value between 0 and m.
# The input list is cleared, and a new sorted list is built by appending each value i to the input list A count[i] times.
# Finally, the sorted list is returned.
# The input list and the sorted list are printed to the console.

def counting_sort(A):
    # Find the maximum value in the list
    m = max(A)

    # Initialize a list of counts for each value between 0 and m
    count = [0] * (m + 1)

    # Count the number of occurrences of each value in the list
    for x in A:
        count[x] += 1

    # Print the count of each item in A
    print(f"count between [0,{m}] : ", count)

    # Clear the input list
    A.clear()

    # Rebuild the input list in sorted order using the counts
    for i in range(m + 1):
        A += [i] * count[i]

    # Return the sorted list
    return A


# Example usage of the counting_sort function
data = [1, 2, 2, 2, 1, 3, 3, 1, 2, 4, 5]
print("list : ", data)

sorted_data = counting_sort(data)
print("sorted list : ", sorted_data)
