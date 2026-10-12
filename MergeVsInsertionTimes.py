from typing import Callable, List, TypeVar

T = TypeVar("T")  # represents generic type

def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list in place using insertion sort algorithm.

    :param data: List of type T to be sorted
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
     treated as less than or equal to the second argument.
    :param descending: Perform the sort in descending order when this is True
    """
    if descending:
        for i in range(len(data)):
            j = i
            while j > 0 and comparator(data[j - 1], data[j]):
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1
    else:
        for i in range(1, len(data)):
            j = i
            while j > 0 and comparator(data[j], data[j - 1]):
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1



def merge_sort(data: List[T], *,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts a list in-place using a hybrid sort with the merge sort and insertion sort algorithms
    Uses insertion_sort to sort lists once their size is less than or equal to threshold,
    and otherwise performs a merge sort

    :param data: List of type T to be sorted
    :param threshold: Maximum size at which insertion sort will be used instead of merge sort
    :param comparator: A function which takes two arguments of type T and returns True when the first argument should be
     treated as less than or equal to the second argument.
    :param descending: Perform the sort in descending order when this is True
    """
    n = len(data)
    if n <= 1:
        return
    mid = n // 2
    left = data[0:mid]
    right = data[mid:n]
    merge_sort(left, comparator=comparator, descending=descending)
    merge_sort(right, comparator=comparator, descending=descending)
    merge(left, right, data, comparator, descending)


def merge(left, right, data, comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    i = j = 0
    if descending:
        while i + j < len(data):
            if j == len(right) or (i < len(left) and comparator(right[j], left[i])):
                data[i + j] = left[i]
                i = i + 1
            else:
                data[i + j] = right[j]
                j = j + 1

    else:
        while i + j < len(data):
            if j == len(right) or (i < len(left) and comparator(left[i], right[j])):
                data[i + j] = left[i]
                i = i + 1
            else:
                data[i + j] = right[j]
                j = j + 1