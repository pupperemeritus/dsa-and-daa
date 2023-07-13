def heapsort(arr):
    """
    Sorts an array using the heapsort algorithm.

    Parameters:
        arr (list): The array to be sorted.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

    # Move the largest element to the end and heapify the remaining elements
    for i in range(n - 1, 0, -1):
        swap(arr, i, 0)
        heap(arr, i, 0)


def heap(arr, n, i):
    """
    Heapify the array by comparing the value at index i with its left and right child.
    If necessary, swap the value with the maximum of the three and recursively heapify the affected subtree.

    Args:
        arr (List[int]): The array to be heapified.
        n (int): The size of the heap.
        i (int): The index of the element to be heapified.

    Returns:
        None
    """
    m = i  # Initialize the maximum value index
    left = 2 * i + 1  # Calculate the left child index
    right = 2 * i + 2  # Calculate the right child index

    # Compare the value at index i with its left child
    if left < n and arr[m] < arr[left]:
        m = left

    # Compare the value at index i with its right child
    if right < n and arr[m] < arr[right]:
        m = right

    # If the maximum value index is not the same as the current index i, swap the values
    if m != i:
        swap(arr, m, i)
        heap(arr, n, m)


def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


if __name__ == "__main__":
    arr = [3, 6, 4, 3, 4, 6, -2, 4, -35, 7]
    heapsort(arr)
    print(arr)
