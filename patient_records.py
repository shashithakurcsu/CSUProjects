import time

# Function to merge two halves
def merge(left_half, right_half):
    sorted_array = []
    i = j = 0

    # Merge the two halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1

    # Collect the remaining elements
    sorted_array.extend(left_half[i:])
    sorted_array.extend(right_half[j:])

    return sorted_array

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Function to measure time taken by sorting algorithms
def measure_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr.copy())
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Test the sorting functions with timing
patient_records = [4067, 9754, 2356, 4321, 4412, 6677, 9876, 1102, 2345, 8867, 2234, 9981, 6644, 8866, 8899]

sorted_bubble, bubble_time = measure_time(bubble_sort, patient_records)
sorted_merge, merge_time = measure_time(merge_sort, patient_records)

print("Bubble Sort Result:", sorted_bubble)
print("Bubble Sort Time Taken: {:.6f} seconds".format(bubble_time))

print("Merge Sort Result:", sorted_merge)
print("Merge Sort Time Taken: {:.6f} seconds".format(merge_time))
