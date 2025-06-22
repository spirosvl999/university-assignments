def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

                                              # The Temp Arrays
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0                                      # First subarray
    j = 0                                      # Second subarray
    k = left                                   # Merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:                              # Copying whats left to the final array.
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:                              # Copying whats left to the final array.
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()
