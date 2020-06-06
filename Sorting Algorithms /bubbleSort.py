# import time


def bubble_sort(array):
    # start_time = time.time()
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    # print(time.time() - start_time)


if __name__ == '__main__':
    unsorted_array = [8, 9, 27, 28, 18, 4, 9]
    bubble_sort(unsorted_array)
    print(unsorted_array)
