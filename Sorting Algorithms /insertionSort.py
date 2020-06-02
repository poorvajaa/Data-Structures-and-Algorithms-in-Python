# Insertion sort
def insertion_sort(array):
    for pointer in range(1, len(array)):
        current_value = array[pointer]
        position = pointer
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = current_value


if __name__ == '__main__':
    unsorted_array = [7, 8, 5, 2, 4]
    insertion_sort(unsorted_array)
    print(unsorted_array)