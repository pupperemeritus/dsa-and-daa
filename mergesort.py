def merge_sort(arr):
    """
    Sorts the given array using the merge sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        None. The array is sorted in-place.
    """
    if len(arr) == 1:
        return arr[:0]

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right)


def merge(left, right):
    """
    Merge two arrays `left` and `right` into a single sorted array.

    Parameters:
    - left (list): The first array to be merged.
    - right (list): The second array to be merged.

    Returns:
    - None: This function does not return anything.
    """
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [45, 63, -32, -54, -76, 34, 74, 86]
    merge_sort(arr)
    print(arr)
