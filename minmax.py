# def array_comparator(arr, comp):
#     refelem = arr[0]
#     for elem in arr:
#         if comp(elem, refelem):
#             refelem = elem
#     return refelem


def minmax_rec(arr):
    """
    Recursively finds the minimum and maximum values in an array.

    Parameters:
    - arr (list): The input array.

    Returns:
    - list: A list containing the minimum and maximum values in the input array.
    """
    if len(arr) == 1:
        return [arr[0], arr[0]]
    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return arr[::-1]
    elif len(arr) > 2:
        mid = len(arr) // 2
        min1, max1 = minmax_rec(arr[:mid])
        min2, max2 = minmax_rec(arr[mid:])
        if min1 < min2:
            min3 = min1
        else:
            min3 = min2
        if max1 > max2:
            max3 = max1
        else:
            max3 = max2
        return [min3, max3]


arr = [3, 32, 4, 34, 533, 433, 2233, 5343, 223, 23, 43, 53, -3]
# print(array_comparator(arr, lambda x, y: x > y))
print(minmax_rec(arr))
# print(array_comparator(arr, lambda x, y: x < y))
