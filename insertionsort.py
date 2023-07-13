def ins_sort(array):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    Args:
        array (list): The array to be sorted.

    Returns:
        None. The array is sorted in-place.
    """
    n = len(array)
    for i in range(1, n):
        k = i
        j = 0
        while array[k] > array[j]:
            j += 1
        print(array)
        array.insert(j, array.pop(k))


if __name__ == "__main__":
    array = [14, 5, 7, 48, 56, 45, 23, 45, 38, 45, 68, 97]
    ins_sort(array)
    print(array)
