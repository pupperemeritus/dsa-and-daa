def counting_sort(arr, digit):
    """
    Perform counting sort on the given array based on the specified digit.

    Args:
        arr (List[int]): The array to be sorted.
        digit (int): The digit to be used for sorting.

    Returns:
        List[int]: The sorted array.

    """
    # Initialize the cumulative and output arrays
    cumulative = [0] * 10
    output = [0] * len(arr)

    # Count the frequency of each digit
    for i in range(len(arr)):
        cumulative[(arr[i] // digit) % 10] += 1

    # Calculate the cumulative sum of frequencies
    for i in range(1, 10):
        cumulative[i] += cumulative[i - 1]

    # Build the sorted output array
    for i in range(len(arr) - 1, -1, -1):
        output[cumulative[(arr[i] // digit) % 10] - 1] = arr[i]
        cumulative[((arr[i] // digit) % 10)] -= 1

    return output


def neg_placer(arr):
    """
    Rearranges the elements in the input list so that all negative numbers appear before any positive numbers.

    Args:
        arr (list): The input list of numbers.

    Returns:
        list: The rearranged list.
    """
    # Find the first positive number in the list
    i = 0


def radixsort(arr):
    """
    Sorts an array using the radix sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    # Find the maximum element in the array
    m = max(arr)

    # Initialize the digit variable
    digit = 1

    # Continue sorting until all digits have been considered
    while m / digit > 1:
        # Sort the array by the current digit using counting sort
        arr = counting_sort(arr, digit)

        # Move to the next digit
        digit *= 10

    # If the array contains negative numbers, place them before the positive numbers
    if min(arr) < 0:
        arr = neg_placer(arr)

    # Return the sorted array
    return arr

    return arr


def radixsort(arr):
    digit = 1
    m = max(arr)
    while m / digit > 1:
        arr = counting_sort(arr, digit)
        digit *= 10
    if min(arr) < 0:
        arr = neg_placer(arr)
    return arr


if __name__ == "__main__":
    arr = [-3, -43, -54, -65, 5, 3, 4, 2, 6, 54, 56, 87, 45, 34, 25, 456]
    arr = radixsort(arr)
    print(arr)
