# import time


# Merge sort
def merge_sort(array):
    # start_time = time.time()
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1
    # print(time.time() - start_time)


unsorted_array = [8, 9, 27, 28, 18, 4, 9]
merge_sort(unsorted_array)
print(unsorted_array)