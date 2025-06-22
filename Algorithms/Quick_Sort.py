# We imagine we have an array named arr as an input

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)
