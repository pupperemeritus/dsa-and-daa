from typing import List


def quicksort(arr: List[int], low: int, high: int) -> List[int]:
    """
    Sorts an array of integers in ascending order using the quicksort algorithm.

    Args:
        arr: List of integers to be sorted.
        low: Starting index of the partition to be sorted.
        high: Ending index of the partition to be sorted.

    Returns:
        The sorted list of integers.
    """
    # Base case
    if len(arr) == 1:
        return arr

    # Recursive case
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

    return arr


def partition(arr: list[int], low: int, high: int) -> int:
    """
    This function takes an array, a low index, and a high index as input.
    It chooses the last element as the pivot and places it in its sorted position.
    All smaller elements than the pivot are moved to the left of the pivot while all larger elements are moved to its right.
    The function returns the index of the pivot.

    Args:
        arr: A list of integers
        low: The minimum index of the list to be partitioned
        high: The maximum index of the list to be partitioned

    Returns:
        An integer representing the index of the pivot
    """
    pivot = arr[high]
    j = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            j += 1
            swap(arr, i, j)
    swap(arr, j + 1, high)
    return j + 1


def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


if __name__ == "__main__":
    arr = [2, 46, -6, -10, 43, 74, 55, 39, 20]
    arr = quicksort(arr, 0, len(arr) - 1)
    print(arr)
