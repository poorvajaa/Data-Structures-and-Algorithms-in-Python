import time


def quick_sort(array):
    # start_time = time.time()
    if not array:
        return []
    pivots = [x for x in array if x == array[0]]
    less = quick_sort([x for x in array if x < array[0]])
    greater = quick_sort([x for x in array if x > array[0]])
    return less + pivots + greater
    # print(time.time() - start_time)


if __name__ == '__main__':
    unsorted_array = [7, 8, 5, 2, 4]
    result = quick_sort(unsorted_array)
    print(result)
