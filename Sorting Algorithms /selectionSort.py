# import time


# Selection Sort
def selection_sort(array):
    # start_time = time.time()
    for pointer in range(len(array) - 1, 0, -1):
        max_position = 0
        for location in range(1, pointer + 1):
            if array[location] > array[max_position]:
                max_position = location
        temp = array[pointer]
        array[pointer] = array[max_position]
        array[max_position] = temp
    # print(time.time() - start_time)


unsorted_array = [8, 9, 27, 28, 18, 4, 9]
selection_sort(unsorted_array)
print(unsorted_array)
