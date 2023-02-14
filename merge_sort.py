# The code implements the merge sort algorithm to sort a list of integers.
# The algorithm works by dividing the list into two halves, recursively sorting each half, and then merging the two sorted halves.
# The merge_sort function is defined to perform the sorting.
# If the input list has zero or one elements, the function returns the list unchanged.
# Otherwise, the function computes the midpoint of the list, divides the list into left and right halves, and recursively calls itself on each half.
# The sorted left and right halves are then merged using a while loop that compares the first elements of each half and appends the smaller one to the merged list.
# Finally, any remaining elements from either half are appended to the merged list.
# The original list and the sorted list are printed to the console for each recursive call to the merge_sort function.

def merge_sort(A):
    # Base case: a list of zero or one elements is already sorted
    if len(A) < 2:
        print("A is :", A)
        print("len(A) < 2 so return A")
        print("-----------------------")
        return A

    # Divide the list into two halves
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    print("A is :", A)
    print("L is :", L)
    print("R is :", R)
    print()

    # Recursively sort the two halves
    L = merge_sort(L)
    R = merge_sort(R)

    print("sorted L is :", L)
    print("sorted R is :", R)
    print()

    # Merge the sorted halves
    A = []  # The merged list will be stored in A
    i = j = 0  # i and j are indices for the left and right halves, respectively
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1

    # Append any remaining elements from the left or right half
    A += L[i:]
    A += R[j:]

    print("merged R and L is :", A)
    print("-----------------------")

    return A


# Test the merge_sort function with a sample list
arr = [20, 47, 15, 8, 9, 4, 40, 30, 12, 17]
print("list =", arr)
print("-----------------------")
sorted_arr = merge_sort(arr)
print("sorted list =", sorted_arr)
