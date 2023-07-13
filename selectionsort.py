def selection_sort(array):
    """
    Sorts an array in ascending order using the selection sort algorithm.

    Args:
        array (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(array)

    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the current element if necessary
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    array = [4, 62, 34, 6, 3, 453, 27, 25, 25, 27, 56, 85]
    array = selection_sort(array)
    print(array)
